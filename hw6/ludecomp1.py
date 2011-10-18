#! /bin/python

from numpy import *

def LUpass(A,k,L,U):				#one 'pass'
	L[k,k] = A[k,k] - L[k,k-1]*U[k-1,k]
	if k < len(A) - 1:
		L[k+1,k] = A[k+1,k]
		U[k,k+1] = A[k,k+1]/L[k,k]

def forwardsub(b,k,L,Z):			#forwardsub solves one element of Z in the eqn LZ=b.
	if k >0:
		Z[k,0] = (b[k,0] - L[k,k-1]*Z[k-1,0])/L[1,1]
	else:
		Z[k,0] = (b[k,0]/L[1,1])

def backsub(k,U,X,Z):				#solve one element of X in the eqn, UX=Z.	
	j = k + len(X) -1
	if k == 0:
		X[j] = Z[j]
	else:
		X[-(k + 1)] = Z[-(k + 1)] - U[-(k + 1),-k]*X[-k]

def solve_tridiagonal(A, b):			#solves the matrix eqn AX=b, wher A is tridiagonal.
	L = zeros((3,3), float)
	U = eye(3)
	k = 0

	while k <= len(A) - 1:			#reduces the matrix A to upper and lower triangular forms.
		LUpass(A,k,L,U)
		k +=1

	k = 0
	Z = zeros((4,1), float)
						
	while k < len(A):			#solve for Z in the eqn LZ=b
		forwardsub(b,k,L,Z)
		k += 1

	k=0

	X = zeros((4,1), float)

	while k < len(X) -1:			#solve for X in the eqn UX=Z
		backsub(k,U,X,Z)
		k += 1
	print(X)

