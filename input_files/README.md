# Input Files

This directory contains files and scripts used to generate the molecular system and prepare it for simulation.

Contents include:
- All-Atom initial PDB files for each system
- Protein: Viral, Eukaryotic, Truncated Eukaryotic Protein; DNA: Widom 601 + Alpha-Satellite DNA
- Files necessary to achieve starting viral nucleosome structure (sequence coordinates, TargetedMD)
- Amber input files (Conventional All Atom + Targeted MD)
- Solvation and ionization script (tleap)

Simulations utilized Amber package for simulations and data analysis, All systems were constructed in tleap with OPC water model box (size ~200x200x200 to accomodate for DNA unwrapping without periodic images), and neutralized with Na+ and Cl– to a final ionic strength of 150 mM NaCl. Nucleosome systems use BSC1 force fields for DNA and ff19SB for protein. Hydrogen mass repartitioning was applied to enable the use of a 4 fs time step.
