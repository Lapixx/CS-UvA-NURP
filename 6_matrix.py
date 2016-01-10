#!/usr/bin/env python

"""
Numerical Recipes Project - Matrix
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import numpy as np

def calculateMatrix(m, f, ni, ne):

    res = []

    # check for e = {ni, ni+1 ... ne-2, ne-2}
    for e in range(ni, ne):

        # calculate mn = m^e
        me = m
        # print me
        for x in range(e - 1):
            me = np.dot(me, m)
            # print me

        # save m^e
        res += [me]

    return res

def checkMatrixA():
    an = lambda n: (n - 1) / 4
    a = np.array([
        [-3, -1,   0],
        [ 4,  7, -10],
        [ 4,  3,  -3]
    ])

    res = calculateMatrix(a, an, 1, 6)
    for n in range(1, 6):
        eq = np.array_equal(a, res[n - 1])
        sym = " === " if eq else " =/= "
        exp = "(n = " + str(an(float(n))) + ")"
        print "A^" + str(n) + sym + "A", exp

def checkMatrixB():
    bn = lambda n: n
    b = np.array([
        [-2,  2,  -5],
        [12, -7,  20],
        [ 6, -4,  11]
    ])

    res = calculateMatrix(b, bn, 1, 6)
    for n in range(1, 6):
        eq = np.array_equal(b, res[n - 1])
        sym = " === " if eq else " =/= "
        exp = "(n = " + str(bn(float(n))) + ")"
        print "B^" + str(n) + sym + "B", exp

def checkMatrixC():
    cn = lambda n: n - 2
    c = np.array([
        [-2,  14,  8],
        [-1,  10,  6],
        [ 1, -13, -8]
    ])

    res = calculateMatrix(c, cn, 1, 6)
    zeros = np.zeros((3, 3))
    for n in range(1, 6):
        eq = np.array_equal(zeros, res[n - 1])
        sym = " === " if eq else " =/= "
        exp = "(n = " + str(cn(float(n))) + ")"
        print "C^" + str(n) + sym + "0", exp

# -------------------- Entry Point --------------------

def main():
    checkMatrixA()
    print "----------"
    checkMatrixB()
    print "----------"
    checkMatrixC()

if __name__ == "__main__":
    main()
