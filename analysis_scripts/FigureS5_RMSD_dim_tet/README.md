**RMSD of H2B–H2A dimers relative to H4–H3 tetramer Calculations (files: protein_rmsd_dim_tet.py)**

Cpptraj scripts within bash script calculate RMSD for dimer subunit (H2B-H2A) within each nucleosome type (viral, eukaryote, truncated eukaryote) aligned at the tetramer for both DNA types (widom 601 and alpha-satellite). 

Script first aligns each the tetramer subunit core residues to the first frame, then calculates the RMSD of each dimer subunit over the entire trajectory and looping over each replica.

- Parmtop and trajectory files mentioned uploaded to Zenodo.
