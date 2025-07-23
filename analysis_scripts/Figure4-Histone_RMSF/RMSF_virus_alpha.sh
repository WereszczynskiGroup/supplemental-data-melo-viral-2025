#!/bin/bash


#Align at residue core
#RMSF for each histone core (H3,H4,H2A,H2B)
#Exclude 100ns of equilibration time



#Loop over 4 replicas
for i in {1..4}

do




cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :305-377&!@H= byres out virus_alpha.rmsf.H4_A_$i.dat
_EOF

cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :400-491&!@H= byres out virus_alpha.rmsf.H3_A_$i.dat
_EOF


cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :503-590&!@H= byres out virus_alpha.rmsf.H2B_B_$i.dat
_EOF


cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :598-680&!@H= byres out virus_alpha.rmsf.H2A_B_$i.dat
_EOF

cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :704-776&!@H= byres out virus_alpha.rmsf.H4_C_$i.dat
_EOF

cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :799-890&!@H= byres out virus_alpha.rmsf.H3_C_$i.dat
_EOF

cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :902-989&!@H= byres out virus_alpha.rmsf.H2B_D_$i.dat
_EOF

cpptraj <<_EOF
parm virus_alpha.run$i.prmtop
trajin virus_alpha.run$i.xtc 1001 last 1
autoimage
rms Run1 :305-377,400-491,503-590,598-680,704-776,799-890,902-989,997-1079&!@H= first 
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :997-1079&!@H= byres out virus_alpha.rmsf.H2A_D_$i.dat
_EOF


done
