#!/bin/sh

for I in `seq 50 50 1000`; do
    sbatch -a [1-70] -J K_gamma -o slurm_log/K_${I}.out sbatch.sh ${I}
done

sbatch -a [1-1000] -J KNO_2 -o slurm_log/K_500.out sbatch.sh 500

