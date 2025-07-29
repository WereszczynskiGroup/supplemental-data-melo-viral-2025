#!/bin/bash


#Aligned at protein core
#Radius of Gyration (Rg) for protein core residues




#Loop over 4 replicas
for i in {1..4}

do


cpptraj <<_EOF
parm trunc_euk_widom.prmtop
trajin trunc_euk_widom.run$i.xtc
autoimage
align :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first
radgyr Rg :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= out trunc_euk_widom_protein_rg$i.dat nomax mass
go
clear all

_EOF


done
