from epicycloid import EpicycloidAnimator
import numpy as np
# Create an instance of EpicycloidAnimator
circles=False#change to show circles
pathToFile=r"D:\fascinating-math\math\fourier\epicycles\output\test1.txt"
epicycloid_animator = EpicycloidAnimator(num_vectors=100, total_time=1,path=pathToFile,show_circles=circles)

# Start animation
epicycloid_animator.animate()