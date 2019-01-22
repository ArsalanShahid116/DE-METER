'''A wrapper using Likwid tool to calculate the base power consumption of
socket and DRAM using RAPL for given applications running on specified nu-
mber of cores on an Intel processor running Linux OS.
'''
#######################################################################
# Licence
#######################################################################

"""
Copyright 2001-2018 Heterogeneous Computing Laboratory,
School of Computer Science, University College Dublin

Redistribution and use in source and binary forms,
with or without modification, are permitted provided
that the following conditions are met:

     1. Redistributions of source code must retain the
     above copyright notice, this list of conditions
     and the following disclaimer.

     2. Redistributions in binary form must reproduce the
     above copyright notice, this list of conditions and
     the following disclaimer in the documentation and/or
     other materials provided with the distribution.

     3. Neither the name of the copyright holder nor the names
     of its contributors may be used to endorse or promote
     products derived from this software without specific
     prior written permission.

     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
     AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
     IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
     ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
     LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
     CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
             SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
             INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
     CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
     ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
     THE POSSIBILITY OF SUCH DAMAGE.
     """

__author__      = "Arsalan Shahid <arsalan.shahid@ucdconnect.ie>"
__copyright__   = "Copyright 2001-2019, HCL Laboratory"
__version__     = "1.0"

#######################################################################

from read_energy_pmcs import read_energy_pmcs
from chk_var import check_varience
from calc_mean import calc_mean
import os
import numpy as np
import sys

#######################################################################
#Input command line arguments and initialize variables
#######################################################################

iterations = 0
varDesired = 0
verbosity = 0
arguments = len(sys.argv)
if (arguments != 4):
    print("\n Execute: \n # python ./get_energy <desired_varience (1-\
100)> <max_iterations> <verbosity (1 || 2)")
else:
    varDesired = float(sys.argv[1])
    iterations = int(sys.argv[2])
    verbosity = int(sys.argv[3])

#######################################################################
# Clear previous files
#######################################################################

if (verbosity == 1):
    print("Removing previous outputs")
clearFiles = "rm PMCs_* sleep_*"
os.system(clearFiles)

iter = 0
listEnergy = []
results = [[0],[0]]
meanEnergy = 0.0
varience = 0.0 

#######################################################################
# Likwid Parameters
#######################################################################

likwid = "likwid-perfctr -f"
cores = "0-43" # specify core to monitor PMCs
energyPmcs = "PWR_PKG_ENERGY:PWR0,PWR_DRAM_ENERGY:PWR3"
applicationSpecPmcs = "FP_ARITH_INST_RETIRED_DOUBLE:PMC0,MEM_LOAD_RETI\
RED_L3_MISS:PMC3"

#######################################################################
# Collect PMCs and calculate base power
#######################################################################

while (iter < iterations):
    # Sleep system for one second
    application = "sleep 1"
    runLikwid = "%s -c %s -g %s,%s %s >> sleep_%s"%(likwid,cores, \
    energyPmcs,applicationSpecPmcs,application,iter)
    os.system(runLikwid)
    # Extract PMCs from Likwid output file
    extractPmcs = "./extract.sh sleep_%s"%(iter)
    os.system(extractPmcs)
    # Read and store extracted PMCs
    fileName = "PMCs_sleep_%s"%(iter)
    results = read_energy_pmcs(fileName)
    totalEnergy = results[0] + results[1]
    # Store base power
    listEnergy.append("%s"%str(totalEnergy))
    #print(len(listEnergy))
    if (len(listEnergy) >= 4):
        listEnergy = list(map(float, listEnergy))
        meanEnergy = calc_mean(listEnergy)
        varience = check_varience([meanEnergy,totalEnergy], varDesired,\
        verbosity)
	if (varience <= varDesired):
	    break
    # rest for 2 seconds
    os.system("sleep 2")
    if (iter == iterations):
	print("Maximum number of iterations has achieved")
	break
    if (verbosity == 1):
        print("iter: %i"% iter, "power: %.2f"% totalEnergy, "mean: %.2f\
"% meanEnergy, "varience: %.3f"% varience)
    iter += 1

if (arguments == 4):
    listEnergy = list(map(float, listEnergy))
    print("\n Power Samples: %s \n" % listEnergy)
    print("Iterations Done: %i"% (iter), "Max Iterations: %i\
"% (iterations), "Base Power: %f"% meanEnergy, "Varience: %.2f"% varience)
    
"""
f=open('PMCs_sleep_3',"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split(' ')[1])
f.close()

print(result)


size = 12000
while (size <= 12000):
    # Specify application here
    application = "numactl --physcpubind=0-43 DGEMM/dgemm.sh %s 1"%(size)
    command = "%s -c %s -g %s,%s %s\
"%(likwid,cores,energyPmcs,applicationSpecPmcs,application)
    os.system(command)
    size += 10000
"""
