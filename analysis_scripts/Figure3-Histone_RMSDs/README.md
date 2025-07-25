**Histone RMSD Calculations (files: RMSD_protein_dna_type.sh)**

Cpptraj scripts within bash script calculate RMSD for each histone (H4,H3,H2A,H2B) within each nucleosome type (viral, eukaryote, truncated eukaryote) for both DNA types (widom 601 and alpha-satellite). 

Script first aligns each histone core residues to the first frame, then calculates the RMSD of that histone over the entire trajectory and looping over each replica.
Excludes first 100ns / 1000 frames of simulation to account for equilibration time. 

Files parmtop and trajectory files mentioned uploaded to Zenodo.

%
%
%

**Average RMSD python script**

To calculate the average RMSD for a histone, run the "Avg_RMSD.py" file in python and follow the prompts asking for the inputs associated with the protein_dnatype (as the prefix) and histone_chain (as the middle).

protein (virus, euk, trunc_euk)  ;  dnatype (widom, alpha)  ;   histone (H4,H3,H2A,H2B)  ;  chain (A-G for euk/trunc euk, A-D for virus)

The resulting output file contains the average Histone RMSD across all replicas, standard deviation, and standard error. 
