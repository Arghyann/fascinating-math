import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from vector import Vector  

class EpicycloidAnimator:
    def __init__(self, num_vectors, total_time, num_frames):
        self.num_vectors = num_vectors
        self.total_time = total_time
        self.num_frames = num_frames
        self.time_step = total_time / num_frames
        self.vectors = []
        self.fig, self.ax = plt.subplots()  # Create figure and axes

    def init_vectors(self):
        for i in range(self.num_vectors):
            coeff =1*np.exp(1j*np.pi/2)
            omega = np.random.uniform(-2*np.pi, 2*np.pi)
            is_last = (i == self.num_vectors - 1)
            v = Vector(coeff=coeff, omega=omega, is_last=is_last, previous=self.vectors[-1] if self.vectors else None)
            self.vectors.append(v)

    def update(self, frame):
        self.ax.clear()  # Clear the axes
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-10,10)
        self.ax.set_ylim(-10,10)
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


