#!/bin/bash


#Aligned at protein core
#Radius of Gyration (Rg) for protein core residues



#Loop over 4 replicas
for i in {1..4}

do


cpptraj <<_EOF
parm virus_widom.prmtop
trajin virus_widom.run$i.xtc
autoimage
align :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first
radgyr Run$i :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= out virus_widom_protein_rg$i.dat nomax mass
go
clear all

_EOF


done
