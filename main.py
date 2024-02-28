import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices=((1,1),(1,-1),(-1,-1),(-1,1),
          (1,1),(1,-1),(-1,-1),(-1,1))

edge=((0,1),(1,2),(2,3),(3,0),
      (4,5),(5,6),(6,7),(7,4))

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

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
