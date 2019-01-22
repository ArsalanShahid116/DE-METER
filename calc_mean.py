'''This program takes input applications' execution times, power and 
energy values and returns the sample means
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

import numpy as np

#######################################################################

def calc_mean(arg):
    """ (numberList) -> float
    
    Take input list is 'atleast' three numbers (ints or floats), cal-
    culate the means of the samples and return the floating point 
    mean value. 
    
    >>> calc_mean([1,2,3,4])  
    2.5000
    >>> calc_mean([1.503,2.232,3.231,4.32]) 
    2.8215
    """

    if (len(arg) < 3):
        message = "Error: the input list should atleast contain 3 numbers"
        print(message)
    else:
	return np.mean(arg, dtype=np.float64)

#######################################################################
# Test the function by uncommenting the below lines
#######################################################################

# print(calc_mean([1,2,3]))
# print(calc_mean([1.503,2.232,3.231,4.32]))

