#!/bin/bash

#PBS -N get-hostname
#PBS -l select=1:ncpus=1:interconnect=1g
#PBS -l walltime=00:02:00
#PBS -j oe
#PBS -J 1-2

cd $PBS_O_WORKDIR

inputs=( $(sed -n ${PBS_ARRAY_INDEX}p inputs.txt) )

ssh -p 22 bpyle@aptvm${inputs[0]}-3.apt.emulab.net "hostname;"


#./quadratic.py ${inputs[0]} ${inputs[1]} ${inputs[2]}
