import numpy as np

RIGHT = (1, 0, 0)
LEFT = (-1, 0, 0)
UP = (0, 1, 0)
DOWN = (0, -1, 0)
FRONT = (0, 0, 1)
BACK = (0, 0, -1)

SOLVED_COLORS = {
    RIGHT: 'red',
    LEFT: 'orange',
    UP: 'white',
    DOWN: 'yellow',
    FRONT: 'green',
    BACK: 'blue'
}


class Cubie:
    def __init__(self, position, colors):
        self.position = position          # (x, y, z) coordinates of the cubie in the cube
        # dictionary mapping face names to colors
        # colors are LOCAL and NEVER change, they are fixed for each cubie
        # the orientation matrix is what tells you where local faces are in world space
        self.colors = colors
        self.orientation = np.identity(3) # 3x3 identity matrix representing the cubie's orientation in space

    def __repr__(self):
        return f"Cubie(position={self.position}, colors={self.colors})"

def createSolvedCube():
    cubies = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if (x, y, z) == (0, 0, 0):
                    continue  # Skip the center cubie
                position = (x, y, z)
                colors = {}
                if x == 1:
                    colors[RIGHT] = SOLVED_COLORS[RIGHT]
                elif x == -1:
                    colors[LEFT] = SOLVED_COLORS[LEFT]
                if y == 1:
                    colors[UP] = SOLVED_COLORS[UP]
                elif y == -1:
                    colors[DOWN] = SOLVED_COLORS[DOWN]
                if z == 1:
                    colors[FRONT] = SOLVED_COLORS[FRONT]
                elif z == -1:
                    colors[BACK] = SOLVED_COLORS[BACK]
                cubies.append(Cubie(position, colors))
    return cubies



"""
Rotate a cubie around a given axis (x, y, or z) by 90 degrees
'direction' = +1 for clockwise, -1 for counter-clockwise
"""

def rotateCubie(cubie, axis, direction):
    angle = np.pi / 2 * direction  # 90 degrees in radians
    c, s = round(np.cos(angle)), round(np.sin(angle))
    if axis == 'x':
        rotationMatrix = np.array([[1, 0, 0],
                                     [0, c, -s],
                                     [0, s, c]])
    elif axis == 'y':
        rotationMatrix = np.array([[c, 0, s],
                                     [0, 1, 0],
                                     [-s, 0, c]])
    elif axis == 'z':
        rotationMatrix = np.array([[c, -s, 0],
                                     [s, c, 0],
                                     [0, 0, 1]])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'.")

    # Update the cubie's orientation
    cubie.orientation = rotationMatrix @ cubie.orientation

    # Update the cubie's position
    cubie.position = tuple(np.round(rotationMatrix @ np.array(cubie.position)).astype(int))


# axis, axisIndex, layerIndex, direction
# axisDirection: x = 0, y = 1, z = 2
# layerIndex: corresponding to layer being rotated 

MOVES = {
    "R": ("x", 0, 1, -1), "R'": ("x", 0, 1, 1),
    "L": ("x", 0, -1, 1), "L'": ("x", 0, -1, -1),
    "U": ("y", 1, 0, -1), "U'": ("y", 1, 0, 1),
    "D": ("y", -1, 0, 1), "D'": ("y", -1, 0, -1),
    "F": ("z", 0, 1, -1), "F'": ("z", 0, 1, 1),
    "B": ("z", 0, -1, 1), "B'": ("z", 0, -1, -1)
}

def applyMove(cubies, moveName):

    if moveName.endswith("2"):
        base = moveName[:-1]
        applyMove(cubies, base)
        applyMove(cubies, base)
        return cubies

    axis, axisIndex, layerIndex, direction = MOVES[moveName]

    # checks if cubie is in the layer being rotated, if so add it to the list of cubies to be rotated
    layerCubies = [cubie for cubie in cubies if cubie.position[axisIndex] == layerIndex]

    for cubie in layerCubies:
        rotateCubie(cubie, axis, direction)

    return cubies

def isSolved(cubies):
    solved = createSolvedCube()
    solvedPositions = {cubie.position: cubie.colors for cubie in solved}
    for cubie in cubies:
        if cubie.position not in solvedPositions:
            return False
        if cubie.colors != solvedPositions[cubie.position]:
            return False
    return True

