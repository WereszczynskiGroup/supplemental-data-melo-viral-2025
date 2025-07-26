import re
import numpy as np
from pymbar import timeseries
from math import sqrt

####### Edit output file names #######
output_file1 = "H2A_dna_complex_data.txt"
output_file2 = "H2A_dna_receptor_data.txt"
output_file3 = "H2A_dna_ligand_data.txt"
######################################

# Function to comment non-numeric lines
def edit_xvg_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if re.match(r'^\s*-?\d', line):
                file.write(line)
            else:
                if not line.startswith('#'):
                    file.write(f'#{line}')
                else:
                    file.write(line)
    print(filename + ' edited')

def load_columns_by_name(fname, columns_to_keep):
    # Map possible alternative header names for each desired column
    column_aliases = {
        'Frame #': ['Frame #'],
        'VDWAALS': ['VDWAALS'],
        'EEL': ['EEL'],
        'EGB': ['EGB'],
        'ESURF': ['ESURF'],
        'TOTAL': ['TOTAL', 'DELTA TOTAL']
    }

    col_indices = {}
    data_lines = []
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            if 'Frame #' in line:
                header = [h.strip() for h in line.lstrip('#').split(',')]
                for col in columns_to_keep:
                    found = False
                    for alias in column_aliases[col]:
                        if alias in header:
                            col_indices[col] = header.index(alias)
                            found = True
                            break
                    if not found:
                        raise ValueError(f"Column '{col}' not found in {fname}. Available headers: {header}")
                continue
            if not line.startswith('#') and col_indices:
                parts = line.split(',')
                if len(parts) >= max(col_indices.values()) + 1:
                    data_lines.append([float(parts[col_indices[c]]) for c in columns_to_keep])
    if not data_lines:
        raise ValueError(f"No data read from {fname}.")
    return np.array(data_lines)

# Files list
files = [f'decomp_chunk{str(i).zfill(2)}.dat' for i in range(1, 21)]

# Comment header lines in all files
for f in files:
    edit_xvg_file(f)

# Columns you need
columns = ['Frame #', 'VDWAALS', 'EEL', 'EGB', 'ESURF', 'TOTAL']

# Predefine lists to hold data
VdWcom, VdWrec, VdWlig = [], [], []
Eleccom, Elecrec, Eleclig = [], [], []

# Process each file
for fname in files:
    data = load_columns_by_name(fname, columns)

    time = data[:, 0]
    vdwaals = data[:, 1]
    eel = data[:, 2]
    egb = data[:, 3]
    esurf = data[:, 4]
    total = data[:, 5]

    # Partition indices
    nframes = len(time)
    comp0, compf = 0, int(nframes / 4)
    rec0, recf  = compf, int(2 * nframes / 4)
    lig0, ligf  = recf, int(3 * nframes / 4)

    # Combine Elec and VdW
    Elec = eel + egb
    VdW = vdwaals + esurf

    # Append to master lists
    VdWcom.extend(VdW[comp0:compf])
    VdWrec.extend(VdW[rec0:recf])
    VdWlig.extend(VdW[lig0:ligf])

    Eleccom.extend(Elec[comp0:compf])
    Elecrec.extend(Elec[rec0:recf])
    Eleclig.extend(Elec[lig0:ligf])

# Convert to numpy arrays
VdWcom, VdWrec, VdWlig = map(np.array, [VdWcom, VdWrec, VdWlig])
Eleccom, Elecrec, Eleclig = map(np.array, [Eleccom, Elecrec, Eleclig])

# Write output files
with open(output_file1, "w") as f:
    f.write("# Complex\n# Elec VdW\n")
    for i in range(len(VdWcom)):
        f.write(f"{i} {Eleccom[i]:.6f} {VdWcom[i]:.6f}\n")
print(f"Data written to {output_file1}")

with open(output_file2, "w") as f:
    f.write("# Receptor\n# Elec VdW\n")
    for i in range(len(VdWrec)):
        f.write(f"{i} {Elecrec[i]:.6f} {VdWrec[i]:.6f}\n")
print(f"Data written to {output_file2}")

with open(output_file3, "w") as f:
    f.write("# Ligand\n# Elec VdW\n")
    for i in range(len(VdWlig)):
        f.write(f"{i} {Eleclig[i]:.6f} {VdWlig[i]:.6f}\n")
print(f"Data written to {output_file3}")

# Error propagation
def sumsq(a, b, c):
    return a*a + b*b + c*c

totalcom = VdWcom + Eleccom
VdW = VdWcom - VdWrec - VdWlig
El = Eleccom - Elecrec - Eleclig
total = El + VdW

# --- Updated: Use fixed decorrelation time ---
SI = 100.0  # frames
N = np.floor(len(totalcom) / SI)


avgVdW = np.average(VdWcom) - np.average(VdWrec) - np.average(VdWlig)
VdWsterr = sqrt(sumsq(np.std(VdWcom, ddof=1)/np.sqrt(N), np.std(VdWlig, ddof=1)/np.sqrt(N), np.std(VdWrec, ddof=1)/np.sqrt(N)))
r_avgVdW = np.round(avgVdW, 1)
r_VdWsterr = np.round(VdWsterr, 1)

avgEl = np.average(Eleccom) - np.average(Elecrec) - np.average(Eleclig)
Elsterr = sqrt(sumsq(np.std(Eleccom, ddof=1)/np.sqrt(N), np.std(Eleclig, ddof=1)/np.sqrt(N), np.std(Elecrec, ddof=1)/np.sqrt(N)))
r_avgEl = np.round(avgEl, 1)
r_Elsterr = np.round(Elsterr, 1)

avgtotal = avgEl + avgVdW
totalsterr = sqrt(sumsq(VdWsterr, Elsterr, 0))
r_avgtotal = np.round(avgtotal, 1)
r_totalsterr = np.round(totalsterr, 1)

with open("decorrelation.dat", "w") as f:
    f.write(f'\nInefficiency analysis using fixed decorrelation time of {SI:.1f} frames.\n')
    f.write(f'Significant points: {int(N)} | Decorrelation time = {SI:.1f} frames\n\n')
    f.write(f'VdW: {r_avgVdW} +/- {r_VdWsterr}\n')
    f.write(f'Elec: {r_avgEl} +/- {r_Elsterr}\n')
    f.write(f'Total: {r_avgtotal} +/- {r_totalsterr}\n')
