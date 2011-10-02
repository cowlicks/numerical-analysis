#! /usr/bin/python3

import math as m 
i = 0   		#index
x = 1			#geuss for the root.
NMAX = 5		#maximum number of iterations
p = 3**(0.5)

###### Functions
def f(x):		#the function
	a = x**3 + x**2 - 3*x -3
	return a
def df(x):		#the derivative of f
	a = 3*x**2 + 2*x -3
	return a
def newtf(x):		#newtons method eqn
	a = x - f(x)/df(x)
	return a 

###### Implementation
print('part (1)')
while i < NMAX:	
	x = newtf(x) 
	i += 1 

	print('i_{0} = {1}'.format( i, x))
i = 0
x = 1
print('\npart (2)')
while i < NMAX:
	x0 = x
	x = newtf(x) 
	i += 1
	a = m.fabs(x - x0)
	b = m.fabs(x0 - p)
	c = m.fabs(x - p)

	print('|pn - p(n-1)| = {0}\n|p(n-1) - p| = {1}\n|pn - p| = {2}\n'.format(a, b, c))

