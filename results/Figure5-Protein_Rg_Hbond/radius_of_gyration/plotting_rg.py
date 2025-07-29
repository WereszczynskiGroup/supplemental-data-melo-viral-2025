import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

# Load the data
a, b = np.loadtxt("virus_widom_rg_all.dat", usecols=(0, 1), unpack=True, comments=('#', '@', '&'))
c = np.loadtxt("virus_alpha_rg_all.dat", usecols=(1,), unpack=True, comments=('#', '@', '&'))
d = np.loadtxt("trunc_euk_widom_rg_all.dat", usecols=(1,), unpack=True, comments=('#','@','&'))
e = np.loadtxt("trunc_euk_alpha_rg_all.dat", usecols=(1,), unpack=True, comments=('#','@','&'))
f = np.loadtxt("euk_widom_rg_all.dat", usecols=(1,), unpack=True, comments=('#','@','&'))
g = np.loadtxt("euk_alpha_rg_all.dat", usecols=(1,), unpack=True, comments=('#','@','&'))

# Create one subplot
fig, ax = plt.subplots(figsize=(3.5, 3.5))

# X range for KDE
x_vals = np.linspace(26, 29, 1000)


ax.plot(x_vals, gaussian_kde(b)(x_vals), label="Viral / Widom 601 DNA", color='#0072B2', linestyle='-')
ax.plot(x_vals, gaussian_kde(c)(x_vals), label="Viral / Alpha-Satellite DNA", color='#0072B2', alpha=0.7,linestyle='--')

ax.plot(x_vals, gaussian_kde(d)(x_vals), label="Eukaryotic / Widom 601", color='#D55E00', linestyle='-')
ax.plot(x_vals, gaussian_kde(e)(x_vals), label="Eukaryotic / Alpha-Satellite", color='#D55E00', alpha=0.7, linestyle='--')

ax.plot(x_vals, gaussian_kde(f)(x_vals), label="Trunc Euk. / Widom 601", color='#009E73', linestyle='-')
ax.plot(x_vals, gaussian_kde(g)(x_vals), label="Trunc Euk. / Alpha-Satellite", color='#009E73', alpha=0.7, linestyle='--')

# Labels, legend, title
ax.set_xlabel('Radius of Gyration ($\AA$)')
ax.set_ylabel('Normalized Frequency')
ax.set_xlim(26,29)
ax.set_ylim(0,5)
ax.set_title('Protein Core Rg',fontsize=12,fontweight='bold')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig('Fig5-protein_core_rg.pdf')

