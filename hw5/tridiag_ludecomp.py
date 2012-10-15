import math
import numpy

# Coefficiant matrix and X matrix.
A = numpy.array([   [3., -1., 0., 0.],
                    [1., 4., 2., 0. ],
                    [0., 3., 5., -1.],
                    [0., 0., -2., 7.]])
B = [4., -7., -15, 18.]

def tridiag_ludecomp(A):
    # Initialize the L and U matricies.
    L = numpy.zeros_like(A)
    U = numpy.identity(len(A))
    # First pass.
    L[0, 0] = A[0, 0]
    L[1, 0] = A[1, 0]
    U[0, 1] = A[0, 1]/L[0, 0]

    for k in range( len( A[0])):
        # L_k,k
        try:
            L[k, k] = A[k, k] - L[k, k-1]*U[k-1, k]
        # Do this if out of bounds.
        except IndexError:
            L[k, k] = A[k, k]

        # L_k+1,k
        try:
            L[k + 1, k] = A[k + 1, k]
        except IndexError:
            pass

        # U_k,k+1
        try:
            U[k, k + 1] = A[k, k + 1]/L[k, k]
        except IndexError:
            pass
        
    return L, U

# Backsubstitution to solve L and U.
def backsub(L, U, b):
    # First say Lz = b, then solve for z.
    z = [0] * len(L)
    for k in range(len(L)):
        try:
            z[k] = (1./L[k, k])*(b[k] - L[k, k-1]*z[k-1])
        except IndexError:
            z[k] = (1./L[k, k])*b[k]
    # Now we have Ux = z, so we solve for x.
    x = [0] * len(U)
    # Now going from the bottom up, we need a reversed list of indexes.
    r = range(len(U))
    r.reverse()
    for k in r:
        try:
            x[k] = z[k] - U[k, k+1]*x[k+1]
        except IndexError:
            x[k] = z[k]
    return x

L, U = tridiag_ludecomp(A)
x = backsub(L, U, B)
print x
