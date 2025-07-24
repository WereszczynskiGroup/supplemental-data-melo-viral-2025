#!/bin/sh
#COBALT -q single-gpu
#COBALT -n 1 
#COBALT -t 01:00:00 
#COBALT -A wereszczynski 
#COBALT -O targetedmd_vv_5.out
#COBALT --attrs filesystems=home,grand,theta-fs0


PRMTOP=hmr_testing3.prmtop
INPCRD=testing3_solvated.rst7
OUTPRE=virus_widom


sander -O -i prod.in    -o ${OUTPRE}_targetedmd.prod.01.out  -p $PRMTOP -c ${OUTPRE}.relax.7.rst7   -ref targeted_virus_widom.rst7    -r ${OUTPRE}_targetedmd.prod.01.rst7   -x ${OUTPRE}_targetedmd.prod.01.nc
