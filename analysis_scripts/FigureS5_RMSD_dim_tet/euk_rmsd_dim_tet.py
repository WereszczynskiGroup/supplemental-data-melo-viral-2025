#!/bin/bash

##Aligned at tetramer core residues
#RMSD deviation of each Dimer from the Tetramer


#Loop over 4 replicas
for i in {1..4}

do





cpptraj <<_EOF
parm euk_widom.prmtop
trajin euk_widom.run$i.xtc
autoimage
align :459-531,338-429,946-1018,825-916&!@H= first
rms ToFirst :693-780,547-629&!@H= first out euk_widom.rmsd.H2B_H2A_dim1_$i.dat mass
go
clear all

parm euk_widom.prmtop
trajin euk_widom.run$i.xtc
autoimage
align :459-531,338-429,946-1018,825-916&!@H= first
rms ToFirst :1180-1267,1034-1116&!@H= first out euk_widom.rmsd.H2B_H2A_dim2_$i.dat mass
go
clear all

_EOF




cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc
autoimage
align :459-531,338-429,946-1018,825-916&!@H= first
rms ToFirst :693-780,547-629&!@H= first out euk_alpha.rmsd.H2B_H2A_dim1_$i.dat mass
go
clear all

parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc
autoimage
align :459-531,338-429,946-1018,825-916&!@H= first
rms ToFirst :1180-1267,1034-1116&!@H= first out euk_alpha.rmsd.H2B_H2A_dim2_$i.dat mass
go
clear all

_EOF




done
