#! /usr/bin/python3



import math as m 
i = 0   		#index
dx = 1		 	#dummy value for dx 

x = 1			#geuss for the root. 
e = 1e-6		#epsilon, required accuracy. Change this to chang accuracy
NMAX = 200		#maximum number of iterations, to prevent an infinite loop

###### Functions

def f(x):		#the function
	a = m.log(1 + x) - m.cos(x)
	return a
def df(x):		#the derivative of f
	a = (1/x) + m.sin(x)
	return a
while i < NMAX:

	while dx  > e:		# while the avg distance from the root is greater than the required accuracy
		if f(x) == 0:		#check if we have the root
			print(x)
			break
#check if x is greater than or less than the root. f(x) is increasing, so if f(midpoint) is greater than zero make the midpoint the new upper bound and vice versa.
		else:
			x0 = x
			x = x - f(x)/(df(x))
		dx = m.fabs(x0 - x)		 
		i += 1
		print('i_{0}={1}'.format( i, x))
	break

