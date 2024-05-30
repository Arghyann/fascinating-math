import numpy as np

y = [100, 100, 100, -100, -100, -100, 100, 100, 100, -100, -100, -100, 100, 100, 100, -100, -100, -100, 100, 100, 100, -100, -100, -100]

def dft(ythis):
    N = len(ythis)
    fourierCoeffs = [] # Initialize array to store Fourier coefficients
    
    for k in range(N):
        sum = 0 + 0j  # Initialize sum as complex number
        for n in range(N):
            commonTerm = 2 * np.pi * k * n / N
            sum += ythis[n] * np.exp(-1j * commonTerm)
        
       
        frequency=k
        phase=np.arctan2(np.imag(sum),np.real(sum))
        amplitude=np.linalg.norm(sum)
        fourierCoeffs.append([frequency,phase,amplitude])
    return fourierCoeffs

x = dft(y)
print(x)