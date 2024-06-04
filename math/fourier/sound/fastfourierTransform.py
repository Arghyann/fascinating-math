import numpy as np
#I'm only writing this again so that I can understand it better
#passing k here seems redundant because it's just the length of the input space 
def fourier(y):        #y is the original signal k is the number of frequenies you wanna break it down into
    N=len(y)
    
    coeffs=[]
    for k in range(-N//2,N//2):
        sum=0
        for n in range(N):
            sum+=y[n]*np.exp(-1j*2*np.pi*k*n/N)         #n/N can basically be thought of as time
        coeffs.append(np.real(sum)/N+np.imag(sum)/N)
    return coeffs