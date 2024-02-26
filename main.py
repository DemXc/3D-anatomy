import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glVertex2f(-3, 3)
    glVertex2f(3, 3)
    glVertex2f(3, -3)
    glVertex2f(-3, -3)
    glEnd()

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(80, display[0] / display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
