# USB-C Daughter Board (`usbc_board`)

2-layer 0.8 mm ENIG PCB (`25.0 x 12.0 mm`, `1.5 mm` corner radius, plated M1.4 ground mounting holes `H1` at `(2.5, 6.0)` and `H2` at `(22.5, 6.0)`) positioned at the bottom edge of the tablet (`world_position_mm: [-48.5, -162.5, 0.0]`). Provides the user-facing USB-C 5 V power sink and USB 2.0 OTG data interface (`J1`), active 6.54 V typ (`6.32 V..6.75 V`) OVP / 5.94 V typ (`5.77 V` min) recovery / 2.43 A typ (`2.19 A..2.68 A`) OCP eFuse (`U2`, `TPS259470ARPWR`, programmed by `R6=34.8k`, `R7=5.62k`, `R8=9.09k`, `R9=1.37k`, `C5=4.7nF` on `DVDT` Pin 7 setting `dV/dt = 5.11 V/ms`, local output decoupling `C4=1uF` + freewheeling Schottky clamp diode `D5=PMEG3005EL,315` on `VBUS`, and wide `>= 1.5-2.0 mm` stitched `F.Cu`/`B.Cu` polygon pours across the full `2.4 mm` length of `U2` Pads 5 and 6 feeding `J2` Pads 11..16 symmetrically, with mainboard `U11` `BQ25895RTWR` input current limit capped `<= 2.00 A` [`10.0 W` max for the `2.4 W` typ / `6.0 W` peak tablet] strictly below `U2` `I_OL(min) = 2.19 A`), 22 V standoff / 28.6 V max flat-clamp `VBUS_IN` surge TVS protection (`D3`, `ESTVS2200DRVR` `C42400188`), 50 V unswitched `VBUS_IN` decoupling (`C1`, `1 uF` 50V `GRM155R61H105KE05D` `C1518208`) + pulse-rated 0.33 W 0603 RC hot-plug snubber (`R3`, `2.2 Ohm` `ERJPA3J2R2V` + `C3`, `1 uF` 50V 0603 `CL10A105KB8NNNC` `C15849`, keeping total unswitched capacitance on `VBUS_IN` at `2.0 uF <= 2.2 uF`), compensated 6.8 kOhm 1% CC1/CC2 pull-down resistors (`R1`, `R2`, `0402WGF6801TCE` `C25917`, yielding `Rd(eff) = 6.8 kOhm || [10 kOhm R4/R5 + 10 kOhm mainboard R49/R50] = 5.075 kOhm` within `5.1 kOhm +/- 10%`), dedicated ground-referenced CC1/CC2 ESD protection (`D1`, `D2`) with `10 kOhm` series overvoltage/current-limiting isolation resistors (`R4`, `R5`), flow-through USB 2.0 D+/D- ESD protection (`U1` with Pin 5 on `USB_ESD_VBUS` decoupled by `100 nF` 50V `C2` to `GND` and biased at `~4.7 V` DC from protected `VBUS` via `1.0 kOhm` `R10` and `70 V` ultra-low-leakage blocking diode `D4` `BAS70L,315` on `USB_ESD_BIAS`), and a 16-pin 0.5 mm pitch FPC link (`J2`) to mainboard connector `J6`.

## Inter-Board 16-Pin FPC Cable Pinout (`usbc_fpc_cable`: Mainboard `J6` <-> `usbc_board` `J2`)

1-to-1 pin mapping across top-mounted `J6` (`0.5K-QX-16PWB` on `main`) and top-mounted `J2` (`0.5K-QX-16PWB` on `usbc_board`) joined by a mandated **2 oz (`0.070 mm`) heavy-copper Type-B** (opposite-side contact, Pin 1 to Pin 1) 16-pin 0.5 mm FFC cable (`FFC-0.5-16P-92MM-TYPE-B`, `0.50 A/pin` connector contact rating = `3.00 A` across 6 parallel `VBUS` contacts, protected by `U2`'s `2.43 A` typ / `2.68 A` max active OCP limit):

| `J6` Pin (Mainboard) | `J2` Pin (`usbc_board`) | Net Name | Signal / Power Function | Contact Rating & Allocation |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | `USB_OTG0_DP` | USB 2.0 OTG Data + (`RK3566.USB_OTG0_DP`) | 90 Ohm diff pair |
| 2 | 2 | `USB_OTG0_DM` | USB 2.0 OTG Data - (`RK3566.USB_OTG0_DM`) | 90 Ohm diff pair |
| 3 | 3 | `GND` | High-speed reference ground adjacent to D+/D- | 0.50 A contact (1 of 8 GND returns) |
| 4 | 4 | `USB_CC1` | Isolated USB-C CC1 sense (behind 10 kOhm series limiter `R4`) | Signal (`< 1 mA` fault current) |
| 5 | 5 | `USB_CC2` | Isolated USB-C CC2 sense (behind 10 kOhm series limiter `R5`) | Signal (`< 1 mA` fault current) |
| 6 | 6 | `GND` | Power return & shield ground | 0.50 A contact (2 of 8 GND returns) |
| 7 | 7 | `GND` | Power return & shield ground | 0.50 A contact (3 of 8 GND returns) |
| 8 | 8 | `GND` | Power return & shield ground | 0.50 A contact (4 of 8 GND returns) |
| 9 | 9 | `GND` | Power return & shield ground | 0.50 A contact (5 of 8 GND returns) |
| 10 | 10 | `GND` | Power return & shield ground | 0.50 A contact (6 of 6 signal GND pins = 3.00 A) |
| 11 | 11 | `VBUS` | Protected 5 V rail from `U2` (`TPS259470ARPWR` VOUT, 2.43 A typ / 2.68 A max OCP) | 0.50 A contact (1 of 6 VBUS contacts) |
| 12 | 12 | `VBUS` | Protected 5 V rail from `U2` (`TPS259470ARPWR` VOUT, 2.43 A typ / 2.68 A max OCP) | 0.50 A contact (2 of 6 VBUS contacts) |
| 13 | 13 | `VBUS` | Protected 5 V rail from `U2` (`TPS259470ARPWR` VOUT, 2.43 A typ / 2.68 A max OCP) | 0.50 A contact (3 of 6 VBUS contacts) |
| 14 | 14 | `VBUS` | Protected 5 V rail from `U2` (`TPS259470ARPWR` VOUT, 2.43 A typ / 2.68 A max OCP) | 0.50 A contact (4 of 6 VBUS contacts) |
| 15 | 15 | `VBUS` | Protected 5 V rail from `U2` (`TPS259470ARPWR` VOUT, 2.43 A typ / 2.68 A max OCP) | 0.50 A contact (5 of 6 VBUS contacts) |
| 16 | 16 | `VBUS` | Protected 5 V rail from `U2` (`TPS259470ARPWR` VOUT, 2.43 A typ / 2.68 A max OCP) | 0.50 A contact (6 of 6 VBUS contacts = 3.00 A contact rating > 2.68 A max OCP) |
| 17, 18 | 17, 18 | `GND` | Soldered mechanical reinforcement & return tabs | Shield ground (7 & 8 of 8 GND returns) |

## Complete Daughterboard BOM & Datasheet Verification

| Ref | MPN | LCSC | Value / Spec | Footprint | Function & Datasheet Margin |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `J1` | `TYPE-C-31-M-12` | `C165948` | 16P USB-C Receptacle (20V/5A) | `lcsc:USB-C_SMD-TYPE-C-31-M-12_1` | Dual `VBUS_IN` (`A4B9`, `B4A9`), dual `GND` (`A1B12`, `B1A12`), 4 grounded shell tabs |
| `J2` | `0.5K-QX-16PWB` | `C2919481` | 16P 0.5mm FPC Connector | `lcsc:FPC-SMD_16P-P0.50_HDGC_0.5K-QX-16PWB` | 6x `VBUS` (`Pins 11..16`, 3.00 A contact rating > 2.68 A max U2 OCP), 8x `GND` (`Pins 3, 6..10, 17, 18`) |
| `U1` | `USBLC6-2P6` | `C2827693` | Low-C (`0.35 pF`) USB 2.0 ESD Array | `lcsc:SOT-666-6_L1.6-W1.2-P0.50-LS1.6-BL` | Flow-through on `USB_OTG0_DP/DM`; Pin 5 on `USB_ESD_VBUS` decoupled by `100 nF` `C2` to `GND` and biased at `~4.7 V` DC from `VBUS` via `R10` (`1k`) + `D4` (`BAS70L,315`) |
| `U2` | `TPS259470ARPWR` | `C3662799` | 28V, 28.3 mOhm, 5.5A Back-to-Back FET eFuse | `lcsc:VQFN-10_L2.0-W2.0-P0.45-TL` | Series OVP/OCP on `VBUS_IN` -> `VBUS`: `6.54 V` typ (`6.34 V` min) OVP cutoff, `5.94 V` typ (`5.77 V` min) recovery, `2.43 A` typ (`2.19 A..2.68 A`) active OCP, `5.11 V/ms` slew (`C5=4.7nF`) |
| `D1, D2` | `PTVS5V5D1BLYL` | `C553450` | 5.5V Bidirectional Surge TVS (`70 pF`) | `lcsc:SOD-882_L1.0-W0.6-BI-1` | Ground-referenced ESD/surge clamping on `USB_CC1_CONN` and `USB_CC2_CONN` |
| `D3` | `ESTVS2200DRVR` | `C42400188` | 22V Standoff / 28.6V Max Flat-Clamp 2000W Surge TVS | `lcsc:DFN-6_L2.0-W2.0-P0.65-BL-EP1.6` | 22 V standoff (`V_BR = 25.8 V > 20 V` USB-PD and `> 6.75 V` `U2` OVLO; flat `V_CL = 27.6 V` typ / `28.6 V` max at `70 A` 8/20 us `< 28.8 V` `U2` abs max) |
| `D4` | `BAS70L,315` | `C456141` | 70V 70mA Ultra-Low-Leakage Schottky | `lcsc:SOD-882_L1.0-W0.6-BI-1` | Blocking diode from `USB_ESD_BIAS` (`R10.2`) to `USB_ESD_VBUS` (`U1.5`/`C2.1`); biases `U1.5` at `~4.7 V` DC and blocks reverse overvoltage faults |
| `D5` | `PMEG3005EL,315` | `C282565` | 30V 0.5A (3A peak) Low-VF Schottky | `lcsc:SOD-882_L1.0-W0.6-BI-1` | Output freewheeling clamp diode (`Anode` = `GND`, `Cathode` = `VBUS`) adjacent to `U2.6` and `J2.11..16` clamping negative inductive kickback |
| `R1, R2` | `0402WGF6801TCE` | `C25917` | `6.8 kOhm` 1% 50V 62.5mW 0402 | `lcsc:R0402` | Compensated USB-C 5V/3A sink pull-downs (`6.8 kOhm || [10 kOhm R4/R5 + 10 kOhm mainboard R49/R50] = 5.075 kOhm` effective `Rd`) |
| `R3` | `ERJPA3J2R2V` | `C445778` | `2.2 Ohm` 5% **0.33W (1/3W)** Anti-Surge 0603 | `lcsc:R0603` | Pulse-rated (`>= 0.25 W`, AEC-Q200) RC hot-plug damper resistor in series with `C3` on `VBUS_DAMP` |
| `R4, R5` | `0402WGF1002TCE` | `C25744` | `10 kOhm` 1% 50V 62.5mW 0402 | `lcsc:R0402` | Series current-limiting isolation between `USB_CC1_CONN`/`USB_CC2_CONN` and `J2` Pins 4-5 (`USB_CC1`/`USB_CC2`) |
| `R6` | `0402WGF3482TCE` | `C47493` | `34.8 kOhm` 1% 50V 62.5mW 0402 | `lcsc:R0402` | Upper ladder resistor from `VBUS_IN` to `VBUS_UVLO` (`U2.1`) |
| `R7` | `0402WGF5621TCE` | `C25909` | `5.62 kOhm` 1% 50V 62.5mW 0402 | `lcsc:R0402` | Middle ladder resistor from `VBUS_UVLO` (`U2.1`) to `VBUS_OVLO` (`U2.2`, sets `V_UVLO = 4.04 V` typ rising / `3.67 V` falling) |
| `R8` | `0402WGF9091TCE` | `C11549` | `9.09 kOhm` 1% 50V 62.5mW 0402 | `lcsc:R0402` | Lower ladder resistor from `VBUS_OVLO` (`U2.2`) to `GND` (sets `V_OVLO = 6.54 V` typ [`6.32 V..6.75 V`] rising / `5.94 V` typ [`5.77 V` min] falling) |
| `R9` | `0402WGF1371TCE` | `C423239` | `1.37 kOhm` 1% 50V 62.5mW 0402 | `lcsc:R0402` | Current-limit resistor on `U2.9` (`ILM` to `GND`), setting `I_OL = 3334 / 1370 = 2.43 A` typ (`2.19 A` min, `2.68 A` max) active OCP (`> 2.00 A` charger `IINLIM` ceiling, `< 3.00 A` `J2` contact rating) |
| `R10` | `0402WGF1001TCE` | `C11702` | `1.0 kOhm` 1% 50V 62.5mW 0402 | `lcsc:R0402` | Current-limiting bias resistor from `VBUS` to `USB_ESD_BIAS` (`D4` Anode), charging `C2` (`100 nF`) in `t = 0.1 ms` |
| `C1` | `GRM155R61H105KE05D` | `C1518208` | `1 uF` **50V** X5R 0402 | `lcsc:C0402` | Unswitched HF input decoupling on `VBUS_IN` adjacent to `J1` (`50 V` rating, `> 1.75x` `D3` `28.6 V` max clamp and `2.5x` `20 V` PD fault) |
| `C2` | `CC0402KRX7R9BB104` | `C131394` | `100 nF` **50V** X7R 0402 | `lcsc:C0402` | Dedicated local ESD rail-clamp bypass on `USB_ESD_VBUS` right beside `U1.5` and `U1.2` (`50 V` rating, biased at `~4.7 V` DC) |
| `C3` | `CL10A105KB8NNNC` | `C15849` | `1 uF` **50V** X5R 0603 | `lcsc:C0603` | RC snubber capacitor in series with `R3` on `VBUS_DAMP` (`50 V` rating; `C1 + C3 = 2.0 uF <= 2.2 uF` unswitched `cSnkBulk`) |
| `C4` | `CL05A105KA5NQNC` | `C52923` | `1 uF` **25V** X5R 0402 | `lcsc:C0402` | Local output decoupling capacitor (`C_OUT`) on `VBUS` adjacent to `U2.6` and `J2.11..16` |
| `C5` | `0402B472K500NT` | `C1538` | `4.7 nF` **50V** X7R 0402 | `lcsc:C0402` | Soft-start slew-rate capacitor on `U2.7` (`VBUS_DVDT` to `GND`), setting `dV/dt = 5.11 V/ms` (`t_dVdT = 0.98 ms`) |
| `H1, H2` | `MountingHole_Pad` | — | M1.4 Plated Ground Mounting Holes (`1.5 mm` drill) | `lcsc:MountingHole_1.5mm` | Chassis/return ground tie at `(2.5, 6.0)` and `(22.5, 6.0)` |
