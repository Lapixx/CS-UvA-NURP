#!/usr/bin/env python

"""
Numerical Recipes Project - Lagrange Interpolation
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as ip

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

def main():
    points = [(0, 2), (2, 1), (1, 2.3), (3, -1), (5.8, 3.5), (6.5, 0.5), (4.5, 2)]
    steps = 100
    zoom = 0.5
    for i in range(len(points)):
        showGraph(points[:i + 1], steps, zoom)

if __name__ == "__main__":
    main()
