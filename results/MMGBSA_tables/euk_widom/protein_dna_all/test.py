import numpy as np

# File to read
fname = "per_residue_decomp_chunk20.dat"  # replace this

# Columns you want to keep
wanted_cols = ['Frame #', 'VDWAALS', 'EEL', 'EGB', 'ESURF', 'TOTAL']

# Read the header and get column indices
with open(fname) as f:
    for line in f:
        if not line.startswith("#"):
            continue
        header = line.strip().lstrip('#').split(',')
        break

# Find the column numbers you want
col_indices = []
for col_name in wanted_cols:
    if col_name in header:
        col_indices.append(header.index(col_name))
    else:
        print(f"Warning: {col_name} not found in header.")

print(f"Using columns: {col_indices}")

# Load only those columns by index
data = np.loadtxt(fname, delimiter=',', comments='#', usecols=col_indices, unpack=True)

# Done — now you can access columns in order you listed them
# For example, if you want Frame # and TOTAL:
frames = data[0]
totals = data[-1]

# Quick print to verify
print("\nFirst 5 frames and totals:")
for i in range(5):
    print(f"Frame {int(frames[i])}: TOTAL = {totals[i]}")

