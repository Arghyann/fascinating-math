import pygame
import numpy as np
import os
from fourierTransform import dft
from dealwithpoints import read_points_from_file
from svgtopoints import extract_points_from_svg
from arrangeVectors import arrangeVectors, findmaxXandY
from epicycloid import EpicycloidAnimator

path = r"fourier\epicycles\output\svgs\fourier.svg"
epicycles = EpicycloidAnimator(num_vectors=50, total_time=1, path=path, show_circles=False, zoom=True)
epicycles.init_vectors()
for vector in epicycles.vectors:
    vector.omega*=0.5


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epicycloid Animation")
clock = pygame.time.Clock()

# Set the new center at the endpoint of the first vector
first_vector = epicycles.vectors[0]
base_x, base_y = np.real(first_vector.head_position), np.imag(first_vector.head_position)
screen_center = (WIDTH // 2, HEIGHT // 2)  # Keep the first vector's endpoint at the screen center

t = 0
dt = 1 / epicycles.num_frames

def drawVector(vector, screen, t, screen_center):
    """Draw a vector and optionally its guiding circle in Pygame."""
    current_position = vector.getHeadPosition(t)

    # Offset everything relative to first vector's endpoint
    x1, y1 = np.real(vector.baseCords) - base_x, np.imag(vector.baseCords) - base_y
    x2, y2 = np.real(current_position) - base_x, np.imag(current_position) - base_y

    # Convert to Pygame coordinates (flip y-axis)
    start_pos = (screen_center[0] + x1, screen_center[1] - y1)
    end_pos = (screen_center[0] + x2, screen_center[1] - y2)

    pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 2)  # Red vector

    if vector.showcircles:
        radius = abs(vector.coeff)
        pygame.draw.circle(screen, (0, 255, 0), start_pos, int(radius), 1)  # Green guiding circle

    # Draw trajectory
    if vector.is_last and len(vector.positions) > 1:
        trajectory_points = [
            (screen_center[0] + np.real(p) - base_x, screen_center[1] - np.imag(p) + base_y)
            for p in vector.positions
        ]
        pygame.draw.lines(screen, (0, 0, 255), False, trajectory_points, 2)  # Blue trajectory line

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen (Black)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw all vectors
    for vector in epicycles.vectors:
        drawVector(vector, screen, t, screen_center)

    t += dt  # Increment time
    pygame.display.flip()  # Refresh display
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
