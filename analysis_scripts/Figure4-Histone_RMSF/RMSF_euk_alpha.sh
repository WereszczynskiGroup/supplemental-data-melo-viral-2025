#!/bin/bash


#Align at residue core
#RMSF for each histone core (H3,H4,H2A,H2B)
#Exclude 100ns of equilibration time



#Loop over 4 replicas
for i in {1..4}

do




cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :338-429&!@H= byres out euk_alpha.rmsf.H3_A_$i.dat
_EOF


cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :459-531&!@H= byres out euk_alpha.rmsf.H4_B_$i.dat
_EOF


cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :547-629&!@H= byres out euk_alpha.rmsf.H2A_C_$i.dat
_EOF

cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :693-780&!@H= byres out euk_alpha.rmsf.H2B_D_$i.dat
_EOF

cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :825-916&!@H= byres out euk_alpha.rmsf.H3_E_$i.dat
_EOF

cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :946-1018&!@H= byres out euk_alpha.rmsf.H4_F_$i.dat
_EOF

cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :1034-1116&!@H= byres out euk_alpha.rmsf.H2A_G_$i.dat
_EOF

cpptraj <<_EOF
parm euk_alpha.prmtop
trajin euk_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :338-429,459-531,547-629,693-780,825-916,946-1018,1034-1116,1180-1267&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :1180-1267&!@H= byres out euk_alpha.rmsf.H2B_H_$i.dat
_EOF


done
