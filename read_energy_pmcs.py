'''This file reads the columns of data from text file
'''

#######################################################################

def read_energy_pmcs(file):
    """ (string) -> float 
    This function takes the name of file as input and returns the co-
    ntents in second column as an output
    """
    f = open(file,"r")
    lines=f.readlines()
    result=[]
    for x in lines:
	result.append(x.split(' ')[1])
    return list(map(float, result))
    f.close()

