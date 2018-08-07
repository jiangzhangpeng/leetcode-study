# encoding:utf-8
import numpy as np

"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Now we view the projection of these cubes onto the xy, yz, and zx planes.
A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.
Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
Return the total area of all three projections.

https://leetcode.com/problems/projection-area-of-3d-shapes/description/
"""


def projectionArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    top = sum(sum(np.array(grid,dtype=np.int32) >= 1))
    front = sum(np.max(grid, axis=0))
    side = sum(np.max(grid, axis=1))
    print(top)
    print(front)
    print(side)
    return top + front + side


if __name__ == '__main__':
    print(projectionArea([[2]]))
    #[[2, 2, 2], [2, 1, 2], [2, 2, 2]]
