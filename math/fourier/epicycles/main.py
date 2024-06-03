from epicycloid import EpicycloidAnimator

# Create an instance of EpicycloidAnimator
circles=False#change to show circles
pathToFile=r"D:\projects\python\fascinating-math\math\fourier\epicycles\output\test1.txt"
zoom=False
epicycloid_animator = EpicycloidAnimator(num_vectors=30, total_time=1,path=pathToFile,show_circles=circles,zoom=zoom)

# Start animation
epicycloid_animator.animate()