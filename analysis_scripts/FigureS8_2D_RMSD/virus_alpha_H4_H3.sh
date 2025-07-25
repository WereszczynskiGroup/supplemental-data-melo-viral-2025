#!/bin/bash


module load cuda/12 amber/24




cpptraj <<_EOF
parm virus_alpha.prmtop
trajin virus_alpha.run1.xtc 1 last 10
trajin virus_alpha.run2.xtc 1 last 10
trajin virus_alpha.run3.xtc 1 last 10
trajin virus_alpha.run4.xtc 1 last 10
strip !(:704-890&!@CA,C,O,N,H=)
align :1-73,96-187 first 
trajout H4_H3_en_con.xtc
run
quit
_EOF


cpptraj <<_EOF
parm virus_alpha.prmtop
trajin virus_alpha.run1.xtc 1 last 10
trajin virus_alpha.run2.xtc 1 last 10
trajin virus_alpha.run3.xtc 1 last 10
trajin virus_alpha.run4.xtc 1 last 10
strip !(:305-491&!@CA,C,O,N,H=)
align :1-73,96-187 first 
trajout H4_H3_ex_con.xtc
run
quit
_EOF



cpptraj <<_EOF
parm virus_alpha.prmtop
parmstrip !(:305-491&!@CA,C,O,N,H=)
parmwrite connector_H4_H3.prmtop
go
_EOF




cpptraj <<_EOF
parm connector_H4_H3.prmtop
trajin H4_H3_en_con.xtc
trajin H4_H3_ex_con.xtc
align :1-73,96-187 first
rms2d :74-95 out alpha_H4_H3_rms2d.dat mass
go
clear all
_EOF
