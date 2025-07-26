**Base pair Unwrapping Calculations**
-

This script can be used to calculate the total number of basepairs unwrapped in a nucleosome simulation as well as seperate the basepair unwrapped counts by DNA sites (Entry and Exit DNA).


Two requirements for a basepair to be considered unwrapped in this script:
1. RMSD of >7 Angstroms from basepair starting position 
2. Loss of contact with protein ( >4.5 Angstroms away)


MDAnalysis is used to calculate the RMSD of each basepair from its starting position in a timeseries. (RMSDs <7 Angstroms = wrapped, >7 = unwrapped)


Definition for loss of protein contact within MDAnalysis are defined, using contacts function and cutoff radius of 4.5 Angstroms




Packages used:
matplotlib, pandas, numpy, MDAnalysis
