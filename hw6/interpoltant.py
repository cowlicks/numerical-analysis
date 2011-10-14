#! /usr/bin/python3

#function to solve problem 5.5.1 in Bradie's Numerical analysis book

#t is the temperature the interpolant is evaluated at
#T1 and T2 are the temperatures nearest to t
#mu1 and mu2 are the densities corresponding to T1 and T2 respectively

def mu(t,mu1,mu2,T1,T2):
	mu = mu1 + ((mu2 - mu1)/(T2 - T1))*(t - T1)
	print(mu)

