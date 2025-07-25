**Angular movement of dimers relative to tetramer in nucleosome core. (files:angle_protein_dnatype_dimer.py )**

This script can be used for calculations of dimer angular displacements relative to the H4–H3 tetramer, in turn quantifying dynamic changes to the histone core arrangement. 

Using MDAnalysis, the script creates vectors representing the orientation of the tetramer helices and dimer helices, using dot product definitions to calculate the angle between the subunits. This is calculated for both dimers movement from the tetramer, and can be modified for other motion calculations.

- Parmtop and trajectory files mentioned uploaded to Zenodo.

Packages used: MDAnalysis, numpy, os
