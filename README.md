# For KNO MC generation
Based on https://github.com/WCSim/WCSim

In KHU Server Use wcsim.sif singularity image

## Install (KHU Server / use wcsim.sif)
    bash WCSim_KNO/make.sh


## Make .mac file
KNO_basic.mac / HK_basic.mac / SK_basic.mac \
Basic mac file in WCSim_v1.8.0-build/KNOmacros \
randomseed / energy / iter(filenum) auto change \
The macs_gen.sh file creates a file in the temp_macs folder by putting randomseed, energy, and iter in the file.
    
    bash macs_loop.sh ### loop macs_gen.sh

## Gen .root file
    ## basic run
    ~/WCSim_v1.8.0-build/WCSim ~/WCSim_v1.8.0-build/KNOmacros/temp_macs/mac_file.mac


KHU Server (use .sif file and slurm)

    bash sbatch_loop.sh