Build a compact 8-inch-class Android tablet like the one in these photos: front, back and a teardown. The brand in
the photos must never appear in the design; the brand gate enforces this.

Study the photos closely, especially the teardown:
- **Battery:** one large flat pouch filling most of the interior.
- **Logic board:** a narrow strip along one long edge.
- **Speakers:** chambers at the top and bottom ends.
- **USB-C:** a small daughter board centred on the bottom edge.
- **Rear camera:** in the top corner of the back.
- **Display:** fills the front inside a thin, even border.

Match those placements, the display-to-bezel look, and the flat back with rounded edges.

**Rear (owner feedback on i1; measured on the reference's straight-on rear view).** i1's rear looked nothing like
the reference: 5.2 mm corners, a 39.5 x 9 mm slot for the camera, no flash and a plastic strip on the back. Match
these instead (rear view, from the top-left corner as seen from behind):
- **Corners:** 14 mm plan-view radius. The mainboard must not push the case corners in: radius or clip its corner
  so it fits inside the wall.
- **Camera:** one round raised lens ring, about 13.5 mm across and about 1 mm proud of the back, centred about
  14.8 mm from the top and 14.8 mm from the side edge. The thickness at the bump is about 10.4 mm; everywhere else
  it stays 9.4 mm.
- **Microphone:** a real rear microphone behind a round hole about 1 mm across, centred about 24.6 mm from the top,
  on the camera's centre line.
- **Flash:** a real LED flash, with its driver on the mainboard, behind a round window about 5.6 mm across, centred
  about 33 mm from the top on the same line.
- **Nothing else on the back.** No logo and no plastic strip. The Wi-Fi antenna's RF window is a thin plastic insert
  in the top edge wall, over the antenna, invisible from the back.

**Overall size.** About 134 x 198 mm (the reference is 132.6 x 195.3 mm) and about 9.4 mm thick. It is thicker than
the reference on purpose, because the display module below is 3.2 mm thick.

| Layer | Thickness |
|---|---|
| Cover glass with touch sensor | 1.1 mm |
| Display | 3.2 mm |
| Foam / clearance | 0.3 mm |
| Battery, with swell allowance | 3.8 mm |
| Back shell | 1.0 mm |

**Display (decided).** Sharp LQ084R1SX01, a bought part.
- 8.4-inch oxide TFT, 1600 x 2560.
- Active area 113.04 x 180.864 mm; module outline 117.04 x 191.164 x 3.2 mm.
- Built-in LED backlight with no driver, and no touch.
- Interface: MIPI-DSI with 2 channels x 4 data lanes.

Driving it from the board:
- Wire both RK3566 DSI ports to it, in dual-channel mode.
- Put the WLED boost backlight driver on the mainboard.
- Add a separate bonded touch sensor on the cover glass, with its own FPC to a touch controller over I2C + INT + RST.

The side bezels will come out near 10 mm; the module border is about 2 mm, so the enclosure walls set the look.

Record two risks in `decisions` as bring-up risks:
- 1600 x 2560 is about 11% above the RK3566's listed dual-DSI limit (2560 x 1440 @ 60), so the panel may need a
  reduced refresh rate.
- The RK3576 is the upgrade path.

If the panel's FPC pinout cannot be found, model the connector from the closest Sharp dual-DSI sibling (LQ101R1SX01)
and say so.

**Back shell (decided).** CNC aluminium (JLC CNC), about 1.0 mm walls, flat back with rounded edges.
- An RF window for the Wi-Fi antenna: a thin plastic insert in the top edge wall, not on the back.
- A 0.5 mm thermal pad from the SoC shield to a graphite sheet bonded to the aluminium back.

**Mainboard (the core of this build; it must be detailed).** Follow this rough spec.
- **Board:** about 28 x 125 mm, 8 layers, 0.8 mm finished, ENIG, built by JLCPCB.
  - 8 layers at 0.8 mm, via-in-pad (filled and capped) and impedance control are standard there.
  - Vias down to 0.15 mm drill / 0.25 mm pad; 3.5/3.5 mil trace/space (3 mil in BGA fan-outs).
- **Position:** along one long edge under the display, with the battery filling the rest.
- **Height limits:** top-side parts at most 1.2 mm, bottom-side at most 1.0 mm.
- **Mounting:** 4 x M1.4 screw holes.
- **Shielding:** solder-down shield frames over the SoC/RAM and over the PMIC.

**Compute.**
- **SoC:** Rockchip RK3566, chip-down; LCSC C2943786, with real symbol and footprint from its EasyEDA entry.
- **RAM:** one 4 GB LPDDR4X x32 package on the RK3566's DDR support list, within 15 mm of the SoC.
- **Storage:** 64 GB eMMC 5.1 (153-ball).
- **PMIC:** RK817 for every SoC rail plus charger, fuel gauge and audio codec. VDD_CPU on its own external buck
  (TCS4525 class), as in Rockchip's reference.

**Stackup, top to bottom.**

| Layer | Use |
|---|---|
| L1 | Fan-out, RF, short signals |
| L2 | Ground |
| L3 | LPDDR4X byte lanes |
| L4 | Power planes |
| L5 | Ground |
| L6 | LPDDR4X CA, MIPI, USB |
| L7 | Ground |
| L8 | Passives, connectors |

**Impedance targets.**

| Interface | Target |
|---|---|
| General signals, eMMC | 50 ohm |
| LPDDR4X DQ/CA | ~40 ohm single-ended, ~80 ohm differential (DQS, CK) |
| MIPI-DSI/CSI | 100 ohm differential |
| USB 2.0 | 90 ohm differential |
| Antenna feed | 50 ohm |

Declare these as `electrical.high_speed` groups, with length tolerances from the RK3566 Hardware Design Guide:
- every DDR byte lane;
- the CA group;
- DSI0, DSI1, the camera CSI and USB.

**Placement along the strip.**
- Antenna end: Wi-Fi/BT module with antenna feeds at the plastic window.
- Compute block: SoC, LPDDR4X and eMMC, shielded.
- Display and camera FPC connectors, where the flexes fold straight onto the panel and camera.
- Power block: PMIC, charger, inductors, a 3-pin battery connector (V+, NTC, GND).
- Bottom end: an FPC to the USB-C daughter board, a Class-D speaker amplifier, and the button flex.

**Connectors and test points.**
- 0.5 mm FPC for USB-C (USB 2.0, CC, VBUS); a 6-10 pin FPC for touch; a 24-30 pin camera connector.
- Test pads for UART debug, the maskrom pin and every power rail.

**USB-C daughter board** (about 12 x 25 mm).
- 5.1 k CC pull-downs for 5 V / 3 A sink.
- ESD on CC and D+/D-.
- FPC to the mainboard.

**Power.**
- A single 1S Li-Po, 18-25 Wh, with NTC and a protection board on the pack; a bought cell with a datasheet.
- Power budget: about 2.4 W typical, 6 W peak.

**Buttons.** Top button and volume buttons on a small flex.

**Audio.** Two micro-speakers at the top and bottom ends, in landscape stereo.

**Cameras.** One rear and one front camera module, both bought MIPI-CSI modules.

**Reference designs** (fetch and read; do not copy their files into the repo):
- Rockchip RK3566 Hardware Design Guide (DDR rules, power, the RK817 reference schematic).
- The open RK3566 + LPDDR4X tablet schematic at https://github.com/PuntoMaximo/VonVisionAI_hardware
  (`Hardware/Board.kicad_sch`).
- Open RK3566 boards (Radxa Zero 3, PineTab2, LCSC TaishanPi) for the SoC-to-LPDDR4X fan-out.

**Build order.**
1. Back shell.
2. Mainboard and USB-C board.
3. Battery.
4. Speakers, cameras and flexes.
5. Display.
6. Cover glass with touch, bonded last.
