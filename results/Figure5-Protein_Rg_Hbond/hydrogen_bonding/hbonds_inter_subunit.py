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
    'Tet–D1':      [[9.7, 6.9],     [11.5, 13.6],   [13.1, 13.3]],
    'Tet–D2':      [[9.3, 9.0],     [11.8, 12.1],   [13.6, 12.5]],
    'Dim1-Dim2':   [[1.5, 1.2],     [1.2, 1.0],   [1.0, 0.9]]
}

errors = {
    'Tet–D1':      [[0.65, 1.13], [0.21, 0.26], [0.52, 0.50]],
    'Tet–D2':      [[0.85, 1.20], [0.15, 0.25], [0.40, 0.38]],
    'Dim1-Dim2':   [[0.60, 0.11], [0.17, 0.13], [0.10, 0.16]]}

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


fig = plt.figure(figsize=(3.25, 2.3))
gs = fig.add_gridspec(1, 3)

ax0 = fig.add_subplot(gs[0, 0])
plot_pairbars(ax0, 'Tet–D1', 'Tet–Dimer1')
#ax0.set_xticklabels(protein_types, rotation=45)
#ax0.set_ylabel('Hydrogen Bond Count')
ax0.set_ylim(0, 15)

ax1 = fig.add_subplot(gs[0, 1],sharey=ax0)
plt.setp(ax1.get_yticklabels(), visible=False)
plot_pairbars(ax1, 'Tet–D2', 'Tet–Dimer2')
#ax1.set_ylabel('Hydrogen Bond Count')
#ax1.set_ylim(0, 100)

ax2 = fig.add_subplot(gs[0, 2],sharey=ax0)
plt.setp(ax2.get_yticklabels(), visible=False)
plot_pairbars(ax2, 'Dim1-Dim2', 'Dimer1-Dimer2')
#ax2.set_ylim(0, 100)
ax0.set_xticklabels([])
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
fig.suptitle("Inter Subunit Interactions", fontweight='bold',fontsize=12,x=0.56)
plt.subplots_adjust(hspace=0.6, wspace=0.3,top=0.75, bottom=0.3, left=0.18,right=0.94)


plt.savefig("Fig5-hbonds_inter.pdf")

