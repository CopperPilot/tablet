# Mainboard & Sub-board Hardware Documentation (`compact-tablet`)

Generated from `rea/spec.yaml` by rea-hardware (fab rules, stackup, outline at the origin, mounting holes), then completed by the electrical agent. Every placed part carries an `LCSC` field and verified 3D model.

## 1. Inter-Board Cable Pinout (`usbc_fpc_cable`: Mainboard `J6` <-> USB-C Board `J2`, 16-pin 0.5 mm FPC `0.5K-QX-16PWB`)

Straight-through 1:1 pinout (Pin $i$ on `main:J6` connects to Pin $i$ on `usbc_board:J2`) over a **2 oz (`0.070 mm`) heavy-copper Type-B 16-pin 0.5 mm FFC (`FFC-0.5-16P-92MM-TYPE-B`, `0.65 A/pin`)**.
Six contacts are allocated in parallel to `VBUS` (`6 x 0.50 A = 3.00 A` connector contact rating and `6 x 0.65 A = 3.90 A` 2 oz FFC rating, protected by `usbc_board:U2` `TPS259470ARPWR`'s `2.43 A` typ / `2.68 A` max active OCP limit via `R9 = 1.37 kOhm`) and eight contacts (`Pin 3` guard + `Pins 6..10` + `Pins 17, 18` shield tabs) to `GND`:

| Pin (`main:J6` / `usbc_board:J2`) | Net Name | Function / Rating |
|---|---|---|
| 1 | `USB_OTG0_DP` | USB 2.0 OTG D+ (`U1.USB_OTG0_DP` <-> `J6.1`) |
| 2 | `USB_OTG0_DM` | USB 2.0 OTG D- (`U1.USB_OTG0_DM` <-> `J6.2`) |
| 3 | `GND` | Ground guard for USB 2.0 differential pair (`0.5 A`) |
| 4 | `USB_CC1` | USB-C CC1 channel (`5.1 kOhm` Rd pull-down on `usbc_board`) |
| 5 | `USB_CC2` | USB-C CC2 channel (`5.1 kOhm` Rd pull-down on `usbc_board`) |
| 6 | `GND` | Power return ground (`0.5 A`) |
| 7 | `GND` | Power return ground (`0.5 A`) |
| 8 | `GND` | Power return ground (`0.5 A`) |
| 9 | `GND` | Power return ground (`0.5 A`) |
| 10 | `GND` | Power return ground (`0.5 A`; total `6 x 0.5 A = 3.0 A` GND return) |
| 11 | `VBUS` | 5 V USB-C sink input (`0.5 A`) |
| 12 | `VBUS` | 5 V USB-C sink input (`0.5 A`) |
| 13 | `VBUS` | 5 V USB-C sink input (`0.5 A`) |
| 14 | `VBUS` | 5 V USB-C sink input (`0.5 A`) |
| 15 | `VBUS` | 5 V USB-C sink input (`0.5 A`) |
| 16 | `VBUS` | 5 V USB-C sink input (`0.5 A`; total `6 x 0.5 A = 3.0 A` VBUS supply) |
| 17, 18 | `GND` | Mechanical shield / retention tabs |

## 2. Capacitor Voltage Derating Checks (`>= 1.5x` Max Net Voltage)

Every capacitor on `main` (`hardware/compact-tablet.kicad_sch`) is rated at least `1.5x` the maximum voltage on its net:

| Ref | MPN (LCSC) | Value / Package | Net | Max Net Voltage | Required (`1.5x`) | Part Rating | Margin |
|---|---|---|---|---|---|---|---|
| `C1` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VDD_CPU` | `1.15 V` | `1.73 V` | `10 V` | `8.7x` PASS |
| `C2` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VDD_LOGIC` | `0.95 V` | `1.43 V` | `10 V` | `10.5x` PASS |
| `C3` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VDD_GPU` | `0.95 V` | `1.43 V` | `10 V` | `10.5x` PASS |
| `C4` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VCC_DDR` | `1.10 V` | `1.65 V` | `10 V` | `9.1x` PASS |
| `C5` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VCC_3V3` | `3.30 V` | `4.95 V` | `10 V` | `3.0x` PASS |
| `C6` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VSYS` | `4.50 V` | `6.75 V` | `10 V` | `2.2x` PASS |
| `C7, C159` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VBUS` (`J6.11..16` & `U11.1` local input decoupling at `1.04 mm`) | `6.75 V` | `10.13 V` | `25 V` | `3.7x` PASS |
| `C8` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VBAT` | `4.35 V` | `6.53 V` | `25 V` | `5.7x` PASS |
| `C9` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC_1V8` | `1.80 V` | `2.70 V` | `25 V` | `13.9x` PASS |
| `C10` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC_2V8` | `2.80 V` | `4.20 V` | `25 V` | `8.9x` PASS |
| `C11` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC_AF_2V8` | `2.80 V` | `4.20 V` | `25 V` | `8.9x` PASS |
| `C12` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `FLASH_C1/C2` | `5.00 V` | `7.50 V` | `25 V` | `5.0x` PASS |
| `C13` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VDD_CPU` | `1.15 V` | `1.73 V` | `16 V` | `13.9x` PASS |
| `C14` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VDD_LOGIC` | `0.95 V` | `1.43 V` | `16 V` | `16.8x` PASS |
| `C15` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC_DDR` | `1.10 V` | `1.65 V` | `16 V` | `14.5x` PASS |
| `C16` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC_1V8` | `1.80 V` | `2.70 V` | `16 V` | `8.9x` PASS |
| `C17` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC_3V3` | `3.30 V` | `4.95 V` | `16 V` | `4.8x` PASS |
| `C18` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `EMMC_VDDI` | `1.80 V` | `2.70 V` | `16 V` | `8.9x` PASS |
| `C19` | `CL10A105KB8NNNC` (`C15849`) | `1 uF` 0603 X5R | `WLED_A` | `24.0 V` (`38 V` OVP) | `36.0 V` | `50 V` | `2.1x` PASS |
| `C20, C21` | `0402CG180J500NT` (`C1549`) | `18 pF` 0402 C0G | `XTAL_24M_IN/OUT` | `1.80 V` | `2.70 V` | `50 V` | `27.8x` PASS |
| `C22, C23` | `0402CG180J500NT` (`C1549`) | `18 pF` 0402 C0G | `RTC_XIN/XOUT` | `1.80 V` | `2.70 V` | `50 V` | `27.8x` PASS |
| `C24, C25` | `0402CG150J500NT` (`C1548`) | `15 pF` 0402 C0G | `WIFI_XTAL_IN/OUT` | `1.80 V` | `2.70 V` | `50 V` | `27.8x` PASS |
| `C26` | `CL10A106MA8NRNC` (`C96446`) | `10 uF` 0603 X5R | `CHG_PMID` | `5.25 V` | `7.88 V` | `25 V` | `4.8x` PASS |
| `C27` | `CC0402KRX7R9BB473` (`C272875`) | `47 nF` 0402 X7R | `CHG_BTST/CHG_SW` | `6.00 V` | `9.00 V` | `50 V` | `8.3x` PASS |
| `C28` | `CL10A475KO8NNNC` (`C19666`) | `4.7 uF` 0603 X5R | `CHG_REGN` | `6.00 V` | `9.00 V` | `16 V` | `2.7x` PASS |
| `C29` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCCA1V8_CODEC` (`LDO4`) | `1.80 V` | `2.70 V` | `25 V` | `13.9x` PASS |
| `C30` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC3V3_PMU` (`LDO6`) | `3.30 V` | `4.95 V` | `25 V` | `7.6x` PASS |
| `C31` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC1V8_CAM` (`LDO9`) | `1.80 V` | `2.70 V` | `25 V` | `13.9x` PASS |
| `C32` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `PMIC_VREF` | `1.20 V` | `1.80 V` | `25 V` | `20.8x` PASS |
| `C33` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `PMIC_CPP/CPN` | `1.80 V` | `2.70 V` | `25 V` | `13.9x` PASS |
| `C34` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `PMIC_CPVSS` | `1.80 V` | `2.70 V` | `25 V` | `13.9x` PASS |
| `C35` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC1V8_LCD` (`U9.5/20` `VREG/VDD`) | `1.80 V` | `2.70 V` | `16 V` | `8.9x` PASS |
| `C36` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCCA3V3_PHY` (`LDO5` at `U4.29`) | `3.30 V` | `4.95 V` | `25 V` | `7.6x` PASS |
| `C37` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC3V3_TP` (`SWOUT2` at `U15.6` `IN`) | `3.52 V` | `5.28 V` | `25 V` | `7.1x` PASS |
| `C38` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC3V3_LCD` (`U15.1` `OUT` `TLV75533PDRVR` at `J1.35/36`, `J2.6`) | `3.30 V` | `4.95 V` | `25 V` | `7.6x` PASS |
| `C39` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VDDA0V9_IMAGE` (`LDO1`) | `0.90 V` | `1.35 V` | `25 V` | `27.8x` PASS |
| `C40` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VDDA_0V9` (`LDO2`) | `0.90 V` | `1.35 V` | `25 V` | `27.8x` PASS |
| `C41` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VDDA0V9_PMU` (`LDO3`) | `0.90 V` | `1.35 V` | `25 V` | `27.8x` PASS |
| `C42` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `DDR_VREFOUT` (`U1.1H3`) | `0.55 V` | `0.83 V` | `16 V` | `29.1x` PASS |
| `C43` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `AUD_BYPASS` (`U10.2`) | `2.25 V` | `3.38 V` | `25 V` | `11.1x` PASS |
| `C44, C45` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `GND` / `AUD_LINE_N` AC coupling | `2.25 V` | `3.38 V` | `16 V` | `7.1x` PASS |
| `C46` | `CL10A475KO8NNNC` (`C19666`) | `4.7 uF` 0603 X5R | `WIFI_1V25` (`U5` buck) | `1.25 V` | `1.88 V` | `16 V` | `12.8x` PASS |
| `C47` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `WIFI_1V25` (`U5` buck) | `1.25 V` | `1.88 V` | `16 V` | `12.8x` PASS |
| `C48` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `WLED_COMP` (`U6.2`) | `2.50 V` | `3.75 V` | `16 V` | `6.4x` PASS |
| `C49` | `GRM155R61E475ME15D` (`C2858031`) | `4.7 uF` 0402 X5R | `FLASH_LED_A` (`U7.10`) | `5.00 V` | `7.50 V` | `25 V` | `5.0x` PASS |
| `C50, C51` | `CL10A226MQ8NRNC` (`C59461`) | `22 uF` 0603 X5R | `VDD_CPU` (`U8` buck) | `1.15 V` | `1.73 V` | `6.3 V` | `5.5x` PASS |
| `C52` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `PMIC_RESETB` (`U1.AG38`) | `3.30 V` | `4.95 V` | `16 V` | `4.8x` PASS |
| `C53, C54` | `0402B102K500NT` (`C1523`) | `1 nF` 0402 X7R | `KEY_VOL_UP/DN_BTN` (`J8.2/3`) | `1.80 V` | `2.70 V` | `50 V` | `27.8x` PASS |
| `C55` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC_RTC` (`U4.45` `VCC_RTC` via `D41/D42` `BAS70L,315` Schottky OR of `VSYS` and `VCC3V3_SYS`) | `4.50 V` | `6.75 V` | `25 V` | `5.6x` PASS |
| `C132` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `PMIC_PWRON_L` (`U4.52` `PWRON` debounce after `D44` `BAS70L,315`) | `4.50 V` | `6.75 V` | `16 V` | `3.6x` PASS |
| `C152` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC_1V8` (`U22.16` `TMUX1511RSVR` CC SARADC isolation switch supply) | `1.80 V` | `2.70 V` | `16 V` | `8.9x` PASS |
| `C56` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC3V3_PMU` (`U1.1P16`) | `3.30 V` | `4.95 V` | `16 V` | `4.8x` PASS |
| `C57` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VBUS_DET` (`U4.61` / `U1.T38`, `R34=47k` / `R35=30k`) | `2.63 V` | `3.95 V` | `16 V` | `6.1x` PASS |
| `C144` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC_1V8` (`U17.5` `SN74LV1T34DCKR` supply) | `1.80 V` | `2.70 V` | `16 V` | `8.9x` PASS |
| `C145, C146` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCC_3V3` (`U18.5`, `U19.5` `SN74LV1T34DCKR` supply) | `3.30 V` | `4.95 V` | `16 V` | `4.8x` PASS |
| `C147` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC3V3_SYS` (`U4.30` `VCC6` LDO4..6 input supply) | `3.52 V` | `5.28 V` | `25 V` | `7.1x` PASS |
| `C160` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `AUD_TOP_BYPASS` (`U23.2` bypass) | `2.25 V` | `3.38 V` | `25 V` | `11.1x` PASS |
| `C161, C162` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `AUD_LINE_L` / `GND` AC coupling to `U23.3/4` | `2.25 V` | `3.38 V` | `16 V` | `7.1x` PASS |
| `C163, C165, C166, C168, C178..C180, C182` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VSYS` (local input decoupling at `U23, U6, L7, U10, U8, U11, U4, U12`) | `4.50 V` | `6.75 V` | `10 V` | `2.2x` PASS |
| `C164, C169, C175, C176` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VSYS` (local HF bypass at `U23, U10, U6, U7`) | `4.50 V` | `6.75 V` | `16 V` | `3.6x` PASS |
| `C167` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VSYS` (`U7.1` local input decoupling) | `4.50 V` | `6.75 V` | `10 V` | `2.2x` PASS |
| `C170..C173` | `GRM155R61A106ME44D` (`C77000`) | `10 uF` 0402 X5R | `VSYS` (`U4` `VCC1..VCC4` local buck input decoupling) | `4.50 V` | `6.75 V` | `10 V` | `2.2x` PASS |
| `C174, C177, C181` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VSYS` (`U4` `VCC5, VCC7, VCC_SPK_HP` local decoupling) | `4.50 V` | `6.75 V` | `25 V` | `5.6x` PASS |
| `C58` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VSYS` (`U4.54` `VCC9`) | `4.50 V` | `6.75 V` | `10 V` | `2.2x` PASS |
| `C59` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `PMIC_SWOUT1` (`U4.55` `SWOUT1`) | `4.50 V` | `6.75 V` | `25 V` | `5.6x` PASS |
| `C60` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VCC1V8_CAM` (`J3.19/20`, `J4.19/20`) | `1.80 V` | `2.70 V` | `25 V` | `13.9x` PASS |
| `C61` | `CL05B104KO5NNNC` (`C1525`) | `100 nF` 0402 X7R | `VCCA3V3_PHY` (`U1.1H18`, `U1.1J2`) | `3.30 V` | `4.95 V` | `16 V` | `4.8x` PASS |
| `C62` | `CL05A105KA5NQNC` (`C52923`) | `1 uF` 0402 X5R | `VSYS` (`U4.22` `VCC5` LDO1..3 input) | `4.50 V` | `6.75 V` | `25 V` | `5.6x` PASS |
| `C63` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `PMIC_VBUCK4` (`U4` `BUCK4` `0.9 V` `VDD_NPU` output) | `0.95 V` | `1.43 V` | `10 V` | `10.5x` PASS |
| `C64` | `CL10A106KP8NNNC` (`C19702`) | `10 uF` 0603 X5R | `VSYS` (`U12.3` `VIN` input) | `4.50 V` | `6.75 V` | `10 V` | `2.2x` PASS |
| `C65` | `CL10A226MQ8NRNC` (`C59461`) | `22 uF` 0603 X5R | `VCC3V3_SYS` (`U12.6` `3.52 V` buck-boost output) | `3.52 V` | `5.28 V` | `6.3 V` | `1.8x` PASS |
| `C66` | `0402CG180J500NT` (`C1549`) | `18 pF` 0402 C0G | `WIFI_RF_S0` / `WIFI_RF_S0_TERM` DC block | `3.30 V` | `4.95 V` | `50 V` | `15.2x` PASS |
| `C67` | `0402CG180J500NT` (`C1549`) | `18 pF` 0402 C0G | `WIFI_RF_S1` / `WIFI_RF_MATCH` DC block | `3.30 V` | `4.95 V` | `50 V` | `15.2x` PASS |
| `C68, C69` | `GJ81555C1H1R5WB01D` (`C2062813`) | `1.5 pF` 0402 C0G | `WIFI_RF_MATCH` / `WIFI_ANT_RF` pi-match | `3.30 V` | `4.95 V` | `50 V` | `15.2x` PASS |

## 3. Connector Contact Current & Ground Return Verification

| Connector | MPN (LCSC) | Per-Contact Rating | Rail / Signal | Contacts Allocated | Total Capacity | Peak Current | Ground Returns |
|---|---|---|---|---|---|---|---|
| `J1` (40P Display FPC) | `FPC-0.5HF-40PWBH10` (`C5343289`) | `0.5 A` | `VCC3V3_LCD`, `VCC1V8_LCD`, `WLED_A/K` | `2` (`VCC3V3_LCD`), `2` (`VCC1V8_LCD`), `1` (`WLED_A/K`) | `1.0 A` / `1.0 A` / `0.5 A` | `0.25 A` / `0.10 A` / `0.06 A` | `13` interleaved `GND` pins + `2` shield tabs flanking all 10 MIPI-DSI pairs |
| `J2` (10P Touch FPC) | `0.5K-QX-10PWB` (`C2919478`) | `0.5 A` | `VCC3V3_LCD`, `VCC1V8_LCD` | `1` (`VCC3V3_LCD`), `2` (`VCC1V8_LCD`) | `0.5 A` / `1.0 A` | `0.02 A` / `0.01 A` | `Pins 1, 9` `GND` + `2` shield tabs |
| `J3` (30P Rear Cam FPC) | `0.5K-QX-30PWB` (`C2919487`) | `0.5 A` | `VCC1V8_CAM`, `VCC_2V8`, `VCC_AF_2V8` | `2` per rail | `1.0 A` per rail | `0.15 A` | `13` interleaved `GND` pins + `2` shield tabs flanking MIPI-CSI pairs |
| `J4` (24P Front Cam FPC) | `FPC-0.5HF-24PWBH10` (`C5343283`) | `0.5 A` | `VCC1V8_CAM`, `VCC_2V8` | `2` per rail | `1.0 A` per rail | `0.12 A` | `9` interleaved `GND` pins + `2` shield tabs flanking MIPI-CSI pairs |
| `J5` (Battery Connector) | `DF58-4P-1.2V(21)` (`C20723302`) | `3.0 A` | `VBAT`, `BAT_NTC`, `BAT_SNSN` | `1` (`Pin 1` `VBAT`), `1` (`Pin 2` `BAT_NTC`), `2` (`Pins 3, 4` `BAT_SNSN` via `10 mOhm` `R13`) | `3.0 A` (`VBAT`) / `6.0 A` (`BAT_SNSN`) | `2.0–2.5 A` | `Pins 3, 4` (`BAT_SNSN` through `10 mOhm` `R13` to `GND`, mating 1-to-1 with 3-wire `V+/NTC/GND` harness on `Pins 1..3`) + `2` shield tabs (`GND`) |
| `J6` (16P USB-C FPC) | `0.5K-QX-16PWB` (`C2919481`) | `0.5 A` | `VBUS` (`5 V`) | `6` (`Pins 11..16`) | `3.0 A` | `3.0 A` | `6` `GND` pins (`Pin 3` guard + `Pins 6..10`) + `2` shield tabs |
| `J7`, `J9` (Speaker FPCs) | `0.5K-QX-4PWB` (`C2919475`) | `0.5 A` | `SPK_TOP_P/N`, `SPK_BOT_P/N` | `2` per phase (`Pins 1,2` & `3,4`) | `1.0 A` | `0.65 A` | `2` shield tabs (`GND`) |
| `J8` (Button Flex FPC) | `0.5K-QX-4PWB` (`C2919475`) | `0.5 A` | `PWRON_L`, `KEY_VOL_UP/DN` | `1` per switch | `0.5 A` | `< 1 mA` | `Pin 4` `GND` return + `2` shield tabs |

## 4. Clocking, Charger, Fuel Gauge & PMIC Power-Tree Verification

- **Pierce Crystal Oscillators (`Y1`, `Y2`, `Y3`)**:
  - `Y1` (`X322524MOB4SI`, `24 MHz`, $C_L = 12\text{ pF}$) connects exclusively to `U1.AD37/AD38` (`XIN24M/XOUT24M`) with matched `18 pF` 50V C0G load capacitors (`C20`, `C21`) and a `1 MOhm` parallel feedback resistor (`R7`).
  - `Y2` (`Q13FC13500004`, `32.768 kHz`, $C_L = 12.5\text{ pF}$) connects to `U4.50/51` (`XIN/XOUT`) with matched `18 pF` 50V C0G load capacitors (`C22`, `C23`).
  - `Y3` (`X322524MOB4SI`, `24 MHz`, $C_L = 12\text{ pF}$) provides a dedicated local crystal for Wi-Fi/BT IC `U5.15/16` (`XI/XO`) on `WIFI_XTAL_IN/OUT` with matched `18 pF` load capacitors (`C24`, `C25`), while `U4.68` (`CLK32K`, `1.8 V` `VCC_1P8D` domain) drives `CLK_32K` exclusively to 1.8 V clock-input pins: RK3566 `U1.A37` (`GPIO2_C0_d / CLK32K_IN1`, `1.8 V` `VCCIO3` domain) and RTL8723DS-CG `U5.20` (`GPIO6 / SUSCLK_IN`, `1.8 V` `VDD_IO` domain), with `U1.1T20` (`GPIO0_B0_u`, `3.3 V` `PMUIO1` domain) and `U1.1V20` (`GPIO0_C7_d`) left unconnected, `U5.21` (`GPIO0 / DWH(WL)` / `ICFG0 = 1`) routed on `WIFI_HOST_WAKE` to `U1.B34` (`GPIO2_B2_u` in `1.8 V` `VCCIO3` domain, leaving `U5.44` `GPIO8/WL_LED` and `U5.23` `GPIO2/ICFG2 = 0` unconnected), `U5.27` (`UART_OUT/ICFG1` on `BT_UART_RX`) and `U5.24` (`GPIO3/UART_RTS/ICFG3` on `BT_UART_RTS`) pulled down to `GND` via `4.7 kOhm` 1% resistors `R82` and `R83` (`0402WGF4701TCE`, `C25900`) so `ICFG[3:0] = 0001` reliably latches the `24 MHz` reference clock at reset/enable deassertion, `U5.18` (`GPIO13 / BT_WAKE_HOST`, `1.8 V` `VDD_IO` domain) routed on `BT_HOST_WAKE` to `U1.D38` (`GPIO2_B1_u` in `1.8 V` `VCCIO3` domain, leaving `U5.42` `GPIO7/BT_LED` unconnected), and `U5.22` (`SPS_LDO_SEL/GPIO1`) strapped low via a dedicated `10 kOhm` pull-down resistor `R42` (`0402WGF1002TCE`, `C25744`) to `GND` so `U5` deterministically latches internal switching buck mode (`SPS`) for `L9` at power-on.
- **Battery Charger (`U11`, `BQ25895RTWR`), VBUS Surge Protection (`D13`, `SMF7.5A`) & Fuel Gauge (`U4`, `RK809-5`)**:
  - `U11.2` (`D+`) and `U11.3` (`D-`) are left unconnected so `BQ25895RTWR` defaults to a safe `500 mA` (`USB500`) input current limit at VBUS insertion until software reads `USB_CC1`/`USB_CC2` on `U1.1B18/1A19` (`SARADC_VIN2/3`, isolated when `VCC_1V8 = 0 V` by powered-off-protected CMOS switch `U22` `TMUX1511RSVR` `C2673275`) and updates `IINLIM` over `I2C0` capped $\le 2.00\text{ A}$; `U11.10` (`ILIM`) connects via `R8` (`196 Ohm` 1%, `0402WGF1960TCE`, `C270631`) to `GND`, setting hardware $I_{\text{INMAX}} = 355 / 196 = 1.81\text{ A}$ typ ($1.64\text{ A}$ min to $1.96\text{ A}$ max, strictly below the `2.19 A` min OCP trip threshold of upstream eFuse `usbc_board:U2` `TPS259470ARPWR` and the `3.00 A` contact rating of `J6.11..16`); `U11.1` (`VBUS`) is locally decoupled to `PGND` (`Pins 17, 18, 25`) by dedicated `1 uF` 25V 0402 ceramic capacitor `C159` (`CL05A105KA5NQNC`, `C52923`) placed at `(14.55, 96.27) mm` within `1.04 mm` (`< 1.5 mm`) of `U11.1`, while `J6.11..16` (`VBUS`) is protected by unidirectional `7.5 V` standoff surge TVS diode `D13` (`SMF7.5A`, `C123796`, $V_{\text{RWM}} = 7.5\text{ V}$, $V_{\text{BR}} = 8.33\text{--}9.21\text{ V} > 6.75\text{ V}$ max eFuse OVP trip, $V_{\text{CL}} = 12.9\text{ V}$ max at $15.5\text{ A} < 14\text{ V}$ operating / $22\text{ V}$ abs max of `U11` `VBUS`); `U11.23` (`PMID`) is isolated on `CHG_PMID` with a `10 uF` 25V 0603 bulk capacitor (`C26`); `U11.21` (`BTST`) connects via a `47 nF` 50V X7R bootstrap capacitor (`C27`) to `CHG_SW`; `U11.22` (`REGN`) is decoupled on `CHG_REGN` by `C28` (`4.7 uF` 16V 0603) and biases `BAT_NTC` (`U11.11` `TS` and `J5.2`) via `R9` (`5.1 kOhm` 1% upper `RT1`) and `R10` (`30 kOhm` 1% lower `RT2`); open-drain `INT` (`U11.7`, `CHG_INT_L`) and `STAT` (`U11.4`, `CHG_STAT_L`) are separated with dedicated `10 kOhm` pull-ups (`R11`, `R12`) to `VCC_1V8`.
  - `U4.62` (`SNSP`) and `U4.63` (`SNSN`) sense battery current across a `10 mOhm` 1% 0603 low-side current-sense resistor (`R13`) between `J5.3/J5.4` (`BAT_SNSN`) and `GND`, while `J5.1` (`VBAT`, `3.0 A` contact rating), `J5.2` (`BAT_NTC`), and `J5.3` (`BAT_SNSN`, with `J5.4` tied in parallel) mate 1-to-1 with the 3-wire (`V+`, `NTC`, `GND`) battery harness.
- **PMIC (`U4`, `RK809-5`), Dedicated `3.3 V` System Buck (`U12`, `TLV62569ADRLR`) & Touch (`U9`, `MPR121QR2`) Rail Isolation**:
  - `U4.45` (`VCC_RTC`, decoupled by `1 uF` `C55`) and `U4.22` (`VCC5`, input supply to Sequence-1 `0.9 V` rails `LDO1` `VDDA0V9_IMAGE`, `LDO2` `VDDA_0V9`, and `LDO3` `VDDA0V9_PMU`, decoupled by local `1 uF` `C62`) are connected directly to `VSYS` (`2.7 V–5.5 V`), ensuring `LDO1–LDO3` ramp immediately in Sequence 1 (`U1.1N16` `PMU_VDD_LOGIC_0V9` and `U1.1P17` `PMUPLL_AVDD_0V9` both powered from `VDDA0V9_PMU`), while a dedicated `2 A` synchronous buck regulator `U12` (`TLV62569ADRLR`, `C398367`, SOT-563, input `C64 = 10 uF` on `VSYS`, enable `U12.5` `EN` driven by PMIC-sequenced `VCC_1V8` so `VCC_3V3` ramps after `VDD_LOGIC`/`VCC_1V8` and turns off in standby/off mode, inductor `L10 = 1.0 uH` `WPN201610U1R0MT` `C97016`, feedback divider `R39 = 45.3 kOhm` `C26980` / `R40 = 10 kOhm` `C25744` setting $V_{\text{OUT}} = 0.6\text{ V} \times (1 + 45.3/10) = 3.318\text{ V}$, output `C65 = 10 uF` + `C5 = 10 uF`) supplies `/VCC_3V3` and `U4.57` (`VCC8`), and `U4` `BUCK4` (`L4.2` / `U4.64` `FB4`, `0.9 V` OTP default on `PMIC_VBUCK4` with `10 uF` `C63`) supplies RK3566 `VDD_NPU` (`U1.1G15, 1H14, 1H15, 1J14, 1J15`).
  - `U4.31` (`LDO6`, input `U4.30` `VCC6` = `VCC3V3_SYS` regulated `3.52 V` nominal [`3.43 V..3.62 V` worst-case] from Slot-1 buck-boost `U12` `TPS63802DLAR` via `R39 = 60.4 kOhm` 1% `0402WGF6042TCE` `C25911` and `R40 = 10 kOhm` 1% `C25744`, providing `>= 220 mV` nominal [`>= 126 mV` worst-case] hardware dropout headroom for both `LDO5` `VCCA3V3_PHY` and `LDO6` `VCC3V3_PMU` at their `3.30 V` OTP default during cold boot and USB Maskrom recovery, and `420–520 mV` headroom when reprogrammed over `I2C0` to `3.00–3.10 V`, while staying within `3.60–3.63 V` operating limits) is configured as the always-on `VCC3V3_PMU` rail (decoupled by `C30` `1 uF` at `U4.31` and `C56` `100 nF` at `U1.1P16`), powering RK3566 `U1.1P16` (`PMUIO1` `3.3 V` domain) and the `10 kOhm` pull-up resistors `R29` (`PMIC_RESETB` on `U1.AG38` `nPOR_u`) and `R4` (`PMIC_INT_L` on `U1.1R19` `GPIO0_A3_u`), while `U1.1P19` (`GPIO0_A2_d`, `3.3 V` `PMUIO1` output on `PMIC_SLEEP_3V3`) drives `1.8 V`-domain `U4.49` (`SLEEP`, `VCC_1P8D = 1.8 V`) and `U8.A1` (`VSEL`) on `PMIC_SLEEP` (`1.80 V` nominal) through a `10 kOhm` (`R43`, `0402WGF1002TCE`, `C25744`) / `12 kOhm` (`R44`, `0402WGF1202TCE`, `C25752`) resistive voltage divider.
  - Every `U4` Buck, LDO, and load-switch output (`Buck1..5`, `LDO1..9`, `SWOUT1..2`) is isolated on its own dedicated net with $\ge 1\ \mu\text{F}$ output decoupling (`C29..C31`, `C36..C41`, `C10`, `C11`, `C60`, `C61`): `U4.26` (`VBUCK3`, `VCC_DDR`) is regulated to `1.100 V` via an external 1% `3:8` feedback divider (`R36 = 75 kOhm` from `VCC_DDR` to `U4.27` `FB3` on `PMIC_FB3`, `R37 = 200 kOhm` from `PMIC_FB3` to `GND`); `U4.6` (`LDO9`, `VCC1V8_CAM` with `C31` `1 uF` and `C60` `1 uF`) supplies `1.8 V` `DOVDD` to rear/front cameras `J3.19/20` and `J4.19/20` (while on-module LDOs generate sensor `1.2V/1.5V` `DVDD` core rails); `U4.29` (`LDO5`, `VCCA3V3_PHY` with `C36` `1 uF` and `C61` `100 nF`) supplies `3.3 V` to RK3566 `U1.1H18` (`USB_AVDD1_3V3`) and `U1.1J2` (`USB_AVDD2_3V3`); `U4.46` (`VREF`) is decoupled solely by `C32` (`1 uF`) on `PMIC_VREF`; `U4.37/36` (`CPP/CPN`) and `U4.35` (`VCC_CPVSS`) use dedicated `1 uF` flying/hold capacitors (`C33`, `C34`); `U4.60` (`EXT_EN`) drives `U8.A2` (`EN`) on `PMIC_EXT_EN`; and `U9` (`MPR121QR2`) operates in `1.8 V` mode inside the switched `VCC1V8_LCD` domain (`U14` `TPS22919DCKR` gated by `LCD_PWR_EN` `U1.1T18` `GPIO0_C6_d` with `10 kOhm` pull-down `R57`) with both `U9.20` (`VDD`) and `U9.5` (`VREG`, decoupled by `100 nF` `C35`) connected to `VCC1V8_LCD` and `U9.1` (`~IRQ`) routed on dedicated `TP_SAR_INT_L` to `U1.1U19` (`GPIO0_C5_d`) with a `10 kOhm` pull-up resistor `R38` to `VCC1V8_LCD`.

## 5. Peripheral Interfaces, Secondary Power Converters & Boot/eMMC Signal Integrity

- **Capacitive Touch (`J2`, `U9`) & `I2C1`/`I2C2` Pull-Ups**:
  - `J2` (`0.5K-QX-10PWB`, 10-pin 0.5 mm FPC) routes `I2C1_SCL` (`Pin 2`), `I2C1_SDA` (`Pin 3`), `TP_INT_L` (`Pin 4` -> `U1.1U20` `GPIO0_B5_u` with `10 kOhm` pull-up `R5` to `VCC1V8_LCD`), `TP_RST_L` (`Pin 5` -> `U1.1V20` `GPIO0_C7_d` default pull-down in `1.8 V` `PMUIO2` domain with a dedicated `10 kOhm` pull-down resistor `R61` `0402WGF1002TCE` `C25744` to `GND`), `VCC3V3_LCD` (`Pin 6`, gated by load switch `U15` `TPS22919DCKR`), `VCC1V8_LCD` (`Pins 7, 8`, gated by load switch `U14` `TPS22919DCKR`), and `GND` (`Pins 1, 9, 11, 12`) directly to the 8.4-inch COF (Chip-On-Flex) X/Y matrix capacitive touch panel (`TP-084-GG-10P`), while `U9` (`MPR121QR2`, I2C address `0x5A` with `ADDR` grounded) operates in `1.8 V` mode (`U9.20` `VDD` and `U9.5` `VREG` tied to `VCC1V8_LCD` with `100 nF` bypass capacitor `C35` so $V_{\text{IH(min)}} = 0.7 \times 1.8\text{ V} = 1.26\text{ V} < 1.8\text{ V}$) as an auxiliary capacitive SAR/grip sensor on `TP_ELE0` (`J2.10`) with a `75 kOhm` 1% bias reference resistor (`R14`, `0402WGF7502TCE`, `C25798`) from `U9.7` (`REXT`) to `GND` and a dedicated interrupt line `TP_SAR_INT_L` (`U9.1` `~IRQ` -> `U1.1U19` `GPIO0_C5_d`, pulled up via `10 kOhm` `R38` to `VCC1V8_LCD`).
  - Touch bus `I2C1` (`R15`, `R16`) has `2.2 kOhm` 1% pull-up resistors (`0402WGF2201TCE`, `C25879`) to switched `VCC1V8_LCD` (preventing back-powering of `J2` and `U9` when `LCD_PWR_EN` is low), and camera bus `I2C2` (`R17`, `R18`) has `2.2 kOhm` 1% pull-up resistors (`0402WGF2201TCE`, `C25879`) to switched `VCC1V8_CAM`.
- **LPDDR4X ZQ Calibration (`U1`, `U2`) & `DDR_VREFOUT`**:
  - `U1.1F3` (`DDR_RZQ` -> `R1`), `U2.A5` (`ZQ0` -> `R19` on `LPDDR4_ZQ0`), and `U2.A8` (`ZQ1` -> `R20` on `LPDDR4_ZQ1`) each have an independent `240 Ohm` 1% 0402 resistor (`0402WGF2400TCE`, `C25094`) to `GND` per JEDEC JESD209-4, and `U1.1H3` (`DDR_VREFOUT`) is isolated from `VCC_DDR` and decoupled by `C42` (`100 nF` 16V 0402) to `GND`.
- **Audio Codec/Amp (`U4`, `U10`), PDM Microphone (`MK1`), and 4-Wire Bluetooth HCI UART (`U1`, `U5`)**:
  - `U10` (`NS4150B`) `Pin 2` (`Bypass`) is decoupled to `GND` via `C43` (`1 uF` 25V 0402) on `AUD_BYPASS`, and `U4.39/41` (`HPL_OUT/HPR_OUT`) drive `U10.3/4` (`INP/INN`) through AC-coupling capacitors `C44`, `C45` (`100 nF`) in series with `30 kOhm` input resistors `R21`, `R22`.
  - Rear PDM MEMS microphone `MK1.5` (`DATA`) is routed on a dedicated `PDM_SDI` net to `U1.B24` (`GPIO1_A5_d` / `PDM_SDI0`), separated from `I2S1_SDI0` (`U4.18` <-> `U1.1A13`).
  - 4-wire Bluetooth HCI UART between `U1` (`UART1_M0`) and `U5` (`RTL8723DS-CG`) connects `U1.F38` (`UART1_TX_M0`) -> `U5.25` (`UART_IN`), `U5.27` (`UART_OUT`) -> `U1.1C20` (`UART1_RX_M0`), `U1.F37` (`UART1_RTSN_M0`) -> `U5.26` (`UART_CTS`), and `U5.24` (`GPIO3/UART_RTS`) -> `U1.G37` (`UART1_CTSN_M0`).
- **Secondary Power Regulators (`U5`, `U6`, `U7`, `U12`), RF Front-End Matching (`U5`, `ANT1`) & `VDD_CPU` Buck (`U8`, `L6`)**:
  - `U5` (`RTL8723DS-CG`) internal 1.25 V buck switcher pin `U5.36` (`SW_LX`, net `WIFI_SW_LX`) drives `WIFI_1V25` (`U5.40`, `U5.3/5/8/9/13`) through a `2.2 uH` power inductor `L9` (`WPN201610H2R2MT`, `C97005`) decoupled by `C46` (`4.7 uF` 16V 0603) and `C47` (`100 nF` 16V 0402); unused RF port `U5.48` (`RFIO_BTG_S0`, net `WIFI_RF_S0`) is DC-blocked by `C66` (`18 pF` 50V C0G, `C1549`) onto `WIFI_RF_S0_TERM` and terminated to `GND` via `R41` (`49.9 Ohm` 1%, `0402WGF499JTCE`, `C25120`), while active RF port `U5.11` (`RFIO_BTG_S1`, net `WIFI_RF_S1`) feeds `ANT1.1` (`WIFI_ANT_RF`) through a series DC-blocking capacitor `C67` (`18 pF` 50V C0G, `C1549` -> `WIFI_RF_MATCH`) and a 3-element $\pi$-matching network (`C68 = 1.5 pF` C0G `C2062813` shunt to `GND`, `L11 = 2.2 nH` `LQG15HN2N2S02D` `C76919` series inductor, and `C69 = 1.5 pF` C0G `C2062813` shunt to `GND`).
  - `U6` (`TPS61165DRVR`) compensation pin `U6.2` (`COMP`) is decoupled to `GND` by `C48` (`100 nF` 16V 0402) on `WLED_COMP`, `R6` is set to `3.3 Ohm` 1% (`0402WGF330KTCE`, `C270612`) for $I_{\text{LED}} = 200\text{ mV} / 3.3\ \Omega = 60.6\text{ mA}$, and `D2` is upgraded to a `60 V` `1 A` Schottky rectifier `B16WS` (`C364278`, SOD-323) for 50% margin above the `38 V` (`40 V` max) open-LED OVP threshold.
  - `U7` (`AW3641EDNR`) 1x/2x regulated charge-pump flash driver uses `10 uF` 10V 0603 local input capacitor `C167` (`CL10A106KP8NNNC`, `C19702`) + `100 nF` HF bypass `C176` (`C1525`) on `U7.1` (`VIN`), `1 uF` flying capacitor `C12` (`C52923`) across `C1/C2`, `4.7 uF` 25V 0402 output capacitor `C49` (`GRM155R61E475ME15D`, `C2858031`) on `FLASH_LED_A` (`U7.10` `VOUT`), `110 kOhm` 1% programming resistor `R23` (`0402WGF1103TCE`, `C25745`) on `U7.6` (`RSET`, setting $V_{\text{FB(FLASH)}} = (1.26\text{ V} / 110\text{ k}\Omega) \times 10.2\text{ k}\Omega = 116.84\text{ mV}$ vs $V_{\text{FB(TORCH)}} = 47\text{ mV}$), and `0.22 Ohm` 1% low-side current-sense resistor `R24` (`0402WGF220LTCE`, `C270628`) from `D1.2`/`U7.7` (`FLASH_LED_K`/`FB`) to `GND`, regulating `D1` (OSRAM `KW CELNM3.TK-S4S9-4L07M0-2686`, `C17383700`, `1.0 A` continuous / `1.5 A` pulse ceramic camera flash LED with thermal pad Pin 3 on `GND`) at $I_{\text{FLASH}} = 116.84\text{ mV} / 0.22\ \Omega = 531\text{ mA}$ and $I_{\text{TORCH}} = 47\text{ mV} / 0.22\ \Omega = 214\text{ mA}$.
  - `L6` on `U8` (`RK860-0`, `4.0 A` peak `VDD_CPU`) is upgraded to a `0.47 uH` 2520 power inductor `WPN252012ER47MT` (`C317620`, $I_{\text{sat}} = 7.0\text{ A}$, $I_{\text{rms}} = 4.1\text{ A}$), and `VDD_CPU` bulk capacitance is increased to `54.1 uF` (`C1` `10 uF` + `C50` `22 uF` + `C51` `22 uF` + `C13` `100 nF`).
- **eMMC 5.1 (`U3`), Dual Camera (`J3`, `J4`), Maskrom Strap (`TP3`), and `PMIC_RESETB` Conditioning**:
  - `U3` (`FEMDNN064G-C9A61`, HS400 eMMC 5.1) connects to RK3566 `U1`'s dedicated `GPIO1_B4..GPIO1_C7` eMMC controller balls (`VCCIO2` at `1.8 V`): `EMMC_D0..D7` on `U1.A32`, `B27`, `B32`, `B29`, `B33`, `A30`, `B30`, `A33`; `EMMC_CMD` on `U1.A27` (`GPIO1_C4_u`, pulled up via `10 kOhm` `R27` to `VCC_1V8`); `EMMC_CLKOUT` on `U1.A29` (`GPIO1_C5_d` = `EMMC_CLK_SOC` -> `33 Ohm` `R25` -> `EMMC_CLK`); `EMMC_DATA_STROBE` on `U1.1A16` (`GPIO1_C6_d` = `EMMC_DS`, pulled down via `10 kOhm` `R28` to `GND`); and `EMMC_RSTn` on `U1.1B16` (`GPIO1_C7_d` = `EMMC_RSTN`).
  - Dual camera control/clocks (`J3`, `J4`) connect to RK3566 `U1`'s `GPIO4` domain (`VCCIO6` at `1.8 V`): `I2C2_SCL` on `U1.AD1` (`GPIO4_B5_d` = `I2C2_SCL_M1`), `I2C2_SDA` on `U1.AF1` (`GPIO4_B4_d` = `I2C2_SDA_M1`), `CAM_MCLK0` on `U1.1N1` (`GPIO4_A7_d` = `CAM_CLKOUT0`), `CAM_MCLK1` on `U1.1L2` (`GPIO4_B0_d` = `CAM_CLKOUT1`), `CAM_REAR_RST_L` on `U1.AB1` (`GPIO4_C1_d`), `CAM_REAR_PDN` on `U1.AB2` (`GPIO4_C0_d`), `CAM_FRONT_RST_L` on `U1.AG2` (`GPIO4_B1_d`), and `CAM_FRONT_PDN` on `U1.AH2` (`GPIO4_A6_d`).
  - `R25` (`33 Ohm` 1%, `0402WGF330JTCE`, `C25105`) provides series source damping on `EMMC_CLK` (`U1.A29` `EMMC_CLK_SOC` -> `EMMC_CLK`), and `TP3` (`TP_MASKROM`) is relocated to `(7.5, 59.5) mm` adjacent to `U3.M6` behind a `10 Ohm` 1% series isolation resistor `R26` (`0402WGF100JTCE`, `C25077`) on `EMMC_MASKROM_TP`.
  - `R29` (`10 kOhm` pull-up to `3.3 V` `VCC3V3_PMU`) + `C52` (`100 nF` to `GND`) filter `PMIC_RESETB` adjacent to `U1.AG38` (`nPOR_u`), and `R4` (`10 kOhm` pull-up to `VCC3V3_PMU`) biases `PMIC_INT_L` (`U1.1R19` `GPIO0_A3_u`).
