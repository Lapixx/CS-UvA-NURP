#!/usr/bin/env python

"""
Numerical Recipes Project - Lagrange Interpolation
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

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

def lagrange(points, x):
    n = len(points)
    xs, ys = unzip(points)

    y = 0
    for i in range(n):
        a = ys[i]
        for j in range(n):
            if j != i:
                a *= (x - xs[j]) / (xs[i] - xs[j])
        y += a
    return y

# -------------------- Assignment A --------------------

def showGraph(points, steps, zoom):
    degree = len(points) - 1
    xs, ys = unzip(points)

    # calculate bounds
    xi = min(xs)
    xe = max(xs)
    yi = min(ys)
    ye = max(ys)
    dx = xe - xi + 0.1
    dy = ye - yi + 0.1

    # scale bounds
    xi -= zoom * dx
    xe += zoom * dx
    yi -= zoom * dy
    ye += zoom * dy

    rangex = np.linspace(xi, xe, steps)

    plt.plot(rangex, map(lambda x: lagrange(points, x), rangex), 'g--', xs, ys, 'bo', xs[-1:], ys[-1:], 'ro')
    plt.axis([xi, xe, yi, ye])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(['Constant', 'Linear', 'Quadratic', 'Cubic', 'Quartic', 'Quintic', 'Sextic', 'Septic'][degree] + ' Lagrange Polynomial')

    plt.show()

def assignmentA():
    points = [(0, 2), (2, 1), (1, 2.3), (3, -1), (5.8, 3.5), (6.5, 0.5), (4.5, 2)]
    steps = 100
    zoom = 0.5
    for i in range(len(points)):
        showGraph(points[:i + 1], steps, zoom)

# -------------------- Assignment B --------------------

def f(t):
    return 1.0 / (t ** 2 + 1.0)

def getPoints(n):
    points = []
    for i in range(n + 1):
        x = -5.0 + 10.0 * i / n
        y = f(x)
        points += [(x, y)]
    return points

def assignmentB():
    steps = 100
    rangex = np.linspace(-6, 6, steps)

    points_a = getPoints(14)
    points_b = getPoints(6)

    axs, ays = unzip(points_a)
    bxs, bys = unzip(points_b)

    plt.plot(rangex, map(lambda x: lagrange(points_a, x), rangex), 'r-', rangex, map(lambda x: lagrange(points_b, x), rangex), 'b-', axs, ays, 'ro', bxs, bys, 'bo')
    plt.axis([-6, 6, -1, 5])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Approximate f(t) = 1 / (t^2 + 1)')

    plt.show()

# -------------------- Entry Point --------------------

def main():
    assignmentA()
    assignmentB()

if __name__ == "__main__":
    main()
