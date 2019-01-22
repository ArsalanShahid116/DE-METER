'''A wrapper using Likwid tool to calculate the dynamic energy consump-
tion of CPU and DRAM using RAPL for given applications.
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
# import packages and remove previous results
#######################################################################

import os,sys
import subprocess

os.system("rm MeanTime TotalEnergy BasePower")

#######################################################################
#Input command line arguments and initialize variables
#######################################################################

application = " "
arguments = len(sys.argv)
if (arguments != 2):
    print("\n Execute: \n # python ./get_dynamic_energy <application>")
else:
    application = str(sys.argv[1])


#######################################################################
# get base power
#######################################################################

print("Getting Base Power")
commandBase = "python get_base.py 5 100 1 >> BasePower"
os.system(commandBase)
basePowerExtract = "grep 'Iterations Done' BasePower | awk '{print $9}'\
  |  sed \"s/',//\" "

basePower = subprocess.check_output(basePowerExtract, shell=True)
print("Base Power =  %.2f " % float(basePower))

#######################################################################
# Compute mean execution time
#######################################################################

print("Starting computation of mean execution time for %s"% application)
commandTime = "python mean_time.py 1 100 1 '%s' >> MeanTime"% application
os.system(commandTime)
timeExtract = "grep 'Total Iterations' MeanTime | awk '{print $5}'\
 | sed 's/,//'"

meanTime = subprocess.check_output(timeExtract, shell=True)
print("Mean time for %s is %.2f " % (application, float(meanTime)))

#######################################################################
# Compute total energy
#######################################################################

print("Starting computation of total energy consumption for: %s"%\
 application)

commandTotalEnergy = "python get_total_energy.py 5 100 10 1 ' %s'\
 >> TotalEnergy"% application
os.system(commandTotalEnergy)
totalEnergyExtract = "grep 'Iterations Done' TotalEnergy | awk \
'{print $6}' |  sed \"s/',//\" "

totalEnergy = subprocess.check_output(totalEnergyExtract, shell=True)
print("Total Energy for %s is %.2f " % (application, float(totalEnergy)))

#######################################################################
# Calculate dynamic energy
#######################################################################

dynamicEnergy = float(totalEnergy) - (float(meanTime) * float(basePower))

print("Dynamic Energy for %s is %.2f "% (application, float(dynamicEnergy)))

#######################################################################
# Print results
#######################################################################

results = "echo Application: %s Mean time: %.2f, Total Energy: %.2f, \
Dynamic Energy: %.2f >> DynamicEnergy" % (application, float(meanTime), \
float(totalEnergy), float(dynamicEnergy))

os.system(results)
