#!usr/bin/env python


import numpy as np
import sys 

n = 5
field = np.zeros ((n,n))
animals = np.random.randint(2, size = (n,n))
#print (field)
#print (animals)
a = 2
c = 1


for t in range (0,100):
	field = t*a
	for x in range (0,5):
		for y in range (0,5):
			if animals (x,y) == 1:
				if (x == 0 and y == 0)
					for x_poz in range (x,x+2):
						for y_poz in range (y, y+2):
							field(x_poz, y_poz) -= c
				if (x == n and y == n)
					for x_poz in range (x-1, x+1):
						for y_poz in range (y -1, y+1):
							field(x_poz, y_poz) -=c
				if (x==0 and y == n)
					for x_poz in range (x, x+2):
						
						
						if (t%3 == 0):
							print (field)
							print (animals)

