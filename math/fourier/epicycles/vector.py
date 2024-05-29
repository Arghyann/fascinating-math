import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

class Vector:
    def __init__(self, coeff, omega,previous=None):
        self.previous=previous
        if self.previous is not None:
            self.baseCords=self.previous.getHeadPosition(0)
        else:
            self.baseCords=0+0j
        self.coeff=coeff
        self.omega = omega
        self.head_position=0

    def getHeadPosition(self,t):
        if self.previous is not None: self.baseCords=self.previous.head_position
        cords=self.baseCords+self.coeff*np.exp(1j*self.omega*t)
        self.head_position=cords          #updates head position every time fore better efficiency 
        return cords
    
    def drawVector(self, t, ax):
        current_position = self.getHeadPosition(t)
        self.head_position = current_position
        ax.arrow(np.real(self.baseCords), np.imag(self.baseCords),
                 np.real(current_position) - np.real(self.baseCords),
                 np.imag(current_position) - np.imag(self.baseCords),
                 head_width=0.1, head_length=0.2, fc='r', ec='r')




        
        
        
