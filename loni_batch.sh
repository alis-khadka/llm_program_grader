#!/bin/bash
#SBATCH -N 1               # request one node
#SBATCH -t 2:00:00	        # request two hours
#SBATCH -p gpu2          # in single partition (queue)
#SBATCH -A loni_csc7135s25
#SBATCH -o slurm-%j.out-%N # optional, name of the stdout, using the job number (%j) and the hostname of the node (%N)
#SBATCH -e slurm-%j.err-%N # optional, name of the stderr, using job and hostname values
# below are job commands
date

# Set some handy environment variables.

# python run.py > log.txt
python run_1.py > log.txt

