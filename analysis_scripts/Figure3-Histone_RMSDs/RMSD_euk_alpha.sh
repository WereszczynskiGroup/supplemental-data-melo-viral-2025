#!/bin/bash


#Align at residue core
#RMSD for each histone type (H3,H4,H2A,H2B)
#Exclude 100ns of equilibration time



#Loop over 4 replicas
for i in {1..4}

do




cpptraj <<_EOF
parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :338-429&!@H= first
rms ToFirst :332-429 first out euk_alpha.rmsd.H3_A_$i.dat mass
go
clear all

parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :459-531&!@H= first
rms ToFirst :450-531 first out euk_alpha.rmsd.H4_B_$i.dat mass
go
clear all

parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :547-629&!@H= first
rms ToFirst :547-648 first out euk_alpha.rmsd.H2A_C_$i.dat mass
go
clear all

parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :693-780&!@H= first
rms ToFirst :685-781 first out euk_alpha.rmsd.H2B_D_$i.dat mass
go
clear all

parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :825-916&!@H= first
rms ToFirst :819-916 first out euk_alpha.rmsd.H3_E_$i.dat mass
go
clear all

parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :946-1018&!@H= first
rms ToFirst :937-1018 first out euk_alpha.rmsd.H4_F_$i.dat mass
go
clear all

parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :1034-1116&!@H= first
rms ToFirst :1034-1135 first out euk_alpha.rmsd.H2A_G_$i.dat mass
go
clear all

parm euk_alpha.run$i.prmtop
trajin euk_alpha.run$i.nc 1001 last 1
autoimage
align :1180-1267&!@H= first
rms ToFirst :1172-1268 first out euk_alpha.rmsd.H2B_H_$i.dat mass
go
clear all
_EOF



done
