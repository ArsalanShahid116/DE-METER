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
stdDesired = 0
application = " "

arguments = len(sys.argv)
if (arguments != 6):
    print("\n Execute: \n # python ./get_total_energy.py <desired_varience (1-\
100)> <max_iterations> <desired_std (e.g. 10)> <verbosity (1 || 2)> <\
application>")
else:
    varDesired = float(sys.argv[1])
    iterations = int(sys.argv[2])
    stdDesired = float(sys.argv[3])
    verbosity = int(sys.argv[4])
    application = str(sys.argv[5])

#######################################################################
# Application parameters
#######################################################################

tag = application.replace(" ", "")
tag0 = tag.replace(".sh", "")
tag00 = tag0.replace(".", "")
tag1 = tag00.replace("/", "")

#######################################################################
# Clear previous files
#######################################################################

if (verbosity == 1):
    print("Removing previous outputs")
clearFiles = "rm PMCs_* DGEMMdgemm* FFTfft*"
os.system(clearFiles)

#######################################################################

iter = 0
listEnergy = []
results = [[0],[0]]
meanEnergy = 0.0
varience = 0.0 
stdDev = 0

#######################################################################
# Likwid Parameters
#######################################################################

likwid = "likwid-perfctr -f"
cores = "0-43" # specify core to monitor PMCs
energyPmcs = "PWR_PKG_ENERGY:PWR0,PWR_DRAM_ENERGY:PWR3"

#######################################################################
# Collect PMCs and calculate total energy
#######################################################################

while (iter < iterations):
    runLikwid = "%s -c %s -g %s %s >> %s_%s"%(likwid,cores, \
    energyPmcs,application,tag1,iter)
    os.system(runLikwid)
    # Extract PMCs from Likwid output file
    extractPmcs = "./extract.sh %s_%s"%(tag1,iter)
    os.system(extractPmcs)
    # Read and store extracted PMCs
    fileName = "PMCs_%s_%s"%(tag1,iter)
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
	stdDev = varience ** 0.5
        if (varience <= varDesired):
	    break
        elif ((len(listEnergy)>15) and (stdDev<=stdDesired)):
            break
    # rest for 2 seconds
    os.system("sleep 2")
    if (iter == iterations):
	print("Maximum number of iterations has achieved")
	break
    if (verbosity == 1):
        print("iter: %i"% iter, "Energy: %.2f"% totalEnergy, "mean: %.2f\
"% meanEnergy, "varience: %.2f"% varience, "std Deviation %.2f"% stdDev)
    iter += 1

if (arguments == 6):
    listEnergy = list(map(float, listEnergy))
    print("\n Power Samples: %s \n"% listEnergy)
    print("Max Allowed Iterations: %i"% iterations) 
    if (varience <= varDesired) and (stdDev <= stdDesired):
        print("The desired varience and standard deviation is achieved.")
    elif (stdDev <= stdDesired):
	print("stdDev '%.2f' at iter '%i' achieved within desired stdDev '%.2f'\
"% (stdDev, iter, stdDesired))
    elif (varience <= varDesired):
	print("Varience '%.2f' at iter '%i' achieved within desired varience '%.2f'\
"% (varience, iter, varDesired))
    else:
	print("The desired varience and standard deviation is NOT achieved.")
    print("Iterations Done: %i"% iter, "Total Energy: %f"% meanEnergy, "Var\
ience: %.2f"% varience, "Std Deviation %.2f"% stdDev)



