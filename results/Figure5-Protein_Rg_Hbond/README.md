Radius of Gyration
-
Rg timeseries data of each protein type was calculated for the 4 replicas and as well as concatenated in intermediate result files for plotting. This excludes 100ns from each run to account for equilibration time.
The histogram plotting script calculates the normalized frequency of the Rg for protein as well as plots the histogram for each nucleosomal system.

Hydrogen Bonding
-
Utilized VMD to process hydrogen bonds counts to account for how often each residue forms these bonds across the system replicas, as calculated between and within tetramer and dimer subunits of the nucleosome. Averages and standard error of these bond counts were calculated for each replica, resulting in the output files located in these folders. 

Each plotting script has the average hbond values and standard error loaded in, and coded to plot barplots comparing the hydrogen bonding at the location (inter- and intra- tetramer and dimer subunits) within the nucleosome across systems (Proteins: viral, eukaryotic, truncated eukaryotic; DNA: widom 601 and alpha-satellite DNA)
