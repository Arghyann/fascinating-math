from vector import Vector
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(t):
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_title('Chained Vectors in Complex Plane')
    ax.grid(True)
    
    for vec in vectors:
        vec.drawVector(t, ax)

# Create the first vector
v1 = Vector(coeff=1, omega=2 * np.pi / 10)

# Create a second vector with the first vector as its previous vector
v2 = Vector(coeff=1, omega=-2 * np.pi / 10, previous=v1)

# List of vectors
vectors = [v1, v2]

# Create a new plot
fig, ax = plt.subplots()

# Time values in seconds
t_values = np.linspace(0, 1000000, 10000000)  # From 0 to 10 seconds with 100 time steps

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=t_values, interval=50)

plt.show()
