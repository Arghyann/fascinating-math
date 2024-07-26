from epicycloid import EpicycloidAnimator

# Create an instance of EpicycloidAnimator
circles=False                     #change to show circles
pathToFile=r"D:\projects\python\fascinating-math\fourier\epicycles\output\texts\test1.txt"
zoom=True                        #change to enable or disable zoom
epicycloid_animator = EpicycloidAnimator(num_vectors=150, total_time=1,path=pathToFile,show_circles=circles,zoom=zoom)

# Start animation
epicycloid_animator.animate()