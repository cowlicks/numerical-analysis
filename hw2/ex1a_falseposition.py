#! /usr/bin/python3
#this problem permutes the method of false position 3 times to find the root of the givin function

import math as m 
x1 = 0  		#left side of interval
x2 = 1  		#right side of interval
i = 0   		#index
NMAX = 5 		#maximum # of iterations

def f(x):		#the function
	a = m.log(1 + x) - m.cos(x)
	return a
def g(x, y):		#the method of false position in eqn form
	a = y - f(y)*((y - x)/(f(y) - f(x)))
	return a
while i <= NMAX:	
	p = g(x1, x2)
	print('p_{0} = {1} and the interval ({2}, {3})'.format( i, p, x1, x2)) 
	#formated to print a nice answer
	if (p * f(x1)) < 0:
		x1 = p
	else:
		x2 = p
	i += 1	
