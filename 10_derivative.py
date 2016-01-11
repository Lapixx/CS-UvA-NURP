#!/usr/bin/env python

"""
Numerical Recipes Project - Derivative
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

def dfdt(f, x, dt):
    yi = f(x)
    ye = f(x + dt)
    return (ye - yi) / dt

def main():
    f = lambda t: 3 * t**2 - 2 * t - 1
    x = 1
    print "n    |    df/dt"
    print "---------------"
    for n in range(18):
        q = dfdt(f, x, 10**-n)
        print (" " + str(n) if n < 10 else n), "  |  ", q

if __name__ == "__main__":
    main()
