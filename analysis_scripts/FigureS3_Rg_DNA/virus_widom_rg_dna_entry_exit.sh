#!/bin/bash

#Align protein
#Radius of gyration for each DNA end (Entry & Exit)



#Loop over 4 replicas
for i in {1..4}

do



cpptraj <<_EOF
parm virus_widom.prmtop
trajin virus_widom.run$i.nc
autoimage
rms Run$i :295-1092&!@H= first 
radgyr :1-73,222-294&!@H= out virus_widom_rg_dna.entry$i.dat  mass nomax
go
clear all

parm virus_widom.prmtop
trajin virus_widom.run$i.nc
autoimage
rms Run$i :295-1092&!@H= first 
radgyr :75-147,148-220&!@H= out virus_widom_rg_dna.exit$i.dat mass nomax
go
clear all
_EOF


done
