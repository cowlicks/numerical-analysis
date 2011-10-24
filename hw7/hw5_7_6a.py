#! /usr/bin/python
#hermite interpolant for problem 5.7.4
from math import *
def P(x):
	p = (1/26.) + (50./(26.**2))*(x + 1) + (150./169.)*(x + 1)**2 - (625./338.)*(x + 1)**2 * x - (625./676.)*(x + 1)**2 * x**2 + (625./676.)*(x + 1)**2 * x**2 * (x - 1)
	return(p)
def f(x):
	f = 1/(1 + 25.*x*x)
	return(f)


