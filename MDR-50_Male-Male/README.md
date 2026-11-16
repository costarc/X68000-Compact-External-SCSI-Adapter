# X68000 Compact external SCSI adapter - MDR-50 Male-Male board

A small board that brings the external half-pitch (MDR 50) SCSI connector of the X68000 Compact out to a standard 2x25, 2.54 mm SCSI header, so a flat ribbon cable or a SCSI device/emulator with a 50-pin header can be attached. It is not a straight pass-through: the half-pitch connector and the ribbon header number their pins differently (see below), and the board does the re-mapping.

- **J1** - 50-position half-pitch connector, towards the X68000 Compact external SCSI port.
- **J2** - 2x25 2.54 mm socket (`PinSocket_2x25_P2.54mm_Horizontal`), standard SCSI-1 ribbon numbering, towards the device.
- Board size 66.8 mm x 20.5 mm, two layers, GND pour on both layers.

## How to use

1. Power the X68000 off.
2. Connect J1 to the machine's external SCSI port (half-pitch).
3. Connect J2 to the device with a 50-pin ribbon cable, red stripe on pin 1. The device must have the usual SCSI-1 50-pin pinout.
4. Set up the SCSI bus as usual: unique IDs, and termination at both ends of the bus. J1 pin 38 (TERMPWR from the machine) is joined to J2 pin 26, so check whether your device expects, supplies or must not receive terminator power before powering it.
5. Power on the device first, then the X68000.

Before first use, check each link in the table below with a meter (continuity from J1 to J2, and no continuity between the data lines and GND or TERMPWR). This revision has not been tested on real hardware.

## Pin mapping

Machine side, half-pitch 50-pin connector (X68000 Book, Appendix D.10) → header side, 2x25 2.54 mm (standard SCSI-1 ribbon numbering):

| Signal | Half-pitch pin | Header pin |
|---|---|---|
| DB0 … DB7 | 26 … 33 | 2, 4, 6, 8, 10, 12, 14, 16 |
| PARITY (DBP) | 34 | 18 |
| TERMPWR (TMPWR) | 38 | 26 |
| /ATN | 41 | 32 |
| /BSY | 43 | 36 |
| /ACK | 44 | 38 |
| /RST | 45 | 40 |
| /MSG | 46 | 42 |
| /SEL | 47 | 44 |
| /C/D | 48 | 46 |
| /REQ | 49 | 48 |
| /I/O | 50 | 50 |
| GND | 1-12, 14-25, 35, 36, 37, 39, 40, 42 | all other pins except 25 |
| not connected | 13 | 25 |

Half-pitch pads 1-25 are one side of the connector and 26-50 the other, with pin 26 beside pin 1. Header pin 1 is the red-stripe side of the ribbon cable.

## Revisions

Rev 2.0 (D.10 pinout)
- J1 is rewired to the half-pitch pinout of the X68000 Book, Appendix D.10. J2 is unchanged.
- Rev 1.0 joined every J1 pad n to J2 pin n, i.e. it numbered J1 as a ribbon header. On the half-pitch connector that put machine grounds on the device's data lines, machine DB0 on device TERMPWR and machine TERMPWR on device /ACK, and held /RST low. **Do not use Rev 1.0 boards** (`Fabrication/... MDR Rev 1.0.zip`).
- The board was re-routed. Gerbers: `Fabrication/X68000-Compact-External-SCSI-Adapter MDR Rev 2.0 (D.10 pinout).zip`.

Rev 1.0
- Based on SCSI pinouts

Also in the original notes: "Changes to pinout in the X68000 side, as the 2.0mm pin header seem to use a non standard pinout".

## Related board

`SCSI-CN50-28AWG` does the same job with solder pads instead of a connector: you solder the wires of a half-pitch plug cable to it. Use one board or the other.
