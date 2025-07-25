**Radius of Gyration (Rg) of Entry and Exit DNA Calculations (files: protein_dnatype_rg_dna_entry_exit.sh)**

Cpptraj scripts within bash script calculate Rg for each DNA arm (Entry/Exit) within each nucleosome type (viral, eukaryote, truncated eukaryote) for both DNA types (widom 601 and alpha-satellite). 

Script first aligns each protein to the first frame, then calculates the Rg of either the Entry or Exit DNA arm over the entire trajectory and looping over each replica.

- Parmtop and trajectory files mentioned uploaded to Zenodo.
