#! /bin/python

from numpy import *

A = array([[3, -1, 0, 0],
	[1, 4, 2, 0],
	[0, 3, 5, -1],
	[0, 0, -2, 7]])

b = array([[4],[-7],[-15],[18]])

L = zeros((4,4), float)
U = eye(4)
k = 0

def LUpass(k):
	L[k,k] = A[k,k] - L[k,k-1]*U[k-1,k]
	if k < len(A) - 1:
		L[k+1,k] = A[k+1,k]
		U[k,k+1] = A[k,k+1]/L[k,k]
	
while k <= len(A) - 1:
	LUpass(k)
	k +=1

k = 0
Z = zeros((4,1), float)

def forsub(k):
	if k >0:
		Z[k,0] = (b[k,0] - L[k,k-1]*Z[k-1,0])/L[1,1]
	else:
		Z[k,0] = (b[k,0]/L[1,1])
while k < len(A):
	forsub(k)
	k += 1

k=0

X = zeros((4,1), float)

def backsub(k):
	j = k + len(X) -1
	if k == 0:
		X[j] = Z[j]
	else:
		X[-(k + 1)] = Z[-(k + 1)] - U[-(k + 1),-k]*X[-k]
while k < len(X):
	backsub(k)
	k += 1
print(X)
