import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from vector import Vector  
from fourierTransform import dft
from dealwithpoints import read_points_from_file
from svgtopoints import extract_points_from_svg
import os
import time
from arrangeVectors import arrangeVectors
class EpicycloidAnimator:
    def __init__(self, num_vectors, total_time,path,show_circles,zoom):
        self.num_vectors = num_vectors
        self.total_time = total_time
        self.path=path
        self.time_step =1                  #very very important for animation
        self.num_frames=total_time/self.time_step
        self.vectors = []
        self.fig, self.ax = plt.subplots()  # Create figure and axes
        self.max_zoom=1
        self.showCircles=show_circles
        self.count=0                          #number of times the animation has occured
        self.zoom=zoom
    def init_vectors(self):
        _, file_extension = os.path.splitext(self.path)
        if file_extension.lower() == '.svg':
            y=extract_points_from_svg(self.path)
        elif file_extension.lower() == '.txt':
            y=read_points_from_file(self.path,814)   #change image height here
        print(y)
        coeffs=[]
        self.time_step=1/len(y)
        self.num_frames=self.total_time/self.time_step
        self.zoom_start_frame= self.num_frames//4            #most important things initilaised here
        self.zoom_end_frame=self.num_frames//2+self.num_frames//4
        frequency_numbers = np.arange(-self.num_vectors/2,self.num_vectors/2,1)  

        for frequencyNumber in frequency_numbers:
            coeffs.append(dft(frequency=frequencyNumber,y=y))
        arrangeVectors(coeffs)
        print(coeffs)
        del(frequency_numbers)
        self.centreOfMass=np.complex128(coeffs[0][0])
        
        for i in range(self.num_vectors):
            coeff =coeffs[i][0]
            omega =2*np.pi*coeffs[i][1]
            is_last = (i == self.num_vectors - 1)
            v = Vector(coeff=coeff, omega=omega, is_last=is_last, previous=self.vectors[i-1] if i!=0 else None,show_circles=self.showCircles)
            print(v.is_last)
            self.vectors.append(v)
        print(self.centreOfMass)
    def update(self, frame):
        if frame == 0:
            self.start_time = time.time()
            
        elif frame == 40:
            elapsed_time = time.time() - self.start_time
            print("fps: ", 40 / elapsed_time)
            self.count+=1
        self.ax.clear()  # Clear the axes
        self.ax.set_aspect('equal')
        self.ax.set_xlabel('Real')
        self.ax.set_ylabel('Imaginary')
        self.ax.set_title('Chained Vectors in the Complex Plane')
        self.initial_xlim=500
        self.initial_ylim=500
        
        # Calculate time in seconds
        t = frame * self.time_step
        #print(t)
        #print(self.time_step)
        #print(frame)
        # Update and draw each vector
        for vec in self.vectors:
            vec.drawVector(t, self.ax)
            end_pos=vec.getHeadPosition(t)
        if self.count==1 and self.zoom:
            if self.zoom_start_frame <= frame <= self.zoom_end_frame:
                zoom_factor = (frame - self.zoom_start_frame) / (self.zoom_end_frame - self.zoom_start_frame)  #fraction to increase zoom gradually
                zoom_level = self.initial_xlim - (self.initial_xlim -self.max_zoom) * zoom_factor   #max zoom is one here
                self.ax.set_xlim(end_pos.real - zoom_level, end_pos.real + zoom_level)
                self.ax.set_ylim(end_pos.imag - zoom_level, end_pos.imag + zoom_level)
            elif frame>self.zoom_end_frame:
                zoom_factor=(frame-self.zoom_end_frame)/(self.num_frames-self.zoom_end_frame)#zooms out more quickly
                zoom_out_level=self.max_zoom+(self.initial_xlim-self.max_zoom)*zoom_factor
                self.ax.set_xlim(end_pos.real - zoom_out_level, end_pos.real + zoom_out_level)
                self.ax.set_ylim(end_pos.imag - zoom_out_level, end_pos.imag + zoom_out_level)
            else:
                self.ax.set_xlim(np.real(self.centreOfMass)-self.initial_xlim,np.real(self.centreOfMass)+ self.initial_xlim)
                self.ax.set_ylim(np.imag(self.centreOfMass)-self.initial_ylim, np.imag(self.centreOfMass)+self.initial_ylim)
        else:
            self.ax.set_xlim(np.real(self.centreOfMass)-self.initial_xlim,np.real(self.centreOfMass)+ self.initial_xlim)      #only zoom the first time
            self.ax.set_ylim(np.imag(self.centreOfMass)-self.initial_ylim, np.imag(self.centreOfMass)+self.initial_ylim)

    def animate(self):
        # Initialize vectors
        self.init_vectors()
        print(self.num_frames)
        
        
        # Animate the plot
        ani = animation.FuncAnimation(self.fig, self.update, frames=np.arange(0, self.num_frames), interval=5)
        #edit interval to make animation go faster
        plt.show()


