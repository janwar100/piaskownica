# -*- coding: utf-8 -*-
"""
Simple program to illustrate cartesian mesh visualisation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math


def show_square(grid_resolution=(4, 4), angle=0):
    """Draw Cartesian grid in a square [-1,1]x[1,1] rotated by given angle
    Parameters
    ----------
    grid_resolution : int or tuple
        number of cells in X and Y direction. If single number is given then
        mesh resolution in both directions is the same
    angle
        rotation angle in degrees
    """
    try:
        res = grid_resolution
        resolution = res[0:4]
    except TypeError:
        resolution = (grid_resolution,)*2
        
    fig, ax = plt.subplots()
    angle = np.deg2rad(angle)
    c, s = math.cos(angle), math.sin(angle)
    rot = np.array([[c, -s], [s, c]])
    x = np.linspace(-3.0, 3.0, resolution[0]+1, dtype=np.float64)
    y = np.linspace(-2.0, 2.0, resolution[1]+1, dtype=np.float64)
    xx, yy = np.meshgrid(x, y)
    coordinates = np.dot(np.c_[xx.flatten(), yy.flatten()], rot.T)
    square_mesh = matplotlib.collections.QuadMesh(*resolution, coordinates,
                                                  edgecolors='red')
    ax.add_collection(square_mesh)
    ax.autoscale()
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    show_square(angle=10, grid_resolution=(6, 5))
