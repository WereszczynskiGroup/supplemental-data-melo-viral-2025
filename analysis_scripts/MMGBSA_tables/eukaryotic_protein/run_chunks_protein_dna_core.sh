#!/bin/bash

# Load modules and Amber environment
module purge
module load gnu12/12.4.0 cuda/12
source /opt/ohpc/pub/apps/amber/amber24/amber.sh

# Define the base directory (same as in your first script)
base_dir="../mmgbsa/protein_dna_core"

# Loop over all chunk directories
for chunk_dir in ${base_dir}/chunk*; do
  chunk_name=$(basename $chunk_dir)

  # Create SLURM submission script
  cat > ${chunk_dir}/submit_${chunk_name}.slurm <<EOF
#!/bin/bash
#SBATCH --job-name=MMGBSA_${chunk_name}
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=high-mem
#SBATCH --output=slurm.out

module purge
module load gnu12/12.4.0 cuda/12
source /opt/ohpc/pub/apps/amber/amber24/amber.sh

echo "Amber24 Python version:"
/opt/ohpc/pub/apps/amber/amber24/miniconda/bin/python --version

echo "Running MMPBSA on ${chunk_name}"
/opt/ohpc/pub/apps/amber/amber24/bin/MMPBSA.py -O \
  -i decomp.in \\
  -eo per_residue_decomp_${chunk_name}.dat \\
  -o FINAL_RESULTS_MMPBSA_${chunk_name}.dat \\
  -cp com1.prmtop \\
  -rp rec1.prmtop \\
  -lp lig1.prmtop \\
  -y chunk${chunk_name:5:2}.xtc
EOF

  # Submit the job
  (cd $chunk_dir && sbatch submit_${chunk_name}.slurm)

  echo "Submitted job for ${chunk_name}"

done

