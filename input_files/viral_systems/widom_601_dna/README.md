Viral Nucleosomes Starting Structures
-

Targeted MD was applied to guide the system toward a closed, fully wrapped conformation based on the 1KX5 structure.


Files for each DNA type are seperated into 3 folders with the following contents: 

Before_TMD
- Viral structure with built DNA (slightly open DNA configuration)
- Target widom 601 DNA conformation (from 1KX5 system)
- Target file but now aligned with the initial Viral structure.
  
Targeted_MD_sims
- prod.in file for TMD
- PDB used as reference for TMD (targeted_virus_widom.pdb)
- Job submission script
- Output file for last relaxation step before TMD was applied
- Output file for targeted md

After_TMD
- Final PDB structure used for nucleosome study (viral protein + widom 601 DNA)
- Solvated version of Final PDB structure
- rst7 file from TMD used to created PDB file
