#!/bin/bash


#Align at residue core
#RMSD for each histone type (H3,H4,H2A,H2B)
#Exclude 100ns of equilibration time



#Loop over 4 replicas
for i in {1..4}

do




cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :301-392&!@H= first
rms ToFirst :295-392&!@H= first out trunc_euk_alpha.rmsd.H3_A_$i.dat mass
go
clear all

parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :402-474&!@H= first
rms ToFirst :393-474&!@H= first out trunc_euk_alpha.rmsd.H4_B_$i.dat mass
go
clear all

parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :475-557&!@H= first
rms ToFirst :475-576&!@H= first out trunc_euk_alpha.rmsd.H2A_C_$i.dat mass
go
clear all

parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :585-672&!@H= first
rms ToFirst :577-673&!@H= first out trunc_euk_alpha.rmsd.H2B_D_$i.dat mass
go
clear all

parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :680-771&!@H= first
rms ToFirst :674-771&!@H= first out trunc_euk_alpha.rmsd.H3_E_$i.dat mass
go
clear all

parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :781-853&!@H= first
rms ToFirst :772-853&!@H= first out trunc_euk_alpha.rmsd.H4_F_$i.dat mass
go
clear all

parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :854-936&!@H= first
rms ToFirst :854-955&!@H= first out trunc_euk_alpha.rmsd.H2A_G_$i.dat mass
go
clear all

parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.nc 1001 last 1
autoimage
align :964-1051&!@H= first
rms ToFirst :956-1052&!@H= first out trunc_euk_alpha.rmsd.H2B_H_$i.dat mass
go
clear all
_EOF


done
