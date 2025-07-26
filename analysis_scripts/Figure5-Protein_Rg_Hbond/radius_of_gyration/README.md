**Protein Radius of Gyration (Rg) Calculations (files: protein_dnatype_protein_rg.sh)**
-

Cpptraj scripts within bash script calculate Rg for the entire protein in each nucleosome (viral, eukaryote, truncated eukaryote) for both DNA types (widom 601 and alpha-satellite). 

Script first aligns the protein core residues to the first frame, then calculates the Rg of that histone core over the entire trajectory and looping over each replica.
Excludes first 100ns / 1000 frames of simulation in plotting to account for equilibration time. 

- Parmtop and trajectory files mentioned uploaded to Zenodo.
