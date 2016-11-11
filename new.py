#!usr/bin/env python

#first draft of the code of game of life

import numpy as np
import sys 

#n = raw_input("What's the size of our game?") 
n = 5 #the size of the 2D array for both animals and food arrays
time = 2 #length of test run
field = np.ones((n,n)) #initialisig 2D array of size n representing amount of food, set to 4
#initialising 2D array representing presence of an animal with random distribution of 0 and 1; 0 means dead, 1 means alive
animals = np.random.randint(2, size = (n,n))

print "The initial animals grid is:\n", animals 
a = 2 # arbitrary constant for rate of food growth
c = 1 # arbitrary constant for rate of food consumption by an animal


for t in range (0,time): #our set run time 
	field += a
	#print "Time is:", t, "and field is:", field
	#amount a of food is added with every iteration for all positions in field 
	for x in range (0,n):	
		#print animals
		for y in range (0,n): 
			#if animal alive, all positions distant by 1 around field(x,y) decrease by c if animal present in animals (x,y)
			if (animals[x,y] == 1): 
				#print field, animals	
				#special case for corners and edge rows/columns as can't have negative values or values larger than n		
				if (x == 0):	
					for x_poz in range (0,2):	
						if (y == 0):	
							for y_poz in range (0,2): 
								field[x_poz, y_poz] -= c
									
						elif y > 0 and y < n-1:
							for y_poz in range ( y-1, y+2):		
								field[x_poz, y_poz] -= c	#all rows except for first and last
						elif (y == n-1):
							for y_poz in range (n-2, n):
								field[x_poz, y_poz] -= c	#once y == n, i.e. last row
				elif (y == 0): 		
					for y_poz in range (0,2):
						if 0 < x and x < n-1:
							for x_poz in range (x-1, x+2):		
								field[x_poz, y_poz] -= c 	# don't need if x == 0 as (0,0) covered previously	
						elif (x == n-1):
							for x_poz in range (n-2, n): 
								field[x_poz, y_poz] -= c
				elif (x == n-1): 		
					for x_poz in range (n-2,n):
						if 0 < y and y < n-1:
							for y_poz in range ( y-1, y+2):		
								field[x_poz, y_poz] -= c
						elif (y == n-1):
							for y_poz in range (n-2, n):  
								field[x_poz, y_poz] -= c
				elif (y == n-1):		
					for y_poz in range (n-2,n):
						if 0 < x and x < n-1:
							for x_poz in range ( x-1, x+1):		
								field[x_poz, y_poz] -= c
				#else:
					#for x_poz in range (x-1, x+2):
						#for y_poz in range (y-1, y+2):
							#field[x_poz, y_poz] -= c
							
print "At time 1, the field is:\n",field
