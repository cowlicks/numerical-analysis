#! /usr/bin/python
from numpy import *
from ludecomp1 import *

#the algorithm for the c_i's will be different for each boundary condition
#get the eqn that is: c_i terms = a_i terms
#the LHS forms a coeficiant matrix w/ the coeficiants of the c_i's
#the RHS form a colum vector since, this gives a solvable system of eqn's
#solve this w/ tridiagonal solution algorithm
#use the c_i values to solve for the b_i's and d_i's

# the data 

X = array([[0.],[0.5],[1.0],[1.5],[2.]])
Y = array([[0.5],[1.425639],[2.640859],[4.009155],[5.305472]])

yprime = array([[1.5],[2.305472]])

'''
def h(x):
	a = x[2,1] - x[1,1]
	return(a)
'''
h = 0.5

def a(Y):
	A = zeros((3,1), float)
	for i in range(1,2):		#the RHS matrix eqn
		A[i] = (3/h)*(Y[i] - Y[i-1]) - (3/h)*(Y[i-1] - A[i-2])
	A[0] = (3/h)*(Y[2] - Y[1]) - (3/h)*(Y[1] - Y[0])	#beginin' imposed by not a knot BC
	A[-1] = (3/h)*(Y[-1] - Y[-2]) - (3/h)*(Y[-2] - Y[-3]) 	#end of A imposed by notaknot BC				
	return(A)

def c(X):
	k = len(X) - 2
	C = zeros((k,k), float)
	for i in range(1,2):		#the LHS of the matrix eqn
		C[i,i-1] = h
		C[i,i] = 2*(h + h)
		C[i, i+1] = h
	C[0,0] = (3*h + 2*h + h)	#imposed by BC
	C[0,1] = (h - h)
	C[-1,-2] = (h - h)		#imposed by BC
	C[-1, -1] = 3*h + 2*h + h
	return(C)

def cicubicspline(X,Y):
	C = c(X)
	A = a(Y)
	j = solve_tridiagonal(C,A)
	return(j)

def d(C):
	D = zeros((4,1), float)
	for i in range(1,len(X)):
		D[i] = (C[i+1] - C[i])/(3*h)
	D[0] = D[1]
	D[-1] = D[-2]
'''
def b(A,C):
	B = zeros((4,1), float)
	for i in range
'''

cicubicspline(X,Y)
	
