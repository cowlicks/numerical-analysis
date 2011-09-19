#! /usr/bin/python
#implementation of a gaussian elimination algorithm
from numpy import *

h = 1 		#h indexes the row being manipulated
i = 0 		#i indexes the row of the pivot
j = 0		#j indexes the colum of the pivot
jmax = 2	#number of pivots inc zero
kmax = jmax + 1  

a = array([ (2, -1, 1, -1),
	(4, 2, 1,4),
	(6, -4, 2, -2)], dtype = float)		#augmented matrix

while j < jmax:					#j indexes the columns
	k = h
	if a[i,j] ==0:
		a[i] = a[i] + a[i + 1]  	#err probably not the best way to fix the pivot = zero problem
	if a[i,j] != 1:
		a[i] = (a[i]/(a[i,j]))

	while k < kmax:			
		a[k] = a[k] - a[k, j]*a[i]
		k += 1
	j += 1
	h += 1
	i += 1
h = 1
print(a,i,j)

while j >= 0:
	k = h
	if a[i,j] != 1:
		a[i] = (a[i]/(a[i,j]))

	while k >= 0:
		a[k] = a[k] - a[k,j]*a[i]
		k -= 1
	i -= 1
	j -= 1
	h -= 1
print(a)

