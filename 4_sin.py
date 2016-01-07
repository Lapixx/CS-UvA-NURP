#!/usr/bin/env python

"""
Numerical Recipes Project - Approximate Sine Function
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import math
import random

def partialSine(x, k):
    a = (-1) ** k
    b = math.factorial(2 * k + 1)
    c = x ** (2 * k + 1)
    return float(a) / float(b) * float(c)

def approxSine(x, p):
    max_err = 10 ** (-p)
    y = 0
    k = 0
    while 1:
        y += partialSine(x, k)
        exact = math.sin(x)
        err = math.fabs(exact - y)
        if err <= max_err:
            return (y, k)
        k += 1

def calculateRequiredK(p):
    iterations = 100000
    max_k = -1
    for i in range(iterations):
        x = random.uniform(0, 0.5)
        _, k = approxSine(x, p)
        if k > max_k:
            max_k = k
    return max_k

def main():

    for i in range(10):
        p = i + 1
        k = calculateRequiredK(p)
        print "Max error 10E-" + str(p) + " => K: " + str(k)

if __name__ == "__main__":
    main()
