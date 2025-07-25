import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10


# Load your 2D-RMSD matrices
rms2d_file1 = 'widom_H4_H3_rms2d.dat'
rms2d_file2 = 'widom_H2B_H2A_rms2d.dat'
rms2d_file3 = 'alpha_H4_H3_rms2d.dat'
rms2d_file4 = 'alpha_H2B_H2A_rms2d.dat'


rmsd_matrix1 = np.loadtxt(rms2d_file1)[:, 1:]  # strip #Frame column if present
rmsd_matrix2 = np.loadtxt(rms2d_file2)[:, 1:]
rmsd_matrix3 = np.loadtxt(rms2d_file3)[:, 1:]  # strip #Frame column if present
rmsd_matrix4 = np.loadtxt(rms2d_file4)[:, 1:]

# Extract upper triangle values, excluding the diagonal
upper_tri_values1 = rmsd_matrix1[np.triu_indices_from(rmsd_matrix1, k=1)]
upper_tri_values2 = rmsd_matrix2[np.triu_indices_from(rmsd_matrix2, k=1)]
upper_tri_values3 = rmsd_matrix3[np.triu_indices_from(rmsd_matrix3, k=1)]
upper_tri_values4 = rmsd_matrix4[np.triu_indices_from(rmsd_matrix4, k=1)]

# Set up subplots side-by-side
fig, axs = plt.subplots(1, 2, figsize=(6.75, 2.3), sharex=True, sharey=True, gridspec_kw={'wspace': 0.13})

plt.subplots_adjust(top=0.76, bottom=0.23, left=0.10,right=0.90)


# Normalized density histogram
axs[0].hist(upper_tri_values1, bins=50, edgecolor='black', label='H4-H3', alpha=0.6,density=True)
axs[0].hist(upper_tri_values2, bins=50, edgecolor='black', label='H2B-H2A', alpha=0.6,density=True)
axs[0].set_xlabel('RMSD (Å)')
axs[0].set_ylabel('Normalized Frequency')
axs[0].set_title('Widom 601 DNA',color='red',x=0.46)

# Normalized density histogram
axs[1].hist(upper_tri_values3, bins=50, edgecolor='black', label='H4-H3', alpha=0.6, density=True)
axs[1].hist(upper_tri_values4, bins=50, edgecolor='black', label='H2B-H2A', alpha=0.6, density=True)
axs[1].set_xlabel('RMSD (Å)')
axs[1].set_title('Alpha-Satellite DNA',color='blue',x=0.54)
axs[1].legend(fontsize=8)

axs[1].set_xlim(0,15)
axs[1].set_ylim(0,0.43)

fig.suptitle('Viral Connectors RMSD', fontsize=14,fontweight='bold')#, x=0.51)

# Layout adjustments
plt.savefig('FigS8-rmsd_hist_connectors.pdf', dpi=300)

