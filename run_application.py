import os

problemSize = 36416
while (problemSize < 42000): 
    command = "python get_dynamic_energy.py 'FFT/fft.sh %i %i 1 1' >> DEFFT"% (problemSize, problemSize)
    os.system(command)    
    problemSize += 64
