import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from cube import createSolvedCube
from shapes import getAllFaces

def drawCube(cubies):
    faces = getAllFaces(cubies)
    for corners, color in faces:
        glColor3f(*color)
        glBegin(GL_QUADS)
        for corner in corners:
            glVertex3f(*corner)
        glEnd()

        # draws outline around each face
        glColor3f(0, 0, 0)
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)
        for corner in corners:
            glVertex3f(*corner)
        glEnd()


def main():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Rubik's Cube Sim")

    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    cubies = createSolvedCube()

    # camera state
    rotX, rotY = -30, 30 # start at 3/4 viewing angle
    dragging = False
    lastMousePos = (0, 0)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                dragging = True
                lastMousePos = event.pos
            elif event.type == MOUSEBUTTONUP:
                dragging = False
            elif event.type == MOUSEMOTION and dragging:
                dx = event.pos[0] - lastMousePos[0]
                dy = event.pos[1] - lastMousePos[1]
                rotY += dx * 0.5
                rotX += dy * 0.5
                lastMousePos = event.pos

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # apply camera rotation fresh each frame, then draw, then undo it
        glPushMatrix()
        glRotatef(rotX, 1, 0, 0)
        glRotatef(rotY, 0, 1, 0)

        drawCube(cubies)

        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()


