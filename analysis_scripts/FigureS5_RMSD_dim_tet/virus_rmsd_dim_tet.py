#!/bin/bash

##Aligned at tetramer core residues
#RMSD deviation of each Dimer from the Tetramer


#Loop over 4 replicas
for i in {1..4}

do


cpptraj <<_EOF
parm virus_widom.prmtop
trajin virus_widom.run$i.xtc
autoimage
align :305-377,400-491,704-776,799-890&!@H= first
rms ToFirst :503-590,598-680&!@H= first out virus_widom.rmsd.H2B_H2A_dim1_$i.dat mass
go
clear all

parm virus_widom.prmtop
trajin virus_widom.run$i.xtc
autoimage
align :305-377,400-491,704-776,799-890&!@H= first
rms ToFirst :902-989,997-1079&!@H= first out virus_widom.rmsd.H2B_H2A_dim2_$i.dat mass
go
clear all

_EOF



cpptraj <<_EOF
parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc
autoimage
align :305-377,400-491,704-776,799-890&!@H= first
rms ToFirst :503-590,598-680&!@H= first out virus_alpha.rmsd.H2B_H2A_dim1_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc
autoimage
align :305-377,400-491,704-776,799-890&!@H= first
rms ToFirst :902-989,997-1079&!@H= first out virus_alpha.rmsd.H2B_H2A_dim2_$i.dat mass
go
clear all

_EOF

done
