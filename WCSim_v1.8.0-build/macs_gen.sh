#!/bin/bash -l

#echo "WCSim_KNO running"

mom=$1
itr=$2
seed=$RANDOM

cd $WCSIMBASE

sed -e "s/MOMMM/${mom}/;s/ITTER/${itr}/;s/SEEDDD/${seed}/" /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/KNOmacros/mu_khu_500MeV.mac > /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/KNOmacros/temp_macs/mu_khu_${itr}_${mom}.mac
sed -e "s/MOMMM/${mom}/;s/ITTER/${itr}/;s/SEEDDD/${seed}/" /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/KNOmacros/mu_khu_500MeV_nodark.mac > /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/KNOmacros/temp_macs/mu_khu_${itr}_${mom}_nodark.mac

#sed -e "s/MOMMM/${mom}/;s/ITTER/${itr}/" /home/chyoo/tool/WCSim_v1.8.0-build/run_elec.sh > /home/chyoo/tool/WCSim_v1.8.0-build/temp_runner/run_elec_${itr}_${mom}.sh
#chmod +x /home/chyoo/tool/WCSim_v1.8.0-build/temp_runner/run_elec_${itr}_${mom}.sh

