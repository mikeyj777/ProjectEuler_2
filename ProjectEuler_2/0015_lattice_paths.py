import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and
# down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


def searchPaths(grid, nodeBranch, pathNo):

    if nodeBranch == (grid.shape[0] - 1, grid.shape[1] - 1):
        return pathNo + 1

    nodeBranches = []

    if nodeBranch[0] < grid.shape[0] - 1:
        nodeBranches.append((nodeBranch[0] + 1, nodeBranch[1]))

    if nodeBranch[1] < grid.shape[1] - 1:
        nodeBranches.append((nodeBranch[0], nodeBranch[1] + 1))

    for nodeBranch in nodeBranches:
        pathNo = searchPaths(grid, nodeBranch, pathNo)
        print(nodeBranch, pathNo)

    return pathNo


def controller(gridPointsPerSquareSide):
    gridX = gridPointsPerSquareSide
    gridY = gridPointsPerSquareSide

    grid = np.ones((gridX, gridY))

    pathNo = 0

    nodeBranch = (0, 0)

    pathNo = searchPaths(grid, nodeBranch, pathNo)

    return pathNo


squaresPerGridSide = 20


def countPaths_take2(pointsPerGridSide):

    grid = np.zeros((pointsPerGridSide, pointsPerGridSide))

    # initialise the grid with boundary conditions
    for i in range(pointsPerGridSide):
        grid[i, pointsPerGridSide - 1] = 1
        grid[pointsPerGridSide - 1, i] = 1

    for i in range(pointsPerGridSide - 2, -1, -1):
        for j in range(pointsPerGridSide - 2, -1, -1):
            grid[i, j] = grid[i + 1, j] + grid[i, j + 1]

    return grid[0, 0]


for i in range(1, 32):
    print(i, countPaths_take2(i))
