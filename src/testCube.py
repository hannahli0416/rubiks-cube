from cube import Cubie, createSolvedCube, applyMove, isSolved

print("Test 1: Solved cube starts solved")
cube1 = createSolvedCube()
assert isSolved(cube1), "Test 1 Failed: Solved cube should be recognized as solved."
print("Test 1 Passed")


print("Test 2: R move")
cube2 = createSolvedCube()
applyMove(cube2, "R")
assert not isSolved(cube2), "Test 2 Failed: Cube should not be solved after R move."
print("Test 2 Passed")


print("Test 3: R' move after R")
cube3 = createSolvedCube()
applyMove(cube3, "R")
applyMove(cube3, "R'")
assert isSolved(cube3), "Test 3 Failed: Cube should be solved after R followed by R'."
print("Test 3 Passed")


print("Test 3a: L' move after L")
cube3a = createSolvedCube()
applyMove(cube3a, "L")
applyMove(cube3a, "L'")
assert isSolved(cube3a), "Test 3a Failed: Cube should be solved after L followed by L'."
print("Test 3a Passed")


print("Test 3b: U' move after U")
cube3b = createSolvedCube()
applyMove(cube3b, "U")
applyMove(cube3b, "U'")
assert isSolved(cube3b), "Test 3b Failed: Cube should be solved after U followed by U'."
print("Test 3b Passed")


print("Test 3c: D' move after D")
cube3c = createSolvedCube()
applyMove(cube3c, "D")
applyMove(cube3c, "D'")
assert isSolved(cube3c), "Test 3c Failed: Cube should be solved after D followed by D'."
print("Test 3c Passed")

print("Test 3d: F' move after F")
cube3d = createSolvedCube()
applyMove(cube3d, "F")
applyMove(cube3d, "F'")
assert isSolved(cube3d), "Test 3d Failed: Cube should be solved after F followed by F'."
print("Test 3d Passed")

print("Test 3e: B' move after B")
cube3e = createSolvedCube()
applyMove(cube3e, "B")
applyMove(cube3e, "B'")
assert isSolved(cube3e), "Test 3e Failed: Cube should be solved after B followed by B'."
print("Test 3e Passed")


print("Test 4: R 4 times")
cube4 = createSolvedCube()
for _ in range(4):
    applyMove(cube4, "R")
assert isSolved(cube4), "Test 4 Failed: Cube should be solved after R 4 times."
print("Test 4 Passed")


print("Test 5: R2 move = R followed by R")
cube5a = createSolvedCube()
cube5b = createSolvedCube()
applyMove(cube5a, "R2")
applyMove(cube5b, "R")
applyMove(cube5b, "R")
# all(): all elements of the iterable are true, or if the iterable is empty
# zip(): loops through both lists simultaneously
# sorted(): sorts the cubies by position to ensure they are in the same order for comparison
assert all(c1.position == c2.position and c1.getWorldFaceColor() == c2.getWorldFaceColor()
            for c1, c2 in zip(sorted(cube5a, key = lambda c: c.position), 
                              sorted(cube5b, key = lambda c: c.position))), "Test 5 Failed: R2 should be equivalent to R followed by R."
print("Test 5 Passed")


print("Test 6: R2 followed by R2")
cube6 = createSolvedCube()
applyMove(cube6, "R2")
assert not isSolved(cube6), "Test 6 Failed: Cube should not be solved after one R2"
applyMove(cube6, "R2")
assert isSolved(cube6), "Test 6 Failed: Cube should be solved after R2 followed by R2."
print("Test 6 Passed")


print("Test 7: Full scramble/solve sequence across all 6 faces")
cube7 = createSolvedCube()
scrambleMoves = ["R", "U", "F", "L", "D", "B"]
unscrambleMoves = ["B'", "D'", "L'", "F'", "U'", "R'"]
for move in scrambleMoves:
    applyMove(cube7, move)
assert not isSolved(cube7), "Test 7 Failed: Cube should not be solved after scramble sequence."
for move in unscrambleMoves:
    applyMove(cube7, move)
assert isSolved(cube7), "Test 7 Failed: Cube should be solved after unscramble sequence."
print("Test 7 Passed")

print("All tests passed!")

