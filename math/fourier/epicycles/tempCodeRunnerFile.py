from epicycloid import EpicycloidAnimator
from fourierTransform import dft
# Create an instance of EpicycloidAnimator


epicycloid_animator = EpicycloidAnimator(num_vectors=100, total_time=10)

# Start animation
epicycloid_animator.animate()