import numpy as np
from cube import Cubie, RIGHT, LEFT, UP, DOWN, FRONT, BACK, SOLVED_COLORS


# RGB colors for PyOpenGL (values from 0 to 1, not 0 to 255)
COLOR_RGB = {
    'red':    (0.77, 0.05, 0.10),
    'orange': (1.00, 0.45, 0.00),
    'white':  (1.00, 1.00, 1.00),
    'yellow': (1.00, 0.85, 0.00),
    'green':  (0.00, 0.60, 0.20),
    'blue':   (0.00, 0.30, 0.80),
    'plastic': (0.05, 0.05, 0.05), # shown in the gaps between cubies
}

CUBIE_SIZE = 0.9 # slightly smaller than 1 to allow for gaps
SPACING = 1.0 # distance between centers of cubies



# Define the corners of each face of a cubie in local coordinates (think unit cube)
# e.g. all corners of RIGHT face are at x = +half (+0,45), and vary in y and z
# Corners differ in ONE coordinate only at a time (e.g. (-half, -half, half) --> (-half, half, half))
# so that when PyOpenGL draws the edges it doesn't accidentally draw diagonals. 
# Basically we want to make sure they are in order. Think pencil drawing square without lifting (we don't want bowties)
half = CUBIE_SIZE / 2
FACE_CORNERS = {
    RIGHT: [(half, -half, -half), (half, half, -half), (half, half, half), (half, -half, half)],
    LEFT:  [(-half, -half, half), (-half, half, half), (-half, half, -half), (-half, -half, -half)],
    UP:    [(-half, half, -half), (-half, half, half), (half, half, half), (half, half, -half)],
    DOWN:  [(-half, -half, half), (-half, -half, -half), (half, -half, -half), (half, -half, half)],
    FRONT: [(-half, -half, half), (half, -half, half), (half, half, half), (-half, half, half)],
    BACK:  [(half, -half, -half), (-half, -half, -half), (-half, half, -half), (half, half, -half)],
}

ALL_FACES = [RIGHT, LEFT, UP, DOWN, FRONT, BACK]    

def getCubieFaces(cubie):
    """
    Return a list of (worldCorners, rgbColor) for each face of the cubie.

    Basically we take the local corners of each face, rotate them using 
    cubie.orientation, and then translate them to the cubie's world position.
    """

    faces = []
    center = np.array(cubie.position) * SPACING # translates cubie.position into real distance by multiplying with SPACING
    for localFace in ALL_FACES:
        colorName = cubie.localColors.get(localFace, None)
        rgb = COLOR_RGB[colorName] if colorName else COLOR_RGB['plastic']

        worldCorners = []
        for localCorner in FACE_CORNERS[localFace]:
            # Rotate the local corner using the cubie's orientation matrix
            rotatedCorner = cubie.orientation @ np.array(localCorner)
            # translate it out
            worldPoint = rotatedCorner + center 
            worldCorners.append(tuple(worldPoint))

        faces.append((worldCorners, rgb))

    return faces


def getAllFaces(cubies):
    """
    Combines all cubie's faces into one big list for the renderer to draw
    """
    allFaces = []
    for cubie in cubies:
        allFaces.extend(getCubieFaces(cubie))
    return allFaces

