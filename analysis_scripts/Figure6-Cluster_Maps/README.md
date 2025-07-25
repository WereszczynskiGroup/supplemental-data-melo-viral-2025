**Viral Fused Histone Connector - DBSCAN Cluster Conformational Analysiss**


These scripts can be used to analyze conformations of the H4-H3 connector from the fused viral histones. This is done by organizing the trajectory frames by the number of basepairs unwrapped at that side of the nucleosome (Entry/Exit) and performing DBSCAN analyses collectively on the connector sidechains. This sets the system up for dominant conformation comparisons as DNA unwrapping progresses in this system by DNA arm, useful for a system with asymmetric DNA fluctuations.

Starting files:
- Loads simulation frames in order of DNA Unwrapped stages (0-5,6-10,11-15,16-20,21-25,26-30bp)
- Frame order predetermined from Base pair unwrapping script for Figure1
- Creates trajectory files for H4-H3.1 connector in order of Entry DNA unwrapped stages and H4-H3.2 in Exit DNA unwrapped stages
- Creates parmtop for H4-H3 connector residues

DBSCAN clustering analysis file:
- Cpptraj first aligns the H4/H3 portion of the fused histone
- Parameter selection, splits the frames into predetermined Unwrapped DNA Stages, first Entry unwrapped 0-30bp, then Exit unwrapping from 0-26bp in 5bp increments. 
