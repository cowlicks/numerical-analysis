#! /usr/bin/python3


'''
Section 2.1-
 Verify that each of the following equations has a root on the interval
(0,1). Next, perform the bisection method to determine p3, the third
approximation to the location of the root, and to determine (a4,b4), the
next enclosing interval:
 a) ln(1+x)-cos(x) = 0
 c) e^(-x) - x = 0
'''

'''
this program preforms the bisection method.
'''

import math as m

x1 = 0
x2 = 1
i = 0

p = int(input('number of iterations to preform:'))

while i < p:
	xm = (x1 + x2)/2
	x = xm
	f = m.log(1 + x) - m.cos(x)
	g =  m.e**(-x) - x 
	i += 1
	if g <= xm:
		x2 = xm

	else:
		x1 = xm
	print(xm)

print(xm)


