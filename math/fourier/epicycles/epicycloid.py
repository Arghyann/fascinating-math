import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from vector import Vector  
from fourierTransform import dft
from dealwithpoints import read_points_from_file
from svgtopoints import extract_points_from_svg
import os

class EpicycloidAnimator:
    def __init__(self, num_vectors, total_time,path):
        self.num_vectors = num_vectors
        self.total_time = total_time
        self.path=path
        self.time_step =1                  #very very important for animation
        self.num_frames=total_time/self.time_step
        self.vectors = []
        self.fig, self.ax = plt.subplots()  # Create figure and axes
        
    def init_vectors(self):
        _, file_extension = os.path.splitext(self.path)
        if file_extension.lower() == '.svg':
            y=extract_points_from_svg(self.path)
        elif file_extension.lower() == '.txt':
            y=read_points_from_file(self.path,814)
        print(y)
        coeffs=[]
        self.time_step=1/len(y)
        self.num_frames=self.total_time/self.time_step
        frequency_numbers = np.arange(-self.num_vectors/2,self.num_vectors/2,1)  

        for frequencyNumber in frequency_numbers:
            coeffs.append(dft(frequency=frequencyNumber,y=y))
        print(coeffs)
        print(frequency_numbers)
        
        
        for i in range(self.num_vectors):
            coeff =coeffs[i]
            omega =2*np.pi*frequency_numbers[i]
            is_last = (i == self.num_vectors - 1)
            v = Vector(coeff=coeff, omega=omega, is_last=is_last, previous=self.vectors[i-1] if i!=0 else None)
            print(v.is_last)
            self.vectors.append(v)

    def update(self, frame):
        self.ax.clear()  # Clear the axes
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-1000,1000)
        self.ax.set_ylim(-1000,1000)
        self.ax.set_xlabel('Real')
        self.ax.set_ylabel('Imaginary')
        self.ax.set_title('Chained Vectors in the Complex Plane')
        
        
        # Calculate time in seconds
        t = frame * self.time_step
        #print(t)
        #print(self.time_step)
        #print(frame)
        # Update and draw each vector
        for vec in self.vectors:
            vec.drawVector(t, self.ax)

    def animate(self):
        # Initialize vectors
        self.init_vectors()
        print(self.num_frames)
        
        # Animate the plot
        ani = animation.FuncAnimation(self.fig, self.update, frames=np.arange(0, self.num_frames), interval=50)
        #edit interval to make animation go faster
        plt.show()


