# -*- coding: utf-8 -*-
"""
Simple program to illustrate cartesian mesh visualisation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math


def show_square(grid_resolution=(2, 2), angle=0):
    """Draw Cartesian grid in a square [-1,1]x[1,1] rotated be given angle
    Parameters
    ----------
    grid_resolution
        number of cells in any direction (X, Y)
    angle
        rotation angle in degrees
    """
    try:
        res = grid_resolution*2
        resolution = res[0:2]
    except TypeError:
        resolution = (grid_resolution,)*2
        
    fig, ax = plt.subplots()
    angle = np.deg2rad(angle)
    c, s = math.cos(angle), math.sin(angle)
    rot = np.array([[c, -s], [s, c]])
    x = np.linspace(-1.0, 1.0, resolution[0]+1, dtype=np.float64)
    y = np.linspace(-1.0, 1.0, resolution[1]+1, dtype=np.float64)
    xx, yy = np.meshgrid(x, y)
    coordinates = np.dot(np.c_[xx.flatten(), yy.flatten()], rot.T)
    square_mesh = matplotlib.collections.QuadMesh(*resolution, coordinates,
                                                  edgecolors='black')
    ax.add_collection(square_mesh)
    ax.autoscale()
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    show_square(angle=10, grid_resolution=(6, 5))
