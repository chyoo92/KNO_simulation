#!/bin/sh

# for J in `seq 1 1000`; do
#         for I in `seq 50 50 1000`; do
#                 /users/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/gen_loop.sh ${I} ${J}
#         done
# done


for J in `seq 1 2000`; do
        /users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/gen_loop.sh 500 ${J}
        
done

