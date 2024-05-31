import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from vector import Vector  
from fourierTransform import ft,dft

class EpicycloidAnimator:
    def __init__(self, num_vectors, total_time):
        self.num_vectors = num_vectors
        self.total_time = total_time
        
        self.time_step = total_time / 2*np.pi/num_vectors
        self.num_frames=total_time/self.time_step
        self.vectors = []
        self.fig, self.ax = plt.subplots()  # Create figure and axes
        
    def init_vectors(self):
        y=[]
        for z in range(100):
            y.append(ft(z))
        coeffs=[]
        step_size=1/self.num_vectors
        frequency_numbers = np.arange(-10, 10+step_size, step_size)[::-1]  #reversed because max frequency will have max amplitude

        for frequencyNumber in frequency_numbers:
            coeffs.append(dft(frequency=frequencyNumber,y=y))
        
        
        for i in range(self.num_vectors-1):
            coeff =coeffs[i]
            omega =2*np.pi*frequency_numbers[i]
            is_last = (i == self.num_vectors - 1)
            v = Vector(coeff=coeff, omega=omega, is_last=is_last, previous=self.vectors[i-1] if i!=0 else None)
            self.vectors.append(v)

    def update(self, frame):
        self.ax.clear()  # Clear the axes
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-25,25)
        self.ax.set_ylim(-25,25)
        self.ax.set_xlabel('Real')
        self.ax.set_ylabel('Imaginary')
        self.ax.set_title('Chained Vectors in Complex Plane')
        self.ax.grid(True)

        # Calculate time in seconds
        t = frame * self.time_step

        # Update and draw each vector
        for vec in self.vectors:
            vec.drawVector(t, self.ax)

    def animate(self):
        # Initialize vectors
        self.init_vectors()

        # Animate the plot
        ani = animation.FuncAnimation(self.fig, self.update, frames=np.arange(0, self.num_frames), interval=50)

        plt.show()


