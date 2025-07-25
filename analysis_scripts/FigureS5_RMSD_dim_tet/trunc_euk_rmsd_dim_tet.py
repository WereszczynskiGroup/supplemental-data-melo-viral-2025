#!/bin/bash

##Aligned at tetramer core residues
#RMSD deviation of each Dimer from the Tetramer


#Loop over 4 replicas
for i in {1..4}

do





cpptraj <<_EOF
parm trunc_euk_widom.prmtop
trajin trunc_euk_widom.run$i.xtc
autoimage
align :402-474,301-392,781-853,680-771&!@H= first
rms ToFirst :585-672,475-557&!@H= first out trunc_euk_widom.rmsd.H2B_H2A_dim1_$i.dat mass
go
clear all

parm trunc_euk_widom.prmtop
trajin trunc_euk_widom.run$i.xtc
autoimage

align :402-474,301-392,781-853,680-771&!@H= first
rms ToFirst :964-1051,854-936&!@H= first out trunc_euk_widom.rmsd.H2B_H2A_dim2_$i.dat mass
go
clear all

_EOF






cpptraj <<_EOF
parm trunc_euk_alpha.prmtop
trajin trunc_euk_alpha.run$i.xtc
autoimage
align :402-474,301-392,781-853,680-771&!@H= first
rms ToFirst :585-672,475-557&!@H= first out trunc_euk_alpha.rmsd.H2B_H2A_dim1_$i.dat mass
go
clear all

parm trunc_euk_alpha.prmtop
trajin trunc_euk_alpha.run$i.xtc
autoimage

align :402-474,301-392,781-853,680-771&!@H= first
rms ToFirst :964-1051,854-936&!@H= first out trunc_euk_alpha.rmsd.H2B_H2A_dim2_$i.dat mass
go
clear all

_EOF


done
