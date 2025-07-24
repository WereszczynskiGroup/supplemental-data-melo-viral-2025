import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

# Setup
protein_types = ['Viral', 'Trunc. Euk', 'Eukaryotic']
colors = ['#0072B2', '#D55E00', '#009E73']


alpha_widom = 1.0
alpha_alpha = 0.4

means = {
    'Tet–Tet':     [[161.3, 162.6], [177.9, 176.7], [186.1, 192.5]],
    'D1–D1':       [[73.4, 71.2],   [87.7, 86.3],   [93.1, 93.5]],
    'D2–D2':       [[69.8, 72.6],   [88.2, 86.2],   [93.1, 91.1]]
}

errors = {
    'Tet–Tet':     [[1.89, 1.42], [0.43, 0.96], [1.46, 1.44]],
    'D1–D1':       [[0.17, 0.76], [0.19, 0.40], [0.44, 0.80]],
    'D2–D2':       [[1.20, 0.99], [0.61, 0.44], [0.28, 0.43]]
}

group_count = len(protein_types)
bar_width = 0.4
x = np.arange(group_count)


def plot_pairbars(ax, interaction, title):
    for i in range(group_count):
        # Widom bar
        ax.bar(x[i] - bar_width/2,
               means[interaction][i][0],
               yerr=errors[interaction][i][0],
               width=bar_width,
               color=colors[i],
               alpha=alpha_widom,
               capsize=3,
               edgecolor=(0, 0, 0, 1),  
               linewidth=0.5,
               error_kw=dict(linewidth=0.5))
        
        # Alpha bar
        ax.bar(x[i] + bar_width/2,
               means[interaction][i][1],
               yerr=errors[interaction][i][1],
               width=bar_width,
               color=colors[i],
               alpha=alpha_alpha,
               capsize=3,
               edgecolor=(0, 0, 0, 1), 
               linewidth=0.5,
               error_kw=dict(linewidth=0.5))


    ax.set_xticks(x)
    ax.set_xticklabels(protein_types, rotation=45)
    ax.set_title(title, fontsize=10)
    ax.tick_params(axis='both', labelsize=9)


fig = plt.figure(figsize=(3.25, 3.3))
gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1])

# Row 1 (spanning both columns)
ax0 = fig.add_subplot(gs[0, :])
plot_pairbars(ax0, 'Tet–Tet', 'Tetramer')
ax0.set_xticklabels(protein_types, rotation=0)
ax0.set_ylim(0, 200)

# Row 2
ax1 = fig.add_subplot(gs[1, 0])
plot_pairbars(ax1, 'D1–D1', 'Dimer1')
ax1.set_ylim(0, 100)

ax2 = fig.add_subplot(gs[1, 1], sharey=ax1)
plt.setp(ax2.get_yticklabels(), visible=False)
plot_pairbars(ax2, 'D2–D2', 'Dimer2')
ax2.set_ylim(0, 100)
ax1.set_xticklabels([])
ax2.set_xticklabels([])


# Create legend handles
legend_handles = [
    Patch(facecolor='gray', edgecolor='black', alpha=1.0, label='Widom 601'),
    Patch(facecolor='gray', edgecolor='black', alpha=0.4, label='Alpha Satellite')
]

# Add legend to figure
fig.legend(handles=legend_handles,
           title='DNA Type',
           loc='lower center',
           bbox_to_anchor=(0.56, 0.005),
           ncol=2,
           fontsize=8,
           title_fontsize=8)

fig.text(0.015, 0.53, 'Hydrogen Bond Count', va='center', rotation='vertical')
fig.suptitle("Intra Subunit Interactions", fontsize=12,fontweight='bold',x=0.56)
plt.subplots_adjust(hspace=0.6, wspace=0.3,top=0.85, bottom=0.17, left=0.18,right=0.94)


plt.savefig("Fig5-hbonds_intra.pdf")

