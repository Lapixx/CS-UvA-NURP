#!/usr/bin/env python

"""
Numerical Recipes Project - Data visualisation
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

# ----- Utils -----

def sign(x):
    return -1 if x < 0 else 1

def abs(x):
    return -1 * x if x < 0 else x

# ----- Assignment A -----

def bisection_solve(f, a, b, tol=0.001, maxiter=100):
    """
    Find the zero of the function f between a and b using the
    Bisection Method with tolerance tol (default: 0.001) and
    maximum number of iterations equal to maxiter (default: 100)
    """
    for i in range(maxiter):

        # find midpoint p
        p = (b + a) / 2.0

        # calculate values at a, b, p
        ya = f(a)
        yb = f(b)
        yp = f(p)

        # select next bounds
        if not sign(ya) == sign(yp):
            b = p
        else:
            a = p

        rerr = abs((b - a) / (b + a))
        if yp == 0 or rerr < tol:
            return p, (i+1)

    # unable to approximate x within maxiter iterations
    return None

def assignmentA():
    f = lambda x: (x**3) + (2*x) - 1
    for p in range(1, 16):
        x0, iters = bisection_solve(f, 0, 1, 10**-p)
        print "Tolerance 10E-" + str(p) + ": x = " + str(x0) + " (" + str(iters) + " iterations)"
        print "Iterations/tolerance ratio = " + str(iters / float(p))
        print ""

# ----- Assignment B -----

def regula_falsi_solve(f, a, b, tol=0.001, maxiter=100):
    """
    Find the zero of a function f between a and b using the
    Regula Falsi Method with tolerance tol (default: 0.001) and
    maximum number of iterations equal to maxiter (default: 1000)
    """
    for i in range(maxiter):

        # calculate values at a, b
        ya = f(a)
        yb = f(b)

        # find intersection p
        p = b - yb * ((b - a) / float(yb - ya))

        # calculate value at p
        yp = f(p)

        # select next bounds
        if not sign(ya) == sign(yp):
            prevp = b
            b = p
        else:
            prevp = a
            a = p

        diff = abs(prevp - p)
        if yp == 0 or diff < tol:
            return p, (i+1)

    return None

def assignmentB():
    f = lambda x: (x**3) + (2*x) - 1
    for p in range(1, 16):
        x0, iters = regula_falsi_solve(f, 0, 1, 10**-p)
        print "Tolerance 10E-" + str(p) + ": x = " + str(x0) + " (" + str(iters) + " iterations)"
        print "Iterations/tolerance ratio = " + str(iters / float(p))
        print ""

# ----- Entry point -----
def main():
    print "----- Assignment A: Binary Search -----"
    assignmentA()
    print "----- Assignment B: Regula Falsi ----- "
    assignmentB()

if __name__ == "__main__":
    main()
