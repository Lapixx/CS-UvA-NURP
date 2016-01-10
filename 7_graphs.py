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

def getPointsA(t, xs):
    points = []
    for x in xs:
        points += [(x, f(t, x))]
    return points

def assignmentA():
    steps = 400
    xs = np.linspace(-4, 4, steps)

    points_a = getPointsA(-0.5, xs)
    points_b = getPointsA(-0.25, xs)
    points_c = getPointsA(0, xs)
    points_d = getPointsA(0.25, xs)
    points_e = getPointsA(0.5, xs)

    axs, ays = unzip(points_a)
    bxs, bys = unzip(points_b)
    cxs, cys = unzip(points_c)
    dxs, dys = unzip(points_d)
    exs, eys = unzip(points_e)

    plt.subplot(511)
    plt.title('t = -0.5')
    plt.plot(axs, ays, 'r-')

    plt.subplot(512)
    plt.title('t = -0.25')
    plt.plot(bxs, bys, 'r-')

    plt.subplot(513)
    plt.title('t = 0')
    plt.plot(cxs, cys, 'r-')

    plt.subplot(514)
    plt.title('t = 0.25')
    plt.plot(dxs, dys, 'r-')

    plt.subplot(515)
    plt.title('t = 0.5')
    plt.plot(exs, eys, 'r-')

    plt.show()

# -------------------- Assignment B -------------------

def getPointsB(ts):
    points = []
    for t in ts:
        x = math.cos(t) / (1 + math.sin(t) ** 2)
        y = (math.cos(t) * math.sin(t)) / (1 + math.sin(t) ** 2)
        points += [(x, y)]
    return points

def assignmentB():
    steps = 100
    ts = np.linspace(-math.pi, math.pi, steps)

    points = getPointsB(ts)
    xs, ys = unzip(points)

    plt.plot(xs, ys, 'r-')
    plt.show()

# -------------------- Assignment C -------------------

def s(t):
    return 100 / (100 + (t - 0.5 * math.pi) ** 8)

def r(t):
    return s(t) * (2 - math.sin(7 * t) - 0.5 * math.cos(30 * t))

def getPointsC(ts):
    points = []
    for t in ts:
        x = r(t) * math.cos(t)
        y = r(t) * math.sin(t)
        points += [(x, y)]
    return points

def assignmentC():
    steps = 500
    ts = np.linspace(-math.pi * 0.5, math.pi * 1.5, steps)

    points = getPointsC(ts)
    xs, ys = unzip(points)

    plt.plot(xs, ys, 'r-')
    plt.show()

# -------------------- Entry Point --------------------

def main():
    assignmentA()
    assignmentB()
    assignmentC()

if __name__ == "__main__":
    main()
