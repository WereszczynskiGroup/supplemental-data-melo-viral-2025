#!/bin/bash


#Aligned at protein core
#Radius of Gyration (Rg) for protein core residues





#Loop over 4 replicas
for i in {1..4}

do


cpptraj <<_EOF
parm euk_widom.prmtop
trajin euk_widom.run$i.xtc
autoimage
align :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first
radgyr Run$i :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= out euk_widom_protein_rg$i.dat nomax mass
go
clear all

_EOF


done
