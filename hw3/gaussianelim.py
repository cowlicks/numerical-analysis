#! /usr/bin/python
#implementation of a gaussian elimination algorithm
#TODO rewrite to rearrange rows from greatest to largest when shifting to the next column
import numpy as np

h = 1
i = 0 					#indicies 		
j = 0


a = np.array([ (1, 1, 1, 1, 1),
	(1, 1, 2, 3, 2),
	(-1, 0, 2, 1, 1),
	(3, 2, -1, 0, 1) ])		 #augmented matrix

while j < 3:
	k = h
	if a[i,j] != 1:
		a[i] = a[i]/float(a[i,j])

	while k < 4:			
		a[k] = a[k] - a[k, j]*a[i]
		k += 1
	j += 1
	h += 1
	i += 1
print(a, h, i, j, k)
	






