#!/bin/bash

#SBATCH -p normal
#SBATCH --nodes=1              
#SBATCH --cpus-per-task=3
#SBATCH --ntasks-per-node=1

iter=$SLURM_ARRAY_TASK_ID

echo "start"

energy=$1


singularity run -B /store/sw/hep/geant4-data:/hep-sw/geant4/share/Geant4/data /users/hep/yewzzang/wcsim.sif <<EOF
export WCSIMDIR=/users/hep/yewzzang/WCSim_KNO/WCSim_KNO/
export G4WORKDIR=$WCSIMDIR/exe
export G4INSTALLDIR=/hep-sw/geant4
source $G4INSTALLDIR/bin/geant4.sh
source $G4INSTALLDIR/share/Geant4-10.7.4/geant4make/geant4make.sh
cd /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build

/users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/WCSim /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/KNOmacros/temp_macs/mu_khu_${iter}_${energy}.mac
/users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/WCSim /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/KNOmacros/temp_macs/mu_khu_${iter}_${energy}_nodark.mac
EOF

