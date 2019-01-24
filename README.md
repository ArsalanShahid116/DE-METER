# DE-METER: Calculate Dynamic Energy Consumption Using RAPL Meter 

DE-METER is a wrapper using Likwid tool to calculate the dynamic energy<br />
 consumption of CPU and DRAM using RAPL within a given statistical <br />
confidence interval for any given application. <br />

Arsalan Shahid and Muhammad Fahad <br />
e-mail: <arsalan.shahid@ucdconnect.ie>


### Required Software
---------------------

1. Likwid tool
2. Pyhton compiler
3. Linux Ubuntu 16.04 and above

### How to Use
--------------
For getting dynamic energy consumption of any given application using default  <br />
settings, specify the application in 'run_application.py' script and run  <br />
using following command:

```
python ./get_dynamic_energy <application>
```

Get base power of server using:

```
python get_base.py <desired_varience (1-100)> <max_iterations> <verbosity (1 || 2)>
python get_base.py 5 100 1 1
```

Get total power of server running an application using:

```
python ./get_total_energy.py <desired_varience (1-100)> <max_iterations> <desired_std (e.g. 10)> <verbosity (1 || 2)> <application>

python ./get_total_energy.py 5 100 10 1 ./app
```
### License
------------
Copyright 2001-2018 Heterogeneous Computing Laboratory, <br />
School of Computer Science, University College Dublin<br />

Redistribution and use in source and binary forms, <br />
with or without modification, are permitted provided <br />
that the following conditions are met:<br />

1. Redistributions of source code must retain the <br />
   above copyright notice, this list of conditions <br />
   and the following disclaimer.<br />

2. Redistributions in binary form must reproduce the <br />
   above copyright notice, this list of conditions and <br />
   the following disclaimer in the documentation and/or <br />
   other materials provided with the distribution.<br />

3. Neither the name of the copyright holder nor the names <br />
   of its contributors may be used to endorse or promote <br />
   products derived from this software without specific <br />
   prior written permission.<br />

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" <br />
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE <br />
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE <br />
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE <br />
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR <br />
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF <br />
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS <br />
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN <br />
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) <br />
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF <br />
THE POSSIBILITY OF SUCH DAMAGE.<br />

### NOTE
--------
This software depends on other packages that may be licensed under different open source licenses.
