'''This program takes input applications' mean execution times, power 
and energy values to return the varience of the poulation. 
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
# Function definition
#######################################################################

def check_varience(samples,limit,verbosity):
    """ (numberList,number,int) -> (float,str)
    
    Take input sample list with 'atleast' two numbers (ints or float,
    user desired limit in percentage (0%-100%) and verbosity (0 or 1)
    . It calculates and returns True or False if varience satisfies 
    the limit.
    
    >>> print(check_varience([12],10))
    None 
    >>> print(check_varience([12,12.4],10))
    True
    >>> print(check_varience([2,3,4],10))
    False
    >>> print(check_varience([2,3],5))
    False
    """

    samplesLength = len(samples)
       
    if (samplesLength < 2):
        print("Error: samples list should have atleast two numbers")
        return

    varience = (np.var(samples, dtype=np.float64)*100)
    if (verbosity == 1):
        print("Varience Satisfied? ", varience < limit)
    return varience 

#######################################################################
# Program tests
#######################################################################

# Test the function by uncommenting the below lines
#check_varience([12],10)
#check_varience([12,12.4],10)
#check_varience([2,3,4],10)
#check_varience([2,3],5)
