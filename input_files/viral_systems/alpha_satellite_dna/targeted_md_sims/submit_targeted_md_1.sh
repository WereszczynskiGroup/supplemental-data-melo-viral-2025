#!/bin/sh
#COBALT -q single-gpu
#COBALT -n 1 
#COBALT -t 01:00:00 
#COBALT -A wereszczynski 
#COBALT -O targetedmd_v1_1.out
#COBALT --attrs filesystems=home,grand,theta-fs0


PRMTOP=hmr_testing2.prmtop
INPCRD=testing2_solvated.rst7
OUTPRE=virus_alpha


sander -O -i prod.in    -o ${OUTPRE}_targetedmd.prod.01.out  -p $PRMTOP -c ${OUTPRE}.relax.7.rst7   -ref targeted_virus_alpha.rst7    -r ${OUTPRE}_targetedmd.prod.01.rst7   -x ${OUTPRE}_targetedmd.prod.01.nc
