#! /usr/bin/python3

import math as m 
x1 = 0  		#left side of interval
x2 = 1  		#right side of interval

i = 0   		#index
dx =(x2 - x1)/2 	#avg distance from the root

x = (x1 + x2)/2		#geuss for the root. 
e = 1e-6		#epsilon, required accuracy. Change this to chang accuracy
NMAX = 200		#maximum number of iterations, to prevent an infinite loop

###### Functions

def f(x):		#the function
	a = m.log(1 + x) - m.cos(x)
	return a
while i < NMAX:

	while dx  > e:		# while the avg distance from the root is greater than the required accuracy
		if f(x) == 0:		#check if the midpoint is the root
			print(x)
			break
#check if x is greater than or less than the root. f(x) is increasing, so if f(midpoint) is greater than zero make the midpoint the new upper bound and vice versa.
		elif f(x) > 0:	
			x2 = x
		else:
			x1 = x
		x = ( x1 + x2)/2	
		dx = ( x2 - x1)/2 
		i += 1	
		print('i_{0} = {1}'.format( i, x)) 	
	break

