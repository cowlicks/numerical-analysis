#! /usr/bin/python
#implementation of a gaussian elimination algorithm
from numpy import *

h = 1 		#h indexes the row being manipulated
i = 0 		#i indexes the row of the pivot
j = 0		#j indexes the colum of the pivot
jmax = 3	#number of pivots inc zero
kmax = jmax + 1 

a = array([ (1, 1, 1, 1, 1),
	(1, 1, 2, 3, 2),
	(-1, 0, 2, 1, 1),
	(3, 2, -1, 0, 1) ], dtype = float)	#augmented matrix

while j < jmax:				
	k = h
<<<<<<< HEAD
	while a[i,j] ==0:			#solves the pivot = zero problem
		m = i
		a[m] = a[m] + a[m + 1]
		m += 1
=======
	while a[i,j] ==0:
		n = i
		a[n] = a[n] + a[n + 1]
		n += 1
>>>>>>> c69cf1af71a258e5b2129e07cebcb37eacef69ba
	if a[i,j] != 1:
		a[i] = (a[i]/(a[i,j]))

	while k < kmax:			
		a[k] = a[k] - a[k, j]*a[i]
		k += 1
	j += 1
	h += 1
	i += 1
<<<<<<< HEAD
h = 2
print(a) 	#at this point the matrix has been gaussian eliminated, the rest of the algorith solves the system.
=======
h = 2		#at this point the matrix is in upper triangular form.
>>>>>>> c69cf1af71a258e5b2129e07cebcb37eacef69ba
while j >= 0:
	k = h
	while k >= 0:		#removes the pivot = zero problem
		a[k] = a[k] - a[k,j]*a[i]
		k -= 1
	i -= 1
	j -= 1
	h -= 1
print(a)

