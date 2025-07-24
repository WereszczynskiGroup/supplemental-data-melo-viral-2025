import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import os


plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10


run_colors = {
    1: "#0072B2",   # Blue
    2: "#E69F00",   # Orange
    3: "#D55E00",   # Vermillion
    4: "#009E73"    # Bluish Green
}



# Set up constants
prefixes = ["virus_widom", "virus_alpha", "euk_widom", "euk_alpha"]
dimers = [1, 2]
runs = [1, 2, 3, 4]

# Build file_dict using nested loops
file_dict = defaultdict(list)
for prefix in prefixes:
    for dimer in dimers:
        key = f"{prefix}_dimer{dimer}"
        for run in runs:
            fname = f"{prefix}_dimer{dimer}.sim{run}"
            file_dict[key].append(fname)

# Plot titles
titles = {
    'virus_widom_dimer1': 'Viral Protein / Widom 601 DNA',
    'virus_widom_dimer2': 'Viral Protein / Widom 601 DNA',
    'virus_alpha_dimer1': 'Viral Protein / Alpha-Satellite DNA',
    'virus_alpha_dimer2': 'Viral Protein / Alpha-Satellite DNA',
    'euk_widom_dimer1': 'Eukaryotic Protein / Widom 601 DNA',
    'euk_widom_dimer2': 'Eukaryotic Protein / Widom 601 DNA',
    'euk_alpha_dimer1': 'Eukaryotic Protein / Alpha-Satellite DNA',
    'euk_alpha_dimer2': 'Eukaryotic Protein / Alpha-Satellite DNA',
}



# Create figure
fig, axes = plt.subplots(4, 2, figsize=(6.75, 6.6), sharex=True, sharey=True, gridspec_kw={'wspace': 0.15, 'hspace': 0.42})


#axes = axes.flatten()
plt.subplots_adjust(left=0.10, right=0.95, top=0.85, bottom=0.15)#, wspace=0.15, hspace=0.55)\n",




# Define fixed plotting order
ordered_keys = [
    'virus_widom_dimer1', 'virus_widom_dimer2',
    'virus_alpha_dimer1', 'virus_alpha_dimer2',
    'euk_widom_dimer1', 'euk_widom_dimer2',
    'euk_alpha_dimer1', 'euk_alpha_dimer2',
]

# Plotting loop
for idx, key in enumerate(ordered_keys):
    row, col = divmod(idx, 2)
    ax = axes[row, col]
    ax.set_xlim(0,2)
    ax.set_ylim(20,65)


    for run_idx, fname in enumerate(file_dict[key], 1):  # run_idx from 1 to 4
        df = pd.read_csv(fname, sep='\s+', header=0)
        label = f"Run {run_idx}" if idx == 0 else None  # Label only in first subplot
        ax.plot(df['#Frame']/10000, df['#Angle'], linewidth=1, alpha=0.6,
                color=run_colors[run_idx], label=label)


    ax.set_title(titles[key], fontsize=10)

    # Only outer axes have labels
    if row == 3:
        ax.set_xlabel("Time (μs)")
    if col == 0:
        ax.set_ylabel("Angle (°)")
    if not (row == 3 or col == 0):
        ax.tick_params(labelleft=False, labelbottom=False)


fig.text(0.30, 0.90, "Dimer 1", ha='center', fontsize=12, fontweight='bold')
fig.text(0.75, 0.90, "Dimer 2", ha='center', fontsize=12, fontweight='bold')
fig.suptitle("Inter-Subunit Angle: Dimer-Tetramer Interface", fontsize=14, fontweight='bold', x=0.52,y=0.97)


# Create shared legend at bottom
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.52, 0.03), ncol=2, frameon=True, fontsize=8)



# Save figure
plt.savefig("FigS4-angle_over_time.pdf", dpi=300)

