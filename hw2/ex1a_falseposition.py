#! /usr/bin/python3
#this problem permutes the method of fals position 3 times to find the of a function.



import math as m 
x1 = 0  		#left side of interval
x2 = 1  		#right side of interval
i = 0   		#index

def f(x):		#the function
	a = m.log(1 + x) - m.cos(x)
	return a
def g(x, y):
	a = y - f(y)*((y - x)/(f(y) - f(x)))
	return a
while i < 5:		#chane the number that i is less than to increase number of iterations
	p = g(x1, x2)
	if (p * f(x1)) < 0:
		x1 = p
	else:
		x2 = p
	i += 1	
	print('p_{0} = {1} and the interval {2} - {3}'.format( i, p, x1, x2)) 	
	
