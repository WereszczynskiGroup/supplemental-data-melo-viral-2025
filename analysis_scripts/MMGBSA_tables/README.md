**MM/GBSA Binding Free Energy Calculations**
-

The scripts located inside each protein type folder can be used to set up and calculate the binding free energy between segments within the nucleosome structure (viral, eukaryotic, truncated eukaryotic) with either DNA sequence (widom 601 or alpha-satellite dna). The initial files assign a set of residues as the "ligand" and another as the "receptor", as part of the complex structure in the single-trajectory approach for MM/GBSA calculations.

Starting (Initial) files:
- Bash script initially divides the trajectory frames into chunks dependent to use the computational resources efficiency.
- Creates receptor, ligand, and complex prmtops using cpptraj parmstrip (Example: Receptor-Protein residues; Ligand-Nucleic residues; Complex: Both receptor and ligand residues)
- Creates and moves files to chunk directories.

Run (Submission) files:
- Creates slurm files, copies them to the chunk directories, and submits all simulations to resources of choice to run
- Outputs decomposition file that breaks energetics down by residue, and energy type (van der Waals, electrostatics, total energy) - for chunks (combine in additional script)

Script in results folder contain scripts to calculate the energetics of the entire simulation (as it was seperated by chunks) combined.

 

- Parmtop and trajectory files mentioned uploaded to Zenodo.
