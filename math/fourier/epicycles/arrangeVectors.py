import numpy as np
def arrangeVectors(list):
    
    list.sort(key=lambda x: abs(x[0]),reverse=True)

#sort the vectors however you like here

def findmaxXandY(a):
    max_x = max(abs(np.real(pair[0])) for pair in a)
    max_abs_y = max(abs(np.imag(pair[0])) for pair in a)

    return max_x, max_abs_y