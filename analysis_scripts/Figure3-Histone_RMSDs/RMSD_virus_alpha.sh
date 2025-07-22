#!/bin/bash


#Align at residue core
#RMSD for each histone type (H3,H4,H2A,H2B)
#Exclude 100ns of equilibration time



#Loop over 4 replicas
for i in {1..4}

do




cpptraj <<_EOF


parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :305-377&!@H= first
rms ToFirst :295-377&!@H= first out virus_alpha.rmsd.H4_A_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :400-491&!@H= first
rms ToFirst :400-491&!@H= first out virus_alpha.rmsd.H3_A_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :503-590&!@H= first
rms ToFirst :492-590&!@H= first out virus_alpha.rmsd.H2B_B_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :598-680&!@H= first
rms ToFirst :598-693&!@H= first out virus_alpha.rmsd.H2A_B_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :704-776&!@H= first
rms ToFirst :694-776&!@H= first out virus_alpha.rmsd.H4_C_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :799-890&!@H= first
rms ToFirst :799-890&!@H= first out virus_alpha.rmsd.H3_C_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :902-989&!@H= first
rms ToFirst :891-989&!@H= first out virus_alpha.rmsd.H2B_D_$i.dat mass
go
clear all

parm virus_alpha.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
align :997-1079&!@H= first
rms ToFirst :997-1092&!@H= first out virus_alpha.rmsd.H2A_D_$i.dat mass
go
clear all
_EOF


done
