#! /usr/bin/python3

from math import *

xo = 1 #center

#the function

def f(x):
	a = log(x*x + 1)
	return(a)

#backwards difference approximation of derivative

def D1(h):
	a = (f(xo) - f(xo - h))/h
	return(a)

#lower order formulas

def D2(h):
	a = (1/3)*(4*D1(h/2.) - D1(h))
	return(a)
def D3(h):
	a = (1/7.)*(8*D2(h/2.) - D2(h))
	return(a)
def D4(h):
	a = (1/15.)*(16*D3(h/2.) - D3(h))
	return(a)

