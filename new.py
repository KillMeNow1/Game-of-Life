#!usr/bin/env python

#writing a function for dying animals

import numpy as np
import sys 

def dying (n, field, animals)
	total = np.zeros((n,n))
	for x, y in range (0, n):
		if animals[x,y] == 1:
			if 0 < x < n-1 and 0 < x < n-1:
				total[x,y] = np.sum(field[[x-1:x+1, y-1:y+1]])
				print total
