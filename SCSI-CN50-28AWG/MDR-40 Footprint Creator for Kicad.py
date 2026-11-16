# run with:  exec(open("C:/Users/roniv/Dev/github/X68000-Compact-External-SCSI-Adapter/MDR-40 Footprint Creator for Kicad.py").read())

import pcbnew

# Create new footprint and attach it to the current board
board = pcbnew.GetBoard()
module = pcbnew.FOOTPRINT(board)
module.SetReference("REF**")
module.SetValue("MDR_40")

# Units conversion: mm → nm
mm_to_nm = lambda mm: int(mm * 1e6)

# Parameters
cols = 10
rows = 4
pin_pitch_x = 1.27  # mm
row_offsets_y = [2.54, 1.27, 0.0, -1.27]  # Row 1 to 4 from top to bottom
pad_diameter = 0.9   # mm
drill_diameter = 0.71  # mm
stagger_offset = 0.635  # mm (half the pitch)

# Generate staggered pad layout
for row in range(rows):
    y_offset = row_offsets_y[row]
    for col in range(cols):
        pad_num = row * cols + col + 1
        x_offset = stagger_offset if row % 2 == 1 else 0.0
        x = mm_to_nm(col * pin_pitch_x + x_offset)
        y = mm_to_nm(y_offset)

        pad = pcbnew.PAD(module)
        pad.SetPadName(str(pad_num))
        pad.SetShape(pcbnew.PAD_SHAPE_CIRCLE)
        pad.SetSize(pcbnew.VECTOR2I(mm_to_nm(pad_diameter), mm_to_nm(pad_diameter)))
        pad.SetDrillSize(pcbnew.VECTOR2I(mm_to_nm(drill_diameter), mm_to_nm(drill_diameter)))
        pad.SetPosition(pcbnew.VECTOR2I(x, y))

        module.Add(pad)

# Add the footprint to the board
board.Add(module)
print("✅ MDR-40 footprint added to board. Use 'Import Footprint from PCB' to save it.")