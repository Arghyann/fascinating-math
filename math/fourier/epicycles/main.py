import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from vector import Vector  
num_vectors = 100
vectors = []

for i in range(num_vectors):
    coeff = 0.5
    omega = np.random.uniform(-2*np.pi, 2*np.pi)
    is_last = (i == num_vectors - 1)
    v = Vector(coeff=coeff, omega=omega, is_last=is_last, previous=vectors[-1] if vectors else None)
    vectors.append(v)

# Define time parameters
total_time = 1000  # Total time for the animation in seconds
num_frames = 100000  # Number of frames
time_step = total_time / num_frames  # Time step in seconds

def update(frame):
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_title('Chained Vectors in Complex Plane')
    ax.grid(True)
    
    # Calculate time in seconds
    t = frame * time_step
    
    # Update and draw each vector
    for vec in vectors:
        vec.drawVector(t, ax)

# Create a new plot
fig, ax = plt.subplots()

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), interval=50)

plt.show()
