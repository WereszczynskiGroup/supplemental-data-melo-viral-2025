#!/bin/bash

# Load your modules
module purge
module load gnu12/12.4.0 cuda/12

# Source Amber environment
source /opt/ohpc/pub/apps/amber/amber24/amber.sh

dna_type=widom #alpha

# Define parent directory for chunk directories
base_dir="../mmgbsa/H2B_H2A_tail_dna"
mkdir -p $base_dir
echo "Chunks and trajectories will be created in $base_dir"

# Total chunks per run
chunks_per_run=5
frames_per_chunk=4000

# Loop over 4 runs
for i in {1..4}; do
  cp euk_${dna_type}.prmtop euk_${dna_type}.run${i}.prmtop
  prmtop="euk_${dna_type}.run${i}.prmtop"
  traj="euk_${dna_type}.run${i}.xtc"

  #Make a temporary directory to hold stripped prmtops for this run
  tmpdir="H2B_H2A_tail_dna_prmtops${i}"
  mkdir -p ${tmpdir}

  # Make receptor trajectory
  cpptraj <<_EOF
parm $prmtop
parmstrip !(:338-429,459-531,532-781,825-916,946-1018,1019-1268)
parmwrite out ${tmpdir}/rec1.prmtop
go
_EOF

  # Make ligand trajectory
  cpptraj <<_EOF
parm $prmtop
parmstrip !(:1-294)
parmwrite out ${tmpdir}/lig1.prmtop
go
_EOF

  # Make complex trajectory
  cpptraj <<_EOF
parm $prmtop
parmstrip !(:1-294,338-429,459-531,532-781,825-916,946-1018,1019-1268)
parmwrite out ${tmpdir}/com1.prmtop
go
_EOF

# Now split the complex trajectory into 4000-frame chunks
  for j in $(seq 1 $chunks_per_run); do
    # Global chunk number across all runs
    chunk=$(( (i-1)*chunks_per_run + j ))
    chunk_dir="${base_dir}/chunk$(printf "%02d" ${chunk})"
    mkdir -p $chunk_dir

    # Calculate start and end frames for this chunk (1-based)
    startframe=$(( (j-1)*frames_per_chunk + 1 ))
    endframe=$(( j*frames_per_chunk ))

    echo "Run ${i} — extracting frames $startframe to $endframe into $chunk_dir"
    cpptraj <<EOF
parm $prmtop
trajin ${traj} ${startframe} ${endframe}
strip !(:1-294,338-429,459-531,532-781,825-916,946-1018,1019-1268)
trajout ${chunk_dir}/chunk$(printf "%02d" ${chunk}).xtc
go
EOF

    # Optionally copy prmtops and decomp.in into chunk dir
     cp decomp.in $chunk_dir/
     cp ${tmpdir}/com1.prmtop $chunk_dir/com1.prmtop
     cp ${tmpdir}/rec1.prmtop $chunk_dir/rec1.prmtop
     cp ${tmpdir}/lig1.prmtop $chunk_dir/lig1.prmtop

  done
done
