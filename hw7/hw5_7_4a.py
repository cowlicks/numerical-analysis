#! /usr/bin/python
from math import *
def P(x):
	p = x - 1 + (log(4.) - 1)*(x - 1)**2 + (log(1./8.) + 2)*(x - 1)**2 * (x - 2) + (1./2.)*(log(4.*sqrt(27.)) - 3)*(x - 1)**2 * (x - 2)**2 + (1./2.)*(log(sqrt(48.)/27.) + 1)*(x - 1)**2 * (x - 2)**2 * (x - 3)
	print(p)
