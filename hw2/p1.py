#! /usr/bin/python3

import math as m 

i = 0   		#index
dx =(x2 - x1)/2 	#avg distance from the root

x = (x1 + x2)/2		#geuss for the root. 
x1 = 0  		#left side of interval
x2 = 1  		#right side of interval
e = 1e-6		#epsilon, required accuracy. Change this to chang accuracy
NMAX = 200		#maximum number of iterations, to prevent an infinite loop

# Functions

def f(x):		#the function
	a = m.log(1 + x) - m.cos(x)
	return a
while i > NMAX:

	while dx  > e:		# while the avg distance from the root is greater than the required accuracy
		if f(x) >
	break
