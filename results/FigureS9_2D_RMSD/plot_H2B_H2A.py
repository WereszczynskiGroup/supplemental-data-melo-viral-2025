import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10


# Load your two RM2D matrices
file1 = 'widom_H2B_H2A_rms2d.dat'
file2 = 'alpha_H2B_H2A_rms2d.dat'
matrix1 = np.loadtxt(file1)[:, 1:]
matrix2 = np.loadtxt(file2)[:, 1:]

# Check RMSD ranges
print(f"{file1} RMSD range: {matrix1.min():.2f} - {matrix1.max():.2f} Å")
print(f"{file2} RMSD range: {matrix2.min():.2f} - {matrix2.max():.2f} Å")

# Number of frames (assuming square matrices)
num_frames = matrix1.shape[0]
if num_frames != 16000:
    print(f"Warning: Expected 16000 frames, got {num_frames}")

# Set up side-by-side subplots
fig, axs = plt.subplots(1, 2, figsize=(6.75, 3.5), gridspec_kw={'wspace': 0.15, 'hspace': 0.45})
plt.subplots_adjust(top=0.95, bottom=0.10, left=0.15,right=0.90)

# Add overall title
fig.suptitle('2D RMSD Heatmaps for H2B-H2A Connector', fontsize=12)

# Shared parameters
vmin, vmax = 0, 14
cmap = 'viridis'

# Ticks every 2000 frames
tick_positions = np.arange(0, num_frames+1, 2000)
tick_labels_positions = tick_positions[:-1] + 1000  # centers at 1000, 3000, etc.
run_labels = ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 1', 'Run 2', 'Run 3', 'Run 4',]

# Divider positions at 2000, 4000, 6000
divider_positions = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000]

# Plot matrix 1
im1 = axs[0].imshow(matrix1, cmap=cmap, vmin=vmin, vmax=vmax, origin='lower', interpolation='nearest')
axs[0].set_title(f'Widom 601 DNA',color='red')
axs[0].set_xticks(tick_labels_positions)
axs[0].set_yticks(tick_labels_positions)
axs[0].set_xticklabels(run_labels, rotation=45, fontsize=8)
axs[0].set_yticklabels(run_labels, fontsize=8)

# Add dividers
for pos in divider_positions:
    axs[0].axhline(y=pos-0.5, color='black', linestyle='dotted', linewidth=1)
    axs[0].axvline(x=pos-0.5, color='black', linestyle='dotted', linewidth=1)

# Plot matrix 2
im2 = axs[1].imshow(matrix2, cmap=cmap, vmin=vmin, vmax=vmax, origin='lower', interpolation='nearest')
axs[1].set_ylabel('Frame')
axs[1].set_title(f'Alpha-Satellite DNA',color='blue')
axs[1].set_xticks(tick_labels_positions)
axs[1].set_yticks(tick_labels_positions)
axs[1].set_xticklabels(run_labels, rotation=45, fontsize=8)
axs[1].set_yticklabels([])
axs[1].set_ylabel('')




line1 = plt.Line2D([0.07, 0.07], [0.56, 0.81], color='black', linewidth=0.5, transform=fig.transFigure)
line2 = plt.Line2D([0.07, 0.07], [0.24, 0.49], color='black', linewidth=0.5, transform=fig.transFigure)
fig.add_artist(line1)
fig.add_artist(line2)


line3 = plt.Line2D([0.16, 0.29], [0.09, 0.09], color='black', linewidth=0.5, transform=fig.transFigure)
line4 = plt.Line2D([0.33, 0.46], [0.09, 0.09], color='black', linewidth=0.5, transform=fig.transFigure)
fig.add_artist(line3)
fig.add_artist(line4)


line5 = plt.Line2D([0.54, 0.67], [0.09, 0.09], color='black', linewidth=0.5, transform=fig.transFigure)
line6 = plt.Line2D([0.70, 0.83], [0.09, 0.09], color='black', linewidth=0.5, transform=fig.transFigure)
fig.add_artist(line5)
fig.add_artist(line6)

# Add dividers
for pos in divider_positions:
    axs[1].axhline(y=pos-0.5, color='black', linestyle='dotted', linewidth=1)
    axs[1].axvline(x=pos-0.5, color='black', linestyle='dotted', linewidth=1)


cbar = fig.colorbar(im2, ax=axs, orientation='vertical', fraction=0.025, pad=0.04)
fig.text(0.95, 0.5, 'RMSD (Å)', va='center', rotation=270)


fig.text(0.04, 0.69, 'H2B-H2A.2', va='center', rotation='vertical')
fig.text(0.04, 0.37, 'H2B-H2A.1', va='center', rotation='vertical')



fig.text(0.18, 0.05, 'H2B-H2A.1', va='center', rotation='horizontal')
fig.text(0.34, 0.05, 'H2B-H2A.2', va='center', rotation='horizontal')

fig.text(0.55, 0.05, 'H2B-H2A.1', va='center', rotation='horizontal')
fig.text(0.71, 0.05, 'H2B-H2A.2', va='center', rotation='horizontal')


plt.savefig('rms2d_H2B_H2A.pdf')

