from epicycloid import EpicycloidAnimator
from fourierTransform import dft
# Create an instance of EpicycloidAnimator
y = [
    -10 + 10j,  # Vertex 1
    10 + 10j,   # Vertex 2
    10 - 10j,   # Vertex 3
    -10 - 10j,  # Vertex 4
] * 50  # Repeat the vert
outputfunction=dft(ythis=y,fps=100,n=2)
epicycloid_animator = EpicycloidAnimator(num_vectors=200, total_time=1000, num_frames=100000,outputfunction=outputfunction)

# Start animation
epicycloid_animator.animate()