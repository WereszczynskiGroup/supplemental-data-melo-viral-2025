#!/bin/bash


#Align at residue core
#RMSF for each histone core (H3,H4,H2A,H2B)
#Exclude 100ns of equilibration time



#Loop over 4 replicas
for i in {1..4}

do




cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :301-392&!@H= byres out trunc_euk_alpha.rmsf.H3_A_$i.dat
_EOF


cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :402-474&!@H= byres out trunc_euk_alpha.rmsf.H4_B_$i.dat
_EOF


cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :475-557&!@H= byres out trunc_euk_alpha.rmsf.H2A_C_$i.dat
_EOF

cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :585-672&!@H= byres out trunc_euk_alpha.rmsf.H2B_D_$i.dat
_EOF

cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :680-771&!@H= byres out trunc_euk_alpha.rmsf.H3_E_$i.dat
_EOF

cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :781-853&!@H= byres out trunc_euk_alpha.rmsf.H4_F_$i.dat
_EOF

cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :854-936&!@H= byres out trunc_euk_alpha.rmsf.H2A_G_$i.dat
_EOF

cpptraj <<_EOF
parm trunc_euk_alpha.run$i.prmtop
trajin trunc_euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :301-392,402-474,475-557,585-672,680-771,781-853,854-936,964-1051&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :964-1051&!@H= byres out trunc_euk_alpha.rmsf.H2B_H_$i.dat
_EOF


done
