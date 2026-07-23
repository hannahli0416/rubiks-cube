from cube import createSolvedCube, applyMove
from shapes import getCubieFaces, getAllFaces

cube = createSolvedCube()

target = next(c for c in cube if c.position == (1, 1, 1))
faces = getCubieFaces(target)

for corners, color in faces:
    xs = [p[0] for p in corners]
    print(f'color = {color}     x-range=({min(xs):.2f}, {max(xs):.2f})')
print()

print('Total faces for whole cube (should be 156): ', len(getAllFaces(cube)))

