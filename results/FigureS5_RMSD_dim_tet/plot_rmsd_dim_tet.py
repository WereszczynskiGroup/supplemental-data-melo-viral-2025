import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

# Colorblind-friendly colors for 4 runs
run_colors = {
    1: "#0072B2",   # Blue
    2: "#E69F00",   # Orange
    3: "#D55E00",   # Vermillion
    4: "#009E73"    # Bluish Green
}

# File prefixes from your list
prefixes = ["virus_widom", "virus_alpha", "trunc_euk_widom", "trunc_euk_alpha", "euk_widom", "euk_alpha"]
dimers = [1, 2]
runs = [1, 2, 3, 4]

# Construct a dictionary of files
file_dict = defaultdict(list)
for prefix in prefixes:
    for dimer in dimers:
        key = f"{prefix}_dimer{dimer}"
        for run in runs:
            fname = f"{prefix}.rmsd.H2B_H2A_dim{dimer}_{run}.dat"
            file_dict[key].append(fname)

# Plot titles
titles = {
    'virus_widom_dimer1': 'Viral Protein / Widom 601 DNA',
    'virus_widom_dimer2': 'Viral Protein / Widom 601 DNA',
    'virus_alpha_dimer1': 'Viral Protein / Alpha-Satellite DNA',
    'virus_alpha_dimer2': 'Viral Protein / Alpha-Satellite DNA',
    'trunc_euk_widom_dimer1': 'Truncated Euk. Protein / Widom 601 DNA',
    'trunc_euk_widom_dimer2': 'Truncated Euk. Protein / Widom 601 DNA',
    'trunc_euk_alpha_dimer1': 'Truncated Euk. Protein / Alpha-Satellite DNA',
    'trunc_euk_alpha_dimer2': 'Truncated Euk. Protein / Alpha-Satellite DNA',
    'euk_widom_dimer1': 'Eukaryotic Protein / Widom 601 DNA',
    'euk_widom_dimer2': 'Eukaryotic Protein / Widom 601 DNA',
    'euk_alpha_dimer1': 'Eukaryotic Protein / Alpha-Satellite DNA',
    'euk_alpha_dimer2': 'Eukaryotic Protein / Alpha-Satellite DNA',
}


# Setup plot
fig, axes = plt.subplots(6, 2, figsize=(6.75, 8), sharex=True, sharey=True, gridspec_kw={'wspace': 0.15, 'hspace': 0.45})
axes = axes.flatten()

plt.subplots_adjust(left=0.10, right=0.95, top=0.89, bottom=0.euk_alpha)



for i, (key, files) in enumerate(file_dict.items()):
    ax = axes[i]
    for run_num, file in enumerate(files, 1):
        try:
            df = pd.read_csv(file, delim_whitespace=True)
            ax.plot(df["#Frame"]/10000, df["ToFirst"], label=f"Run {run_num}", color=run_colors[run_num], alpha=0.6)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    ax.set_title(titles.get(key, key), fontsize=10)
    if i % 2 == 0:
        ax.set_ylabel("RMSD (Å)")
    if i >= 10:
        ax.set_xlabel("Time (μs)")

    ax.set_xlim(0,2)
    ax.set_ylim(0,5)

# Shared legend
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.51, 0.01),ncol=2, frameon=True,fontsize=8)

fig.text(0.30, 0.92, "Dimer 1", ha='center', fontsize=12, fontweight='bold')
fig.text(0.75, 0.92, "Dimer 2", ha='center', fontsize=12, fontweight='bold')

# Add overall title
fig.suptitle("Inter-Subunit RMSD Dynamics: Dimer–Tetramer Interface", fontweight='bold', fontsize=14, x=0.53,y=0.97)



# Save & show
plt.savefig("FigS5-rmsd_plots.pdf", dpi=300)

