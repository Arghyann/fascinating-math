import pygame
import sys
import numpy as np

pygame.init()

infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Bezier curves")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
step=200
def lerp(a,b,t):
    return a+t*(b-a)
def quad(a,b,c,t):
    p1=lerp(a,b,t)
    p2=lerp(b,c,t)
    return lerp(p1,p2,t)
def cubic(a,b,c,d,t):
    p1=quad(a,b,c,t)    
    p2=quad(b,c,d,t)
    return lerp(p1,p2,t)
def main():
    c = [None] * 4
    c[0] = np.array([WIDTH // 2 - 100, HEIGHT // 2])      # point1
    c[1] = np.array([WIDTH // 2 - 50, HEIGHT // 2 + 100])  # point2
    c[2] = np.array([WIDTH // 2 + 50, HEIGHT // 2 - 100])  # point3
    c[3] = np.array([WIDTH // 2 + 100, HEIGHT // 2])      # point4
    dragging = [False] * 4

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = np.array(pygame.mouse.get_pos())
                # Check if mouse is within any of the circles
                for i in range(4):
                    if np.linalg.norm(c[i] - mouse_pos) <= 5:
                        print(f"Mouse is in circle {i + 1}")
                        dragging[i] = True
            elif event.type == pygame.MOUSEMOTION:
                for i in range(4):
                    if dragging[i]:
                        c[i] = np.array(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in range(4):
                    dragging[i] = False

        points = []
        for i in range(step):
            t = i / (step - 1)
            point = cubic(c[0], c[1], c[2], c[3], t)
            points.append(point)

        screen.fill(BLACK)  # Clear the screen before drawing
        for i in range(4):
            color = WHITE if i in [0,3] else (255, 0, 0)
            pygame.draw.circle(screen, color, c[i], 5)
        pygame.draw.lines(screen, WHITE, False, points, 2)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
