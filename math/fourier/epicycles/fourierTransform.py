import numpy as np



def dft(frequency, y):
    sum = 0
    t_values = np.linspace(0,1, num=len(y)-1, endpoint=False)  # Generate t values
    omega = 2 * np.pi * frequency
    i=0        #to extract values at the ith position in y
    for t in t_values:
        
        sum += y[i] * np.exp(-1j * omega * t)
        i+=1

    return sum/400,frequency                  #use this to scale the image up or down
'''coeffs=[]
frequency_numbers = np.arange(-10, 10.5, 0.5)

for frequencyNumber in frequency_numbers:
    coeffs.append(dft(frequency=frequencyNumber,y=y))'''


