from epicycloid import EpicycloidAnimator
import numpy as np
# Create an instance of EpicycloidAnimator

pathToFile=r"D:\fascinating-math\math\fourier\epicycles\output\testsvg.svg"
epicycloid_animator = EpicycloidAnimator(num_vectors=200, total_time=20,path=pathToFile)

# Start animation
epicycloid_animator.animate()