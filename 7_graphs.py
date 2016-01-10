#!/usr/bin/env python

"""
Numerical Recipes Project - Graph visualisation
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import math
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

# -------------------- Assignment A -------------------

def f(t, x):
    return math.e**(-(x-3*t)**2) * math.sin(3 * math.pi * (x - t))

def getPoints(t, xs):
    points = []
    for x in xs:
        points += [(x, f(t, x))]
    return points

def assignmentA():
    steps = 400
    xs = np.linspace(-4, 4, steps)

    points_a = getPoints(-0.5, xs)
    points_b = getPoints(-0.25, xs)
    points_c = getPoints(0, xs)
    points_d = getPoints(0.25, xs)
    points_e = getPoints(0.5, xs)

    axs, ays = unzip(points_a)
    bxs, bys = unzip(points_b)
    cxs, cys = unzip(points_c)
    dxs, dys = unzip(points_d)
    exs, eys = unzip(points_e)

    plt.plot(axs, ays, 'r-', bxs, bys, 'g-', cxs, cys, 'b-', dxs, dys, 'g--', exs, eys, 'b--')
    plt.legend(['t = -0.5', 't = -0.25', 't = 0', 't = 0.25', 't = 0.5'])
    plt.axis([-4, 4, -2, 2])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphs')

    plt.show()



# -------------------- Entry Point --------------------

def main():
    assignmentA()
    # assignmentB()

if __name__ == "__main__":
    main()
