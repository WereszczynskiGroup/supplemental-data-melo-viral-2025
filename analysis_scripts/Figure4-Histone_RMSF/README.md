**Histone RMSF Calculations (files: RMSF_protein_dnatype.sh)**

Cpptraj scripts within bash script calculate RMSF for each histone (H4,H3,H2A,H2B) within each nucleosome type (viral, eukaryote, truncated eukaryote) for both DNA types (widom 601 and alpha-satellite). 

Script first aligns each histone core residues to the first frame, then calculates the RMSF of that histone core over the entire trajectory and looping over each replica.
Excludes first 100ns / 1000 frames of simulation to account for equilibration time. 

- Parmtop and trajectory files mentioned uploaded to Zenodo.


**Average RMSF calculations (files: avg_rmsf_protein_dnatype.sh)**

To calculate the average RMSF for each histone residue, run the provided bash script that uses Cpptraj to read the rmsf data generated from the previous script for each histone type. Output contains averages of the residues across replicas with standard error calculated.
