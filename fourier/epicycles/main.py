
from epicycloid import EpicycloidAnimator
# Create an instance of EpicycloidAnimator
circles=False                     #change to show circles
pathToFile=r"fourier\epicycles\output\svgs\dragon.svg"
zoom=True                        #change to enable or disable zoom
epicycloid_animator = EpicycloidAnimator(num_vectors=50, total_time=1,path=pathToFile,show_circles=circles,zoom=zoom)

# Start animation
epicycloid_animator.animate()
