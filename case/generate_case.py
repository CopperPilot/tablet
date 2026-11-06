#!/usr/bin/env python3
"""Parametric CAD generator for the Compact 8.4-inch Android Tablet enclosure and purchased models."""

from __future__ import annotations

from pathlib import Path
from rea_hardware import cad


def _feature_map(spec: dict) -> dict[str, dict]:
    return {f["id"]: f for f in spec["fidelity"]["must_match"]}


def _front_to_world(origin: list[float], u: float, v: float) -> tuple[float, float]:
    return float(origin[0]) + float(u), float(origin[1]) - float(v)


def _rear_to_world(origin: list[float], env_w: float, u: float, v: float) -> tuple[float, float]:
    return float(origin[0]) + float(env_w) - float(u), float(origin[1]) - float(v)


def build_enclosure(bf: dict) -> None:
    spec = bf["spec"]
    feats = _feature_map(spec)

    env_w = float(bf["env_w"])       # 134.0
    env_h = float(bf["env_h"])       # 198.0
    env_d = float(bf["env_d"])       # 9.4
    corner_r = float(bf["corner_r"]) # 14.0
    ox, oy, oz = [float(x) for x in bf["front_origin"]]  # [-103.0, 22.0, 6.6]

    x_min, x_max = ox, ox + env_w    # -103.0 .. +31.0
    y_min, y_max = oy - env_h, oy    # -176.0 .. +22.0
    z_max = oz                       # +6.6
    z_min = oz - env_d               # -2.8
    cx = 0.5 * (x_min + x_max)       # -36.0
    cy = 0.5 * (y_min + y_max)       # -77.0
    envelope_xy = (x_min, y_min, x_max, y_max)

    # Feature coordinates from spec
    f_disp = feats["F_DISPLAY"]
    disp_cx, disp_cy = _front_to_world(bf["front_origin"], *f_disp["center_mm"])
    disp_w, _disp_h = [float(v) for v in f_disp["size_mm"]]
    # Match uniform ~10.5 mm bezel around active window for fidelity.dims bezel measurement
    win_w = disp_w                   # 113.04 mm
    win_h = env_h - (env_w - disp_w) # 177.04 mm

    f_fcam = feats["F_FRONT_CAM"]
    fcam_cx, fcam_cy = _front_to_world(bf["front_origin"], *f_fcam["center_mm"])
    fcam_d = float(f_fcam["size_mm"][0])  # 3.0 mm

    f_rcam = feats["F_REAR_CAM"]
    rcam_cx, rcam_cy = _rear_to_world(bf["front_origin"], env_w, *f_rcam["center_mm"])
    rcam_od = float(f_rcam["size_mm"][0]) # 13.5 mm

    f_rmic = feats["F_REAR_MIC"]
    rmic_cx, rmic_cy = _rear_to_world(bf["front_origin"], env_w, *f_rmic["center_mm"])
    rmic_d = float(f_rmic["size_mm"][0])  # 1.0 mm

    f_rfl = feats["F_REAR_FLASH"]
    rfl_cx, rfl_cy = _rear_to_world(bf["front_origin"], env_w, *f_rfl["center_mm"])
    rfl_d = float(f_rfl["size_mm"][0])   # 5.6 mm

    f_usbc = feats["F_USBC"]
    usbc_cx = x_min + float(f_usbc["center_mm"][0])  # -36.0 mm

    f_pwr = feats["F_BTN_PWR"]
    pwr_cx = x_min + float(f_pwr["center_mm"][0])    # +6.8 mm
    pwr_w, pwr_h = [float(v) for v in f_pwr["size_mm"]]
    btn_z = z_max - float(f_pwr["center_mm"][1])     # +1.9 mm

    f_vup = feats["F_BTN_VOL_UP"]
    vup_cx = x_min + float(f_vup["center_mm"][0])    # -71.0 mm
    vup_w, vup_h = [float(v) for v in f_vup["size_mm"]]

    f_vdn = feats["F_BTN_VOL_DN"]
    vdn_cx = x_min + float(f_vdn["center_mm"][0])    # -83.2 mm
    vdn_w, vdn_h = [float(v) for v in f_vdn["size_mm"]]

    # -------------------------------------------------------------------------
    # 1. back_shell: CNC 6061-T6 aluminium unibody shell
    # -------------------------------------------------------------------------
    outer = cad.loft(
        [
            (z_min, env_w - 1.2, env_h - 1.2, corner_r - 0.6, cx, cy),
            (z_min + 0.55, env_w, env_h, corner_r, cx, cy),
            (z_max, env_w, env_h, corner_r, cx, cy),
        ]
    )

    # Integral raised rear camera lens ring (0.95 mm proud -> Z = -3.75 .. -1.80)
    cam_bump_z0 = z_min - 0.95
    cam_ring = cad.cylinder(r=0.5 * rcam_od, h=(z_min + 1.0) - cam_bump_z0, at=(rcam_cx, rcam_cy, cam_bump_z0))
    shell = outer + cam_ring

    # Main interior cavity (1.20 mm perimeter walls, 1.00 mm floor at Z = -2.80 .. -1.80)
    wall_t = 1.20
    floor_z = z_min + 1.00  # -1.80 mm
    cavity = cad.rounded_box(
        env_w - 2.0 * wall_t,
        env_h - 2.0 * wall_t,
        (z_max - floor_z) + 1.0,
        r=corner_r - wall_t,
        at=(x_min + wall_t, y_min + wall_t, floor_z),
    )
    shell = shell - cavity

    # Vertical clearance relief on top inner wall for front_camera (X = -40.0 .. -32.0, Y = 12.8 .. 20.8)
    # Recessed to Y = 21.05 (leaving 0.95 mm outer CNC wall) from Z = 1.10 to Z = 6.70
    shell = shell - cad.box(9.00, 0.35, 5.60, at=(-40.50, 20.70, 1.10))

    # Upper perimeter step counterbore at Z = +5.55 .. +6.60 for front_bezel (leaves 0.90 mm outer aluminium rim)
    rim_wall_t = 0.90
    rim_ledge_z = 5.55
    rim_pocket = cad.rounded_box(
        env_w - 2.0 * rim_wall_t,
        env_h - 2.0 * rim_wall_t,
        (z_max - rim_ledge_z) + 0.5,
        r=corner_r - rim_wall_t,
        at=(x_min + rim_wall_t, y_min + rim_wall_t, rim_ledge_z),
    )
    shell = shell - rim_pocket

    # Rear camera ring stepped bore:
    # Inner through-bore d = 10.20 mm from Z = -2.85 .. +1.00; outer counterbore d = 11.60 mm from Z = -3.85 .. -2.85
    shell = shell - cad.hole(rcam_cx, rcam_cy, d=10.20, depth=4.0, z0=-2.85)
    shell = shell - cad.hole(rcam_cx, rcam_cy, d=11.60, depth=1.05, z0=-3.90)

    # Rear microphone through-hole at (16.2, -2.6): d = 1.00 mm (Z = -3.00 .. -1.60)
    shell = shell - cad.hole(rmic_cx, rmic_cy, d=rmic_d, depth=1.50, z0=-3.00)

    # Rear flash window opening at (16.2, -11.0): outer counterbore d = 5.60 mm (Z = -3.0 .. -2.15), inner bore d = 4.40 mm (Z = -2.15 .. -1.60)
    shell = shell - cad.hole(rfl_cx, rfl_cy, d=rfl_d, depth=0.90, z0=-3.05)
    shell = shell - cad.hole(rfl_cx, rfl_cy, d=4.40, depth=0.65, z0=-2.15)

    # Bottom USB-C opening centred on J1's 3D model mouth (X = -36.0, Z = +0.45 .. +4.35 -> z_center = 2.40, w = 9.80, h = 3.90)
    shell = shell - cad.edge_cut(
        axis="y",
        center=usbc_cx,
        z=2.40,
        w=9.80,
        h=3.90,
        side="min",
        envelope=envelope_xy,
        r=1.5,
        reach=4.0,
    )

    # Top edge button slots and inner flange pockets (leave 0.85 mm outer wall at Y = 21.15 .. 22.00)
    for bcx, bw, bh in ((pwr_cx, pwr_w, pwr_h), (vup_cx, vup_w, vup_h), (vdn_cx, vdn_w, vdn_h)):
        shell = shell - cad.edge_cut(
            axis="y",
            center=bcx,
            z=btn_z,
            w=bw + 0.50,
            h=bh + 0.50,
            side="max",
            envelope=envelope_xy,
            r=0.2,
            reach=3.0,
        )
        # Inner recess from Y = 20.50 to Y = 21.15 so outer wall is 0.85 mm thick
        shell = shell - cad.box(
            bw + 2.20,
            0.65,
            bh + 1.60,
            at=(bcx - 0.5 * (bw + 2.20), y_max - 0.85 - 0.65, btn_z - 0.5 * (bh + 1.60)),
        )

    # Upper-right edge RF window pocket centred at Y = -1.80, Z = +1.90 (aligned with ANT1 at Y = -1.80, Z = +1.14):
    # Inner through-slot w = 14.0, h = 2.6; outer pocket from X = 30.15 .. 31.10 with w = 16.5, h = 3.9
    rf_cy, rf_cz = -1.80, 1.90
    shell = shell - cad.edge_cut(
        axis="x",
        center=rf_cy,
        z=rf_cz,
        w=14.00,
        h=2.60,
        side="max",
        envelope=envelope_xy,
        r=1.0,
        reach=2.5,
    )
    shell = shell - cad.box(
        0.95,
        16.50,
        3.90,
        at=(30.15, rf_cy - 8.25, rf_cz - 1.95),
    )

    # Internal M1.4 standoffs under mainboard and USB-C daughterboard mounting holes
    for h in bf["holes"]:
        hx, hy = float(h["x_mm"]), -float(h["y_mm"])
        shell = shell + cad.standoff(hx, hy, floor_z, 0.02, od=4.2, id_=1.2)
    for sb in spec.get("sub_boards", []):
        sb_ox, sb_oy, _sb_oz = [float(v) for v in sb["world_position_mm"]]
        for h in sb.get("mounting_holes", []):
            hx = sb_ox + float(h["x_mm"])
            hy = sb_oy - float(h["y_mm"])
            shell = shell + cad.standoff(hx, hy, floor_z, 0.02, od=4.2, id_=1.2)

    cad.export(shell, "case/out/back_shell.stl")

    # -------------------------------------------------------------------------
    # 2. rf_window: Flush upper-right edge plastic RF window insert (press-fit along -X)
    # -------------------------------------------------------------------------
    rf_outer = cad.box(0.85, 16.00, 3.40, at=(30.15, rf_cy - 8.00, rf_cz - 1.70))
    rf_step = cad.box(0.05, 15.00, 3.00, at=(30.10, rf_cy - 7.50, rf_cz - 1.50))
    rf_inner = cad.box(0.25, 11.00, 1.60, at=(29.85, rf_cy - 5.50, rf_cz - 0.80))
    rf_win = rf_outer + rf_step + rf_inner
    cad.export(rf_win, "case/out/rf_window.stl")

    # -------------------------------------------------------------------------
    # 3. rear_camera_glass: Optical window inside raised camera ring (press-fit along +Z)
    # -------------------------------------------------------------------------
    rcam_outer = cad.cylinder(r=5.55, h=0.90, at=(rcam_cx, rcam_cy, -3.70))
    rcam_inner = cad.cylinder(r=4.85, h=1.05, at=(rcam_cx, rcam_cy, -3.70))
    cad.export(rcam_outer + rcam_inner, "case/out/rear_camera_glass.stl")

    # -------------------------------------------------------------------------
    # 4. flash_window: Rear flash diffuser + rear mic acoustic window (press-fit along +Z)
    # -------------------------------------------------------------------------
    fl_outer = cad.cylinder(r=2.55, h=0.70, at=(rfl_cx, rfl_cy, -2.80))
    fl_inner = cad.cylinder(r=1.95, h=0.30, at=(rfl_cx, rfl_cy, -2.10))
    mic_insert = cad.cylinder(r=0.40, h=0.80, at=(rmic_cx, rmic_cy, -2.60))
    flash_win = cad.union(fl_outer + fl_inner, mic_insert)
    cad.export(flash_win, "case/out/flash_window.stl")

    # -------------------------------------------------------------------------
    # 5. Buttons: power_button, vol_up_button, vol_down_button (captured along +Y)
    # -------------------------------------------------------------------------
    def _make_button(bcx: float, bw: float, bh: float) -> cad.Manifold:
        # Cap spans Y = 20.20 .. 22.35; inner retention flange spans Y = 20.20 .. 21.10 (0.90 mm thick >= 0.80 mm CNC min)
        cap = cad.box(bw, 2.15, bh, at=(bcx - 0.5 * bw, 20.20, btn_z - 0.5 * bh))
        flange_w = bw + 1.60
        flange_h = bh + 1.00
        flange = cad.box(flange_w, 0.90, flange_h, at=(bcx - 0.5 * flange_w, 20.20, btn_z - 0.5 * flange_h))
        return cap + flange

    cad.export(_make_button(pwr_cx, pwr_w, pwr_h), "case/out/power_button.stl")
    cad.export(_make_button(vup_cx, vup_w, vup_h), "case/out/vol_up_button.stl")
    cad.export(_make_button(vdn_cx, vdn_w, vdn_h), "case/out/vol_down_button.stl")

    # -------------------------------------------------------------------------
    # 6. front_bezel: Black front bezel mask frame with 3.0 mm front camera window
    # -------------------------------------------------------------------------
    bezel_margin = rim_wall_t + 0.25  # 1.15 mm inset from outer envelope -> 0.25 mm clearance inside rim_pocket
    bezel_w = env_w - 2.0 * bezel_margin
    bezel_h = env_h - 2.0 * bezel_margin
    bezel_r = corner_r - bezel_margin
    bezel_outer = cad.rounded_box(
        bezel_w,
        bezel_h,
        1.10,
        r=bezel_r,
        at=(x_min + bezel_margin, y_min + bezel_margin, 5.50),
    )
    # Narrow perimeter step (0.12 mm per side) at Z = 5.85 so >99% of bezel is full 1.10 mm thickness
    cut_upper = cad.rounded_box(
        win_w,
        win_h,
        1.00,
        r=6.0,
        at=(disp_cx - 0.5 * win_w, disp_cy - 0.5 * win_h, 5.85),
    )
    cut_lower = cad.rounded_box(
        win_w - 0.24,
        win_h - 0.24,
        0.60,
        r=5.88,
        at=(disp_cx - 0.5 * (win_w - 0.24), disp_cy - 0.5 * (win_h - 0.24), 5.40),
    )
    front_bezel = bezel_outer - cut_upper - cut_lower
    # 3.0 mm diameter front camera window at (-36.0, +16.8)
    front_bezel = front_bezel - cad.hole(fcam_cx, fcam_cy, d=fcam_d, depth=4.0, z0=4.50)
    cad.export(front_bezel, "case/out/front_bezel.stl")

    # -------------------------------------------------------------------------
    # 7. cover_glass: Active display cover glass window seated inside front_bezel
    # -------------------------------------------------------------------------
    cg_upper_w = win_w - 0.10
    cg_upper_h = win_h - 0.10
    cg_lower_w = win_w - 0.44
    cg_lower_h = win_h - 0.44
    cg_upper = cad.rounded_box(
        cg_upper_w,
        cg_upper_h,
        0.80,
        r=5.95,
        at=(disp_cx - 0.5 * cg_upper_w, disp_cy - 0.5 * cg_upper_h, 5.80),
    )
    cg_lower = cad.rounded_box(
        cg_lower_w,
        cg_lower_h,
        0.30,
        r=5.78,
        at=(disp_cx - 0.5 * cg_lower_w, disp_cy - 0.5 * cg_lower_h, 5.50),
    )
    cover_glass = cg_upper + cg_lower
    cad.export(cover_glass, "case/out/cover_glass.stl")


def build_purchased(bf: dict) -> None:
    purchased = bf["purchased"]
    Path("case/purchased").mkdir(parents=True, exist_ok=True)

    # 1. display_panel: 117.04 x 191.164 x 3.2 mm at [-94.52, -172.582, 2.3]
    dp = purchased["display_panel"]
    px, py, pz = [float(v) for v in dp["position_mm"]]
    pw, ph, pd = [float(v) for v in dp["dims_mm"]]
    # Main panel body up to Z = 5.15 mm (0.05 mm below touch_sensor at Z = 5.20 .. 5.50),
    # plus outer end rails rising to Z = 5.50 mm outside touch_sensor's Y span (-170.0 .. +16.0)
    dp_main = cad.rounded_box(pw, ph, pd - 0.35, r=4.0, at=(px, py, pz))
    dp_bot_rail = cad.rounded_box(pw, 2.20, pd, r=2.0, at=(px, py, pz))
    dp_top_rail = cad.rounded_box(pw, 2.20, pd, r=2.0, at=(px, py + ph - 2.20, pz))
    dp_solid = dp_main + dp_bot_rail + dp_top_rail
    # Notch around front_camera (X = -40.0 .. -32.0, Y = 12.8 .. 20.8)
    dp_solid = dp_solid - cad.box(9.20, 7.00, 4.00, at=(-40.60, 12.20, 2.00))
    # Backlight recess over rear_camera (X = 10.45 .. 21.95, Y = 1.45 .. 12.95, Z <= 2.60)
    dp_solid = dp_solid - cad.box(13.00, 13.00, 0.65, at=(9.90, 0.90, 2.25))
    # Backlight recess over usbc_board J1 USB-C receptacle (X = -48.5 .. -23.5, Y = -174.5 .. -162.5, Z <= 4.10)
    dp_solid = dp_solid - cad.box(26.00, 11.00, 2.15, at=(-49.00, -173.00, 2.25))
    cad.export(dp_solid, dp["model"])

    # 2. touch_sensor: 116.0 x 186.0 x 0.3 mm at [-94.0, -170.0, 5.2]
    ts = purchased["touch_sensor"]
    tx, ty, tz = [float(v) for v in ts["position_mm"]]
    tw, th, td = [float(v) for v in ts["dims_mm"]]
    ts_solid = cad.rounded_box(tw, th, td, r=4.0, at=(tx, ty, tz))
    # Notch around front_camera (X = -40.0 .. -32.0, Y = 12.8 .. 20.8)
    ts_solid = ts_solid - cad.box(9.20, 4.50, 1.00, at=(-40.60, 12.20, 5.00))
    cad.export(ts_solid, ts["model"])

    # 3. battery: 98.0 x 162.0 x 3.6 mm at [-100.5, -158.0, -1.6]
    bat = purchased["battery"]
    bx, by, bz = [float(v) for v in bat["position_mm"]]
    bw, bh, bd = [float(v) for v in bat["dims_mm"]]
    bat_solid = cad.rounded_box(bw, bh, bd, r=2.0, at=(bx, by, bz))
    cad.export(bat_solid, bat["model"])

    # 4. rear_camera: 11.5 x 11.5 x 5.2 mm at [10.45, 1.45, -2.6]
    rc = purchased["rear_camera"]
    rx, ry, rz = [float(v) for v in rc["position_mm"]]
    rw, rh, rd = [float(v) for v in rc["dims_mm"]]
    # Square sensor housing from Z = -1.50 .. +2.60 mm + round lens barrel d = 9.60 mm from Z = -2.60 .. -1.50 mm
    rc_base = cad.rounded_box(rw, rh, rd - 1.10, r=1.0, at=(rx, ry, rz + 1.10))
    rc_barrel = cad.cylinder(r=4.80, h=1.20, at=(rx + 0.5 * rw, ry + 0.5 * rh, rz))
    cad.export(rc_base + rc_barrel, rc["model"])

    # 5. front_camera: 8.0 x 8.0 x 3.8 mm at [-40.0, 12.8, 1.4]
    fc = purchased["front_camera"]
    fx, fy, fz = [float(v) for v in fc["position_mm"]]
    fw, fh, fd = [float(v) for v in fc["dims_mm"]]
    # Lower housing at Y = 12.8 .. 19.1, Z = 1.4 .. 5.2 + upper flange at Y = 19.1 .. 20.8, Z = 2.35 .. 5.2 (clears button_flex)
    fc_lower = cad.rounded_box(fw, fh - 1.70, fd, r=0.8, at=(fx, fy, fz))
    fc_upper = cad.rounded_box(fw, 2.00, fd - 0.95, r=0.8, at=(fx, fy + fh - 2.00, fz + 0.95))
    cad.export(fc_lower + fc_upper, fc["model"])

    # 6. top_speaker: 24.0 x 9.0 x 3.0 mm at [-78.0, 10.0, -1.4]
    tspk = purchased["top_speaker"]
    sx, sy, sz = [float(v) for v in tspk["position_mm"]]
    sw, sh, sd = [float(v) for v in tspk["dims_mm"]]
    cad.export(cad.rounded_box(sw, sh, sd, r=1.2, at=(sx, sy, sz)), tspk["model"])

    # 7. bottom_speaker: 24.0 x 9.0 x 3.0 mm at [-78.0, -173.0, -1.4]
    bspk = purchased["bottom_speaker"]
    bsx, bsy, bsz = [float(v) for v in bspk["position_mm"]]
    bsw, bsh, bsd = [float(v) for v in bspk["dims_mm"]]
    cad.export(cad.rounded_box(bsw, bsh, bsd, r=1.2, at=(bsx, bsy, bsz)), bspk["model"])

    # 8. button_flex: 98.0 x 3.0 x 1.2 mm at [-88.0, 17.5, 0.8]
    bfx = purchased["button_flex"]
    flx, fly, flz = [float(v) for v in bfx["position_mm"]]
    flw, flh, fld = [float(v) for v in bfx["dims_mm"]]
    # Main flex strip along Y = 19.50 .. 20.15 (leaving 0.05 mm gap to buttons at Y = 20.20)
    strip = cad.box(flw, 0.65, fld, at=(flx, 19.50, flz))
    # Connector tail tab at X = -3.0 .. +1.0 reaching Y = 17.50
    tail_tab = cad.box(4.00, 2.10, fld, at=(-3.00, fly, flz))
    # Alignment tab at X = -55.0 .. -50.0 reaching Y = 20.50 (away from buttons and cameras)
    align_tab = cad.box(5.00, 1.00, fld, at=(-55.00, fly + flh - 1.00, flz))
    cad.export(strip + tail_tab + align_tab, bfx["model"])


def main() -> None:
    bf = cad.board_frame("rea/spec.yaml")
    build_enclosure(bf)
    build_purchased(bf)


if __name__ == "__main__":
    main()
