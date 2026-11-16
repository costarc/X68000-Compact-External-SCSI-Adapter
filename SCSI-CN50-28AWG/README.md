# X68000 Compact external SCSI adapter - 28 AWG cable board

A board for bringing the external half-pitch (MDR 50) SCSI port of the X68000 Compact out to a standard 2x25, 2.54 mm SCSI header. Instead of a half-pitch connector on the board, **J1 is a block of 2x25 solder holes** for the wires of a 28 AWG cable that ends in a half-pitch 50-pin plug (for example a "CN50P" SCSI cable with soldered MDR plug and bare wires at the other end). The board re-maps the half-pitch pin numbers to ribbon-header numbering.

- **J1** - 2x25 solder holes, one hole per half-pitch pin. Hole numbers are the half-pitch pin numbers (see the table).
- **J2** - 2x25 2.54 mm socket (`PinSocket_2x25_P2.54mm_Horizontal`), standard SCSI-1 ribbon numbering, towards the device.

## How to use

1. Take a cable with a half-pitch 50-pin plug and strip the free end. Identify the wire of each plug pin (use a meter or the cable's colour chart; do not assume the wire order).
2. Solder the wire of plug pin *n* into J1 hole *n*. Pin 13 is not connected on the machine and its hole is also left open. Ground wires (pins 1-12, 14-25, 35, 36, 37, 39, 40, 42) must all be soldered.
3. Power the X68000 off and plug the cable into its external SCSI port.
4. Attach the device to J2 with a 50-pin ribbon cable, red stripe on pin 1.
5. Set up the SCSI bus as usual: unique IDs and termination at both ends. TERMPWR (half-pitch pin 38) is joined to J2 pin 26, so check whether your device expects, supplies or must not receive terminator power.
6. Power on the device first, then the X68000.

Check the links with a meter before first use. This board has not been tested on real hardware.

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

On J1 the solder holes are paired in rows: 1-2, 3-4, ... 49-50 (odd numbers in one column, even in the other); the hole number is the half-pitch pin number. On J2, header pin 1 is the red-stripe side of the ribbon cable.

## Revisions

Rev 2.0 (pin 13 NC)
- J1 pin 13 is no connect (it was tied to ground); J2 unchanged.
- Gerbers: `Fabrication/X68000-Compact-External-SCSI-Adapter Rev 2.0 (pin 13 NC).zip` (earlier: `Rev 2.0.zip`).

Rev 2.0
- Changes to pinout in the X68000 side, as the 2.0mm pin header seem to use a non standard pinout

Rev 1.0
- Based on SCSI pinouts

## Related board

`MDR-50_Male-Male` does the same job with a half-pitch connector on the board instead of solder pads. Use one board or the other.
