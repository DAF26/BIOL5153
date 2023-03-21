#!/dadean/bin/env python3

# Set variables

#Job name variable
job_name = 'my_a4_job'

#Queue variable
queue = 'comp72'

#Node variable
num_nodes = 1

#Number of processor variable
num_processors = 4

#Amount of walltime variable
walltime = '00:10:00'


# Print SLURM script to STDOUT

print("#!/bin/bash")

print(f"#SBATCH --job-name={job_name}")

print(f"#SBATCH --partition={queue}")

print(f"#SBATCH --nodes={num_nodes}")

print(f"#SBATCH --ntasks-per-node={num_processors}")

print(f"#SBATCH --time={walltime}")
