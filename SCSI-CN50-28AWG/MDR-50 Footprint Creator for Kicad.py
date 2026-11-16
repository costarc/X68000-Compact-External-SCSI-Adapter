# run with:  exec(open("C:/Users/roniv/Dev/github/X68000-Compact-External-SCSI-Adapter/MDR-50 Footprint Creator for Kicad.py").read())

import pcbnew

board = pcbnew.GetBoard()
module = pcbnew.FOOTPRINT(board)
module.SetReference("REF**")
module.SetValue("3M_10250_5212PL")

mm_to_nm = lambda mm: int(mm * 1e6)

# Parameters
cols = 13
rows = 4
pin_pitch_x = 1.27
row_offsets_y = [2.54, 1.27, 0.0, -1.27]  # Top to bottom
pad_diameter = 0.9
drill_diameter = 0.7
stagger_offset = 0.635  # Half pitch

# Generate staggered pin layout
pad_count = 0
for row in range(rows):
    y = mm_to_nm(row_offsets_y[row])
    for col in range(cols):
        if pad_count >= 50:
            break
        x_offset = stagger_offset if row % 2 == 1 else 0.0
        x = mm_to_nm(col * pin_pitch_x + x_offset)

        pad = pcbnew.PAD(module)
        pad.SetPadName(str(pad_count + 1))
        pad.SetShape(pcbnew.PAD_SHAPE_CIRCLE)
        pad.SetSize(pcbnew.VECTOR2I(mm_to_nm(pad_diameter), mm_to_nm(pad_diameter)))
        pad.SetDrillSize(pcbnew.VECTOR2I(mm_to_nm(drill_diameter), mm_to_nm(drill_diameter)))
        pad.SetPosition(pcbnew.VECTOR2I(x, y))
        module.Add(pad)
        pad_count += 1

# Mounting holes
mount_dia = 2.3
mount_spacing = 26.67
mount_y = mm_to_nm(-3.81)  # Approx. 2.54 mm below bottom row

for x_offset in [-mount_spacing / 2, mount_spacing / 2]:
    hole = pcbnew.PAD(module)
    hole.SetPadName("")
    hole.SetShape(pcbnew.PAD_SHAPE_CIRCLE)
    hole.SetSize(pcbnew.VECTOR2I(mm_to_nm(mount_dia), mm_to_nm(mount_dia)))
    hole.SetDrillSize(pcbnew.VECTOR2I(mm_to_nm(mount_dia), mm_to_nm(mount_dia)))
    hole.SetPosition(pcbnew.VECTOR2I(mm_to_nm(x_offset + 6.35), mount_y))  # Centered under pin field
    hole.SetAttribute(pcbnew.PAD_ATTRIB_NPTH)
    module.Add(hole)

# Mounting holes
mount_dia = 2.3
mount_spacing = 26.67  # mm
mount_y = mm_to_nm(-3.81)  # 3.81 mm below bottom row
pinfield_center_x = mm_to_nm((cols - 1) * pin_pitch_x / 2)

for x_offset in [-mount_spacing / 2, mount_spacing / 2]:
    x = pinfield_center_x + mm_to_nm(x_offset)
    hole = pcbnew.PAD(module)
    hole.SetPadName("")
    hole.SetShape(pcbnew.PAD_SHAPE_CIRCLE)
    hole.SetSize(pcbnew.VECTOR2I(mm_to_nm(mount_dia), mm_to_nm(mount_dia)))
    hole.SetDrillSize(pcbnew.VECTOR2I(mm_to_nm(mount_dia), mm_to_nm(mount_dia)))
    hole.SetPosition(pcbnew.VECTOR2I(x, mount_y))
    hole.SetAttribute(pcbnew.PAD_ATTRIB_NPTH)
    module.Add(hole)
    
board.Add(module)
print("✅ MDR-50 footprint with 4-row staggered pins and mounting holes added to board.")