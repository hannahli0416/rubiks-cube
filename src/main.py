import pygame
from pygame.locals import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Rubik's Cube Sim")

    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()
    angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 0, 1, 0)  # spin, just to prove rendering + rotation work
        draw_test_triangle()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def draw_test_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0); glVertex3f(0, 1, 0)
    glColor3f(0, 1, 0); glVertex3f(-1, -1, 0)
    glColor3f(0, 0, 1); glVertex3f(1, -1, 0)
    glEnd()

if __name__ == "__main__":
    main()