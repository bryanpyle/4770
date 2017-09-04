#PBS -N gnu-parallel-example
#PBS -l select=5:ncpus=4:mem=1gb,walltime=00:05:00
#PBS -j oe
module add gnu-parallel

cd $PBS_O_WORKDIR
cat $PBS_NODEFILE > nodes.txt
ls ./inputs/* | parallel --sshloginfile nodes.txt -j4 'module add anaconda3/4.2.0; cd /home/bpyle/cpsc4770/assignment2/GNU-Parallel; python transpose.py {}'
rm nodes.txt
