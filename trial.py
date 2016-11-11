#!usr/bin/env python

#first draft of the code of game of life

import numpy as np
import sys 

def replicating (animals):
	for x in range (1, n):
		for y in range (1, n):
			if total[x,y] >=20:
				if animals[x,y] == 1 and animals[x+1, y] == 0:
					animals[x+1, y] = 1
					print "New animal created on",x,",",y
				if animals[x,y] == 1 and animals[x-1, y] == 0:
					animals[x-1, y] = 1
					print "New animal created on",x,",",y
				if animals[x,y] == 1 and animals[x,y+1] == 0: 
					animals[x, y+1] = 1
					print "New animal created on",x,",",y
				if animals[x,y] == 1 and animals [x, y+1] == 0:
					animals[x, y-1] = 1
					print "New animal created on",x,",",y
			if total[x,y] < 20 and total[x,y] > 10:
				if animals[x,y] == 1 and animals[x+1, y] == 0:
					animals[x+1, y] = 1
					print "New animal created on",x,",",y
				if animals[x,y] == 1 and animals[x-1, y] == 0:
					animals[x-1, y] = 1
					print "New animal created on",x,",",y
				elif animals[x,y] == 1 and animals[x,y+1] == 0: 
					animals[x, y+1] = 1
					print "New animal created on",x,",",y
				elif animals[x,y] == 1 and animals [x, y+1] == 0:
					animals[x, y-1] = 1
					print "New animal created on",x,",",y
			if total[x,y] < 10:
				if animals[x,y] == 1 and animals[x+1, y] == 0:
					animals[x+1, y] = 1
					print "New animal created on",x,",",y
				elif animals[x,y] == 1 and animals[x-1, y] == 0:
					animals[x-1, y] = 1
					print "New animal created on",x,",",y
				elif animals[x,y] == 1 and animals[x,y+1] == 0: 
					animals[x, y+1] = 1
					print "New animal created on",x,",",y
				elif animals[x,y] == 1 and animals [x, y+1] == 0:
					animals[x, y-1] = 1
					print "New animal created on",x,",",y
				
			
