#!/bin/bash

Benchmarks=$1
EXE=${Benchmarks}

grep 'PWR_PKG_ENERGY STAT
PWR_DRAM_ENERGY STAT
FP_ARITH_INST_RETIRED_DOUBLE STAT
MEM_LOAD_RETIRED_L3_MISS STAT' $EXE > PMC_${EXE}

awk '{print $2 " " $7}' PMC_${EXE} > PMCs_${EXE}

rm PMC_${EXE}

