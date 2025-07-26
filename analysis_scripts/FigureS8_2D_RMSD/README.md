**2D RMSD Viral Fused Histone Connector Calculations (files: protein_dnatype_connector.sh)**
-

Cpptraj scripts within bash script calculate the 2D RMSD for the histone connectors (H4-H3,H2B-H2A) found in the viral nucleosome for both DNA types (widom 601 and alpha-satellite). 

Script first strips the nuclecome trajectories of all residues but the fused histone (H4-H3 or H2B-H2A), and aligns the core residues of that each histone equivalent (H4/H3 or H2/H2A) to the first frame. Stripped parmtops are also created for that connector. This is repeated for both copies of the fused histone (of which there are two for each type).

The trajectories for both fused histones are aligned at the core residues of the fused histone and the 2D RMSD for the connector is calculated.
 

- Parmtop and trajectory files mentioned uploaded to Zenodo.
