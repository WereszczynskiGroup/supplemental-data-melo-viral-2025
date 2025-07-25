#!/bin/bash


module load cuda/12 amber/24




cpptraj <<_EOF
parm virus_alpha.prmtop
trajin virus_alpha.run1.xtc 1 last 10
trajin virus_alpha.run2.xtc 1 last 10
trajin virus_alpha.run3.xtc 1 last 10
trajin virus_alpha.run4.xtc 1 last 10
strip !(:503-680&!@CA,C,O,N,H=)
align :1-88,96-178 first
trajout H2B_H2A_en_con.xtc
run
quit
_EOF


cpptraj <<_EOF
parm virus_alpha.prmtop
trajin virus_alpha.run1.xtc 1 last 10
trajin virus_alpha.run2.xtc 1 last 10
trajin virus_alpha.run3.xtc 1 last 10
trajin virus_alpha.run4.xtc 1 last 10
strip !(:902-1079&!@CA,C,O,N,H=)
align :1-88,96-178 first
trajout H2B_H2A_ex_con.xtc
run
quit
_EOF



cpptraj <<_EOF
parm virus_alpha.prmtop
parmstrip !(:902-1079&!@CA,C,O,N,H=)
parmwrite connector_H2B_H2A.prmtop
go
_EOF




parm connector_H2B_H2A.prmtop
trajin H2B_H2A_en_con.xtc
trajin H2B_H2A_ex_con.xtc
align :1-88,96-178 first 
rms2d :89-95 out alpha_H2B_H2A_rms2d.dat mass
go
clear all
_EOF
