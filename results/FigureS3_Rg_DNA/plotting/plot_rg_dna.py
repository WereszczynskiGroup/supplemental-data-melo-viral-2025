import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def load_rg_data(filename):
    df = pd.read_csv(filename, sep="#", header=None, names=["Entry", "Exit"],skiprows=1)
    df["Entry"] = df["Entry"].astype(str).str.strip().astype(float)
    df["Exit"] = df["Exit"].astype(str).str.strip().astype(float)
    return df

euk_alpha = load_rg_data("euk_alpha_rg_dna.dat") 
euk_widom = load_rg_data("euk_widom_rg_dna.dat") 
virus_alpha = load_rg_data("virus_alpha_rg_dna.dat") 
virus_widom = load_rg_data("virus_widom_rg_dna.dat") 
trunc_euk_alpha = load_rg_data("trunc_euk_alpha_rg_dna.dat") 
trunc_euk_widom = load_rg_data("trunc_euk_widom_rg_dna.dat") 

# Font settings
font = {
    'family': 'Arial',
    'color': 'black',
    'size': 10
}

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

# Set style
sns.set(style='dark')

# Create figure
fig, axs = plt.subplots(2, 3, figsize=(6.75, 6), sharex=False, sharey=False, gridspec_kw={'wspace': 0.018, 'hspace': 0.58})

plt.subplots_adjust(left=0.08, right=0.92, top=0.90, bottom=0.2)#, wspace=0.15, hspace=0.55)\n",

# Add main figure title and row labels
fig.suptitle("Radius of Gyration (Entry DNA / Exit DNA)", fontsize=14, fontweight='bold', y=1.00)
fig.text(0.51, 0.94, "Widom 601 DNA", ha='center', fontsize=12, fontweight='bold',color='red')
fig.text(0.51, 0.51, "Alpha-Satellite DNA", ha='center', fontsize=12, fontweight='bold',color='blue')


# Set ticks
x_ticks = np.arange(40, 65, 5)
y_ticks = np.arange(40, 65, 5)

# Configure each subplot
for i, ax in enumerate(axs.flat):
    ax.set_xlim(40, 60)
    ax.set_ylim(40, 60)
    ax.set_xticks(x_ticks)
    ax.xaxis.tick_bottom()
    ax.set_yticks(y_ticks)
    ax.yaxis.set_ticks_position('left')
    ax.set_aspect('equal', adjustable='box')
    ax.tick_params(labelsize=10, width=1)

    # X-axis label for all
    ax.set_xlabel("Entry DNA Rg ($\AA$)", fontsize=10)

    # Y-axis label only for leftmost column
    if i % 3 == 0:
        ax.set_ylabel("Exit DNA Rg ($\AA$)", fontsize=10)
    else:
        ax.set_ylabel("")
        ax.set_yticklabels([])

# Plot heatmaps
sns.kdeplot(ax=axs[0, 0], data=virus_widom, x="Entry", y="Exit", fill=True, cbar=False, cmap="rainbow")
axs[0, 0].set_title('Viral Protein', fontdict=font)

sns.kdeplot(ax=axs[0, 1], data=trunc_euk_widom, x="Entry", y="Exit", fill=True, cbar=False, cmap="rainbow")
axs[0, 1].set_title('Truncated Eukaryotic Protein', fontdict=font)
axs[0, 1].set_ylabel("")

sns.kdeplot(ax=axs[0, 2], data=euk_widom, x="Entry", y="Exit", fill=True, cbar=False, cmap="rainbow")
axs[0, 2].set_title('Eukaryotic Protein', fontdict=font)
axs[0, 2].set_ylabel("")

sns.kdeplot(ax=axs[1, 0], data=virus_alpha, x="Entry", y="Exit", fill=True, cbar=False, cmap="rainbow")
axs[1, 0].set_title('Viral Protein', fontdict=font)

sns.kdeplot(ax=axs[1, 1], data=trunc_euk_alpha, x="Entry", y="Exit", fill=True, cbar=False, cmap="rainbow")
axs[1, 1].set_title('Truncated Eukaryotic Protein', fontdict=font)
axs[1, 1].set_ylabel("")

sns.kdeplot(ax=axs[1, 2], data=euk_alpha, x="Entry", y="Exit", fill=True, cbar=False, cmap="rainbow")
axs[1, 2].set_title('Eukaryotic Protein', fontdict=font)
axs[1, 2].set_ylabel("")

# Save to PDF
plt.savefig('FigS3_Rg_Entry_Exit.pdf', bbox_inches='tight')

