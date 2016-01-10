#!/usr/bin/env python

"""
Numerical Recipes Project - Data visualisation
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as ip

# -------------------- Utils --------------------

def unzip(points):
    points_x = []
    points_y = []
    for p in points:
        points_x += [p[0]]
        points_y += [p[1]]

    return (points_x, points_y)

def getPoints(xs):
    points = []
    for x in xs:
        y = 2 * x +random.uniform(-0.5, 0.5)
        points += [(x ,y)]
    return points

# -------------------- Entry Point --------------------

def main():
    steps = 50
    xs = np.linspace(0, 5, steps)

    points = getPoints(xs)
    xs, ys = unzip(points)

    plt.plot([0, 5], [0, 10], 'b-', xs, ys, 'ro')
    plt.show()

if __name__ == "__main__":
    main()
