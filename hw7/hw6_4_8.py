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
	a = (4/3)*(D1(h/2.) - D(h))
	return(a)
def D3(h):
	a = (8/7)*(D2(h/2.) - D2(h))
	return(a)
def D4(h):
	a = (16/15)*(D3(h/2.) - D3(h))
	return(a)

