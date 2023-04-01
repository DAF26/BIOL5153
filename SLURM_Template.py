#!/dadean/bin/env python3

# import modules 

import argparse

# creating an ArgumentParser object

parser = argparse.ArgumentParser(description="The following are the positional and optional arguments for this slurm script")

# add positional (required) arguments

parser.add_argument("job_name", help= "The name of the job you are running")

# add optional arguments

parser.add_argument("-v", "--verbose", help="Print verbose output",
	action = 'store_true')
	
parser.add_argument("--queue", help= "The name of the queue you would like to use")

parser.add_argument("--nodes", help= "The amount of nodes you would like to run", type=int)

parser.add_argument("--processors", help= "The amount of processors you would like to use", type=int)

parser.add_argument("--Walltime", help= "The amount of walltime you would like to use")

# parse the actual arguments

args = parser.parse_args()


# Set variables

#Job name variable
job_name = args.job_name

#Queue variable
queue = args.queue

#Node variable
num_nodes = args.nodes

#Number of processor variable
num_processors = args.processors

#Amount of walltime variable
walltime = args.walltime

# Default values if not provided by user
if queue is None:
    queue = 'comp72'

if num_nodes is None:
    num_nodes = 1

if num_processors is None:
    num_processors = 1

if walltime is None:
    walltime = '00:60:00'

# Print SLURM script to STDOUT

print("#!/bin/bash")

print(f"#SBATCH --job-name={job_name}")

print(f"#SBATCH --partition={queue}")

print(f"#SBATCH --nodes={num_nodes}")

print(f"#SBATCH --ntasks-per-node={num_processors}")

print(f"#SBATCH --time={walltime}")

print(f"#SBATCH -o %j.out")

print(f"#SBATCH -e %j.err")

print(f"#SBATCH --mail-type=ALL")

print(f"#SBATCH --mail-user=dadean@uark.edu")

print(f"cd $SLURM_SUBMIT_DIR")


# Commands Below










