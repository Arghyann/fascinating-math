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

def lerp(x, y, a, step=20):  # starting with a quadratic bezier curves
    p1 = np.zeros((step, 2))
    p2 = np.zeros((step, 2))
    for i, t in enumerate(np.linspace(0, 1, step)):
        p1[i]=x+t*(a-x)
        p2[i]=a+t*(y-a)
        

    return p1,p2

def main():
    c = [None] * 3
    c[0] = np.array([WIDTH // 2 - 50, HEIGHT // 2])  # point1
    c[1] = np.array([WIDTH // 2 + 50, HEIGHT // 2])  # point2
    c[2] = np.array([WIDTH // 2, HEIGHT // 2 + 50])  # point3
    dragging = [False] * 3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = np.array(pygame.mouse.get_pos())
                # Check if mouse is within any of the circles
                for i in range(3):
                    if np.linalg.norm(c[i] - mouse_pos) <= 5:
                        print(f"Mouse is in circle {i + 1}")
                        dragging[i] = True
            elif event.type == pygame.MOUSEMOTION:
                for i in range(3):
                    if dragging[i]:
                        c[i] = np.array(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in range(3):
                    dragging[i] = False

        screen.fill(BLACK)
        for i in range(3):
            color = WHITE if i < 2 else (255, 0, 0)
            pygame.draw.circle(screen, color, c[i], 5)
        p1,p2=lerp(c[0],c[1],c[2])
        for i in range(len(p1)):
            pygame.draw.line(screen, WHITE, p1[i],p2[i], 2)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
