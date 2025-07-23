import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10


#Load data

#H4 histone
x, y, yerr = np.loadtxt("virus_widom.rmsf.H4_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
a, b, berr = np.loadtxt("virus_alpha.rmsf.H4_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
c, d, derr = np.loadtxt("euk_widom.rmsf.H4_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
f, g, gerr = np.loadtxt("euk_alpha.rmsf.H4_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
h, j, jerr = np.loadtxt("trunc_euk_widom.rmsf.H4_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
k, l, lerr = np.loadtxt("trunc_euk_alpha.rmsf.H4_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))

z = np.loadtxt("virus_numH4.dat", skiprows=1, usecols=(0,), dtype=str)
t = np.loadtxt("trunc_numH4.dat", skiprows=1, usecols=(0,), dtype=str)


#H3 histone
x2, y2, yerr2 = np.loadtxt("virus_widom.rmsf.H3_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
a2, b2, berr2 = np.loadtxt("virus_alpha.rmsf.H3_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
c2, d2, derr2 = np.loadtxt("euk_widom.rmsf.H3_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
f2, g2, gerr2 = np.loadtxt("euk_alpha.rmsf.H3_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
h2, j2, jerr2 = np.loadtxt("trunc_euk_widom.rmsf.H3_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
k2, l2, lerr2 = np.loadtxt("trunc_euk_alpha.rmsf.H3_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))

z2 = np.loadtxt("virus_numH3.dat", skiprows=1, usecols=(0,), dtype=str)
t2 = np.loadtxt("trunc_numH3.dat", skiprows=1, usecols=(0,), dtype=str)


#H2A histone
x3, y3, yerr3 = np.loadtxt("virus_widom.rmsf.H2A_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
a3, b3, berr3 = np.loadtxt("virus_alpha.rmsf.H2A_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
c3, d3, derr3 = np.loadtxt("euk_widom.rmsf.H2A_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
f3, g3, gerr3 = np.loadtxt("euk_alpha.rmsf.H2A_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
h3, j3, jerr3 = np.loadtxt("trunc_euk_widom.rmsf.H2A_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
k3, l3, lerr3 = np.loadtxt("trunc_euk_alpha.rmsf.H2A_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))

z3 = np.loadtxt("virus_numH2A.dat", skiprows=1, usecols=(0,), dtype=str)
t3 = np.loadtxt("trunc_numH2A.dat", skiprows=1, usecols=(0,), dtype=str)


#H2B histone
x4, y4, yerr4 = np.loadtxt("virus_widom.rmsf.H2B_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
a4, b4, berr4 = np.loadtxt("virus_alpha.rmsf.H2B_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
c4, d4, derr4 = np.loadtxt("euk_widom.rmsf.H2B_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
f4, g4, gerr4 = np.loadtxt("euk_alpha.rmsf.H2B_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
h4, j4, jerr4 = np.loadtxt("trunc_euk_widom.rmsf.H2B_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))
k4, l4, lerr4 = np.loadtxt("trunc_euk_alpha.rmsf.H2B_avg.error.dat", usecols=(0, 1, 2), unpack=True, comments=('#','@','&'))

z4 = np.loadtxt("virus_numH2B.dat", skiprows=1, usecols=(0,), dtype=str)
t4 = np.loadtxt("trunc_numH2B.dat", skiprows=1, usecols=(0,), dtype=str)

# Create a 2x2 grid of subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(6.75,6.6),dpi=300, sharey=True, gridspec_kw={'wspace': 0.1, 'hspace': 0.94})
fig.patch.set_facecolor('white')



# Plot the data in the first subplot 
ax1 = axs[0, 0]
ax1.fill_between(t, y - yerr / 2.2, y + yerr / 2.2, alpha=0.3, linestyle='dashed', color='#0072B2')
ax1.plot(t, y, alpha=0.8, label='Viral Protein/Widom 601 DNA', color='#0072B2')
ax1.fill_between(t, b - berr / 2.2, b + berr / 2.2, alpha=0.3, linestyle='dashed', color='#E69F00')
ax1.plot(t, b, alpha=0.8, label='Viral Protein/Alpha Satellite DNA', color='#E69F00')
ax1.fill_between(t, d - derr / 2.2, d + derr / 2.2, alpha=0.3, linestyle='dashed', color='#009E73')
ax1.plot(t, d, alpha=0.8, label='Eukaryotic Protein/Widom 601 DNA', color='#009E73')
ax1.fill_between(t, g - gerr / 2.2, g + gerr / 2.2, alpha=0.3, linestyle='dashed', color='#D55E00')
ax1.plot(t, g, alpha=0.8, label='Eukaryotic Protein/Alpha Satellite DNA', color='#D55E00')
ax1.fill_between(t, j - jerr / 2.2, j + jerr / 2.2, alpha=0.3, linestyle='dashed', color='#CC79A7')
ax1.plot(t, j, alpha=0.8, label='Truncated Eukaryotic Protein/Widom 601 DNA', color='#CC79A7')
ax1.fill_between(t, l - lerr / 2.2, l + lerr / 2.2, alpha=0.3, linestyle='dashed', color='#999999')
ax1.plot(t, l, alpha=0.8, label='Truncated Eukaryotic Protein/Alpha Satellite DNA', color='#999999')

ax1.set_xlabel(r'Eukaryotic H4 Histone Core')
ax1.set_ylabel(r'RMSF ($\AA$)')
ax1.set_xticks([t[i] for i in range(0, len(t)) if i % 5 == 0])
ax1.set_ylim([0, 9])
ax1.set_xticklabels([t[i] for i in range(0, len(t)) if i % 5 == 0], rotation=90, fontsize=9)
ax1.set_yticklabels(ax1.get_yticks(), fontsize=9)
ax1.margins(x=0)

# Create a twin Axes sharing the yaxis
ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(ax1.get_xticks())  # Set the tick positions from ax1
ax2.set_xticklabels([z[i] for i in range(0, len(z)) if i % 5 == 0], rotation=90, fontsize=9)
ax2.set_xlabel('Viral H4 Histone Core')





# Create a second subplot 
ax3 = axs[0, 1]
ax3.fill_between(t2, y2 - yerr2 / 2.2, y2 + yerr2 / 2.2, alpha=0.3, linestyle='dashed', color='#0072B2')
ax3.plot(t2, y2, alpha=0.8, color='#0072B2')
ax3.fill_between(t2, b2 - berr2 / 2.2, b2 + berr2 / 2.2, alpha=0.3, linestyle='dashed', color='#E69F00')
ax3.plot(t2, b2, alpha=0.8, color='#E69F00')
ax3.fill_between(t2, d2 - derr2 / 2.2, d2 + derr2 / 2.2, alpha=0.3, linestyle='dashed', color='#009E73')
ax3.plot(t2, d2, alpha=0.8, color='#009E73')
ax3.fill_between(t2, g2 - gerr2 / 2.2, g2 + gerr2 / 2.2, alpha=0.3, linestyle='dashed', color='#D55E00')
ax3.plot(t2, g2, alpha=0.8, color='#D55E00')
ax3.fill_between(t2, j2 - jerr2 / 2.2, j2 + jerr2 / 2.2, alpha=0.3, linestyle='dashed', color='#CC79A7')
ax3.plot(t2, j2, alpha=0.8, color='#CC79A7')
ax3.fill_between(t2, l2 - lerr2 / 2.2, l2 + lerr2 / 2.2, alpha=0.3, linestyle='dashed', color='#999999')
ax3.plot(t2, l2, alpha=0.8, color='#999999')

ax3.set_xlabel(r'Eukaryotic H3 Histone Core')#,color='black',fontdict=font) 
ax3.set_xticks([t2[i] for i in range(0, len(t2)) if i % 5 == 0])
ax3.set_ylim([0, 5])
ax3.set_xticklabels([t2[i] for i in range(0, len(t2)) if i % 5 == 0], rotation=90, fontsize=9)
ax3.set_yticklabels(ax3.get_yticks(), fontsize=9)
ax3.margins(x=0)

# Create a twin Axes sharing the yaxis
ax4 = ax3.twiny()
ax4.set_xlim(ax3.get_xlim())
ax4.set_xticks(ax3.get_xticks())  # Set the tick positions from ax3
ax4.set_xticklabels([z2[i] for i in range(0, len(z2)) if i % 5 == 0], rotation=90, fontsize=9)
ax4.set_xlabel('Viral H3 Histone Core')




# Create a third subplot 
ax5 = axs[1, 1]
ax5.fill_between(t3, y3 - yerr3 / 2.2, y3 + yerr3 / 2.2, alpha=0.3, linestyle='dashed', color='#0072B2')
ax5.plot(t3, y3, alpha=0.8, color='#0072B2')
ax5.fill_between(t3, b3 - berr3 / 2.2, b3 + berr3 / 2.2, alpha=0.3, linestyle='dashed', color='#E69F00')
ax5.plot(t3, b3, alpha=0.8, color='#E69F00')
ax5.fill_between(t3, d3 - derr3 / 2.2, d3 + derr3 / 2.2, alpha=0.3, linestyle='dashed', color='#009E73')
ax5.plot(t3, d3, alpha=0.8, color='#009E73')
ax5.fill_between(t3, g3 - gerr3 / 2.2, g3 + gerr3 / 2.2, alpha=0.3, linestyle='dashed', color='#D55E00')
ax5.plot(t3, g3, alpha=0.8, color='#D55E00')
ax5.fill_between(t3, j3 - jerr3 / 2.2, j3 + jerr3 / 2.2, alpha=0.3, linestyle='dashed', color='#CC79A7')
ax5.plot(t3, j3, alpha=0.8, color='#CC79A7')
ax5.fill_between(t3, l3 - lerr3 / 2.2, l3 + lerr3 / 2.2, alpha=0.3, linestyle='dashed', color='#999999')
ax5.plot(t3, l3, alpha=0.8, color='#999999')

ax5.set_xlabel(r'Eukaryotic H2A Histone Core')
ax5.set_xticks([t3[i] for i in range(0, len(t3)) if i % 5 == 0])
ax5.set_ylim([0, 9])
ax5.set_xticklabels([t3[i] for i in range(0, len(t3)) if i % 5 == 0], rotation=90, fontsize=9)
ax5.set_yticklabels(ax5.get_yticks(), fontsize=9)
ax5.margins(x=0)

# Create a twin Axes sharing the yaxis
ax6 = ax5.twiny()
ax6.set_xlim(ax5.get_xlim())
ax6.set_xticks(ax5.get_xticks())  # Set the tick positions from ax5
ax6.set_xticklabels([z3[i] for i in range(0, len(z3)) if i % 5 == 0], rotation=90, fontsize=9)
ax6.set_xlabel('Viral H2A Histone Core')





# Create a fourth subplot
ax7 = axs[1, 0] 
ax7.fill_between(t4, y4 - yerr4 / 2.2, y4 + yerr4 / 2.2, alpha=0.3, linestyle='dashed', color='#0072B2')
ax7.plot(t4, y4, alpha=0.8, color='#0072B2')
ax7.fill_between(t4, b4 - berr4 / 2.2, b4 + berr4 / 2.2, alpha=0.3, linestyle='dashed', color='#E69F00')
ax7.plot(t4, b4, alpha=0.8, color='#E69F00')
ax7.fill_between(t4, d4 - derr4 / 2.2, d4 + derr4 / 2.2, alpha=0.3, linestyle='dashed', color='#009E73')
ax7.plot(t4, d4, alpha=0.8, color='#009E73')
ax7.fill_between(t4, g4 - gerr4 / 2.2, g4 + gerr4 / 2.2, alpha=0.3, linestyle='dashed', color='#D55E00')
ax7.plot(t4, g4, alpha=0.8, color='#D55E00')
ax7.fill_between(t4, j4 - jerr4 / 2.2, j4 + jerr4 / 2.2, alpha=0.3, linestyle='dashed', color='#CC79A7')
ax7.plot(t4, j4, alpha=0.8, color='#CC79A7')
ax7.fill_between(t4, l4 - lerr4 / 2.2, l4 + lerr4 / 2.2, alpha=0.3, linestyle='dashed', color='#999999')
ax7.plot(t4, l4, alpha=0.8,  color='#999999')

ax7.set_xlabel(r'Eukaryotic H2B Histone Core')
ax7.set_ylabel(r'RMSF ($\AA$)')
ax7.set_xticks([t4[i] for i in range(0, len(t4)) if i % 5 == 0])
ax7.set_ylim([0, 9])
ax7.set_xticklabels([t4[i] for i in range(0, len(t4)) if i % 5 == 0], rotation=90, fontsize=9)
ax7.set_yticklabels(ax7.get_yticks(), fontsize=9)
ax7.margins(x=0)

# Create a twin Axes sharing the yaxis
ax8 = ax7.twiny()
ax8.set_xlim(ax7.get_xlim())
ax8.set_xticks(ax7.get_xticks())  # Set the tick positions from ax7
ax8.set_xticklabels([z4[i] for i in range(0, len(z4)) if i % 5 == 0], rotation=90, fontsize=9)
ax8.set_xlabel('Viral H2B Histone Core')



fig.legend(loc='upper center', bbox_to_anchor=(0.53, 0.1), shadow=False, ncol=2,fontsize=8)

fig.suptitle("Histone Fluctuations - Viral vs Eukaryotic Residues", fontsize=12,fontweight='bold',x=0.52)


# Adjust figure layout
fig.subplots_adjust(left=0.10, right=0.96, top=0.85, bottom=0.2)


# Save the figure
plt.savefig('Fig4-Histone_RMSF_all_error.pdf')
