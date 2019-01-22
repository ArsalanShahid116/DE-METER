'''This script executes a given application for a number of times to 
calculate its mean execution time satisfying a given varience.
'''

#######################################################################
import os
import sys
import time
from calc_mean import calc_mean
from chk_var import check_varience

#######################################################################
#Input command line arguments and initialize variables
#######################################################################

maxIter = 0
varDesired = 0
verbosity = 0
application = " "
arguments = len(sys.argv)

if (arguments != 5):
    print("\n Execute: \n # python ./mean_time.py <desired_varience (1-\
100)> <max_iterations> <verbosity (1 || 2)> <\
./application>")
else:
    varDesired = float(sys.argv[1])
    maxIter = int(sys.argv[2])
    verbosity = int(sys.argv[3])
    application = str(sys.argv[4])

#######################################################################

currentIter = 0
mtime = 0.0
listTime = list()
meanTime = 0
varience = 0 
   
while (currentIter <= maxIter):
    start = time.time()
    command = "%s"% (application)
    os.system(command)    
    end = time.time()
    mtime = end - start
    listTime.append("%s"% str(mtime))
    listTime = list(map(float, listTime))
    if (currentIter > 3):
        meanTime = calc_mean(listTime)
	varience = check_varience([meanTime,mtime], varDesired,\
        verbosity)
        if (varience <= varDesired):
	    break
    if (currentIter <=3):
        print("Current Iter: %i, Time: %.3f"% (currentIter, mtime))
    else:
        print("Current Iter: %i, Time: %.3f, Mean:%.3f, Varience:\
        %.3f"% (currentIter, mtime, meanTime, varience))
    currentIter += 1

if (arguments == 5):    
    print("Time Samples: %s"% listTime)
    print("Total Iterations: %i, MeanTime: %.3f, Varience: %.3f"% \
    (currentIter, meanTime, varience))

