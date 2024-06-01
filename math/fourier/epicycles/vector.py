import numpy as np

import matplotlib.patches as patches

class Vector:
    def __init__(self, coeff, omega,previous=None,is_last=False,show_circles=False):
        self.previous=previous
        if self.previous is not None:
            self.baseCords=self.previous.getHeadPosition(0)
        else:
            self.baseCords=0+0j
        self.coeff=coeff
        self.omega = omega
        self.head_position=0
        self.is_last=is_last
        self.positions=[]
        self.showcircles=show_circles

    def getHeadPosition(self,t):
        if self.previous is not None: self.baseCords=self.previous.head_position
        cords=self.baseCords+self.coeff*np.exp(1j*self.omega*t)
        self.head_position=cords          #updates head position every time fore better efficiency 
        self.positions.append(cords)
        return cords
    
    def drawVector(self, t, ax):
        current_position = self.getHeadPosition(t)
        dx = np.real(current_position) - np.real(self.baseCords)
        dy = np.imag(current_position) - np.imag(self.baseCords)
        length = np.sqrt(dx**2 + dy**2)
        arrow = patches.FancyArrow(np.real(self.baseCords), np.imag(self.baseCords),
                           dx, dy,
                           head_width=0.1, head_length=0.2, fc='r', ec='r',
                           length_includes_head=True)
        ax.add_patch(arrow)
        if self.showcircles:
            circle=patches.Circle((np.real(self.baseCords),np.imag(self.baseCords)),radius=length,edgecolor='g', facecolor='none')
            ax.add_patch(circle)      #uncomment to add the stupid circles
        if self.is_last:
            
            if len(self.positions) > 1:
                trajectory = np.array(self.positions)
                ax.plot(np.real(trajectory), np.imag(trajectory), color='blue', linestyle='-')  # Draw a solid line



        
        
        
