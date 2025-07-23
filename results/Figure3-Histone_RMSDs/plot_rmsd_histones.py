import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import to_rgba

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

# Load data
df = pd.read_csv("rmsd_data.csv")

# Set histone types, proteins, and DNA sequences
histone_types = df["Histone_Type"].unique()
proteins = ["Viral", "Truncated Eukaryotic", "Eukaryotic"]
prot = ["Viral", "Trunc Euk.", "Euk."]
dnas = ["Widom 601", "Alpha-Satellite"]

# Bar width and positions
bar_width = 0.2
x = np.arange(len(proteins))  # positions for Viral, Eukaryotic, Truncated

# Base colors by histone type
base_colors = {'H4': 'forestgreen', 'H3': 'royalblue', 'H2A': 'gold', 'H2B': 'firebrick'}
alpha_values = {'Widom 601': 1.0, 'Alpha-Satellite': 0.4}

# Error bar styling
error_style = dict(ecolor='black', elinewidth=0.4, capsize=3, capthick=0.4)

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(3.25, 5), sharey=True,
                         gridspec_kw={'wspace': 0.12, 'hspace': 0.28})
axes = axes.flatten()

# Loop through each histone type (H4, H3, H2A, H2B)
for i, htype in enumerate(histone_types):
    ax = axes[i]
    hdata = df[df["Histone_Type"] == htype]
    histones = hdata["Histone"].unique()

    n_bars_per_group = len(histones) * len(dnas)
    group_width = bar_width * n_bars_per_group

    for j, protein in enumerate(proteins):
        for k, dna in enumerate(dnas):
            for l, histone in enumerate(histones):
                subset = hdata[(hdata["Protein"] == protein) &
                               (hdata["DNA"] == dna) &
                               (hdata["Histone"] == histone)]
                if subset.empty:
                    continue
                rmsd = subset["RMSD"].values[0]
                err = subset["Error"].values[0]

                # Compute position
                pos = x[j] - (group_width / 2) + (k * len(histones) + l) * bar_width

                # Set RGBA face color with appropriate alpha
                color = base_colors[htype]
                alpha_val = alpha_values[dna]
                face_color = to_rgba(color, alpha_val)

                # Plot bar with black outline and black error bars
                ax.bar(pos, rmsd, bar_width, yerr=err,
                       color=face_color,
                       edgecolor='black', linewidth=0.8,
                       error_kw=error_style)

    # Formatting
    ax.set_title(f"{htype} Histones", fontsize=10)
    ax.set_xticks(x)
    ax.set_ylim(0, 5)
    if i in [2, 3]:
        ax.set_xticklabels(prot, rotation=30)
    else:
        ax.set_xticklabels([])  # remove ticks and labels


# Global legend (manually building it)
legend_patches = []
for htype in histone_types:
    patch = Patch(facecolor=base_colors[htype], edgecolor='black')
    legend_patches.append(patch)

# DNA alpha shading patch
dna_patches = [
    Patch(facecolor='gray', alpha=1.0, edgecolor='black', label='Widom 601'),
    Patch(facecolor='gray', alpha=0.4, edgecolor='black', label='Alpha-Satellite')
]


axes[2].legend(handles=dna_patches, loc='upper left', bbox_to_anchor=(-0.03,1.03), fontsize=8, frameon=False)


# Suptitle and layout
fig.suptitle("Average RMSDs of Histones",fontweight='bold',fontsize=12,x=0.54)#,0.9)
fig.text(0.01, 0.5, 'Average RMSD (Å)', va='center', rotation='vertical', fontsize=10)


# Adjust overall figure layout
fig.subplots_adjust(left=0.12, right=0.96)#, top=0.93, bottom=0.1, wspace=0.15, hspace=0.15)

# Save to file
plt.savefig("Fig3-rmsd_histones.pdf")

