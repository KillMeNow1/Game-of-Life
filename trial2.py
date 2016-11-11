#!usr/bin/env python

import numpy as np
import sys 

n = 5 #the size of the 2D array for both animals and food arrays
time = 2 #length of test run
field = np.zeros((n,n)) #initialisig 2D array of size n representing amount of food, set to 
#initialising 2D array representing presence of an animal with random distribution of 0 and 1; 0 means dead, 1 means alive, in subset of field
s = 1 #space around population
#have this as input and evaluate by if statement
population = np.random.randint(2, size = (n-2*s,n-2*s))
empty_1 = np.zeros((n-2*s,s))
empty_2 = np.zeros((s,n))
anim_1 = np.hstack((empty_1, population, empty_1)) 	#adding buffer with 0s of width s to the left and right of population
animals = np.vstack((empty_2, anim_1, empty_2))		#buffer of 2 rows of 0s on top and bottom; now animals dimensions match field

print "The initial animals grid is:\n", animals 
a = 2 # arbitrary constant for rate of food growth
b = 3 # rate of replication
c = 1 # arbitrary constant for rate of food consumption by an animal

total = np.zeros((n,n))
min_value = 5

field += n-2*s
for t in range (0,time): #our set run time 
	field += a
	#print "Time is:", t, "and field is:", field
	#amount a of food is added with every iteration for all positions in field 
	for x in range (0,n):	
		#print animals
		for y in range (0,n): 
			#if animal alive, all positions distant by 1 around field(x,y) decrease by c if animal present in animals (x,y)
			if animals[x,y] == 1: 	
				#special case for corners and edge rows/columns as can't have negative values or values larger than n		
				if x == 0:	
					for x_poz in range (0,x+2):	
						if y == 0:	
							for y_poz in range (0,y+2): 
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
								total[x, y] += field[x_poz, y_poz]
												
						elif y > 0 and y < n-1:
							for y_poz in range ( y-1, y+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c	#all rows except for first and last
								total[x, y] += field[x_poz, y_poz]
						elif y == n-1:
							for y_poz in range (n-2, n):
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c	#once y == n, i.e. last row
								total[x, y] += field[x_poz, y_poz]
					if total[x,y] < min_value:
						animals[x,y] = 0
						print "Animal at position", x, y, "died at time", t
				elif y == 0: 		
					for y_poz in range (0,y+2):
						if 0 < x and x < n-1:
							for x_poz in range (x-1, x+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c 	# don't need if x == 0 as (0,0) covered previously
								total[x, y] += field[x_poz, y_poz]	
						elif x == n-1:
							for x_poz in range (n-2, n): 
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
								total[x, y] += field[x_poz, y_poz]
					if total[x,y] < min_value:
						animals[x,y] = 0
						print "Animal at position (",x,",",y,") died at time", t
				elif x == n-1: 		
					for x_poz in range (n-2,n):
						if 0 < y and y < n-1:
							for y_poz in range ( y-1, y+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
								total[x, y] += field[x_poz, y_poz]
						elif y == n-1:
							for y_poz in range (n-2, n):  
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
								total[x, y] += field[x_poz, y_poz]
					if total[x,y] < min_value:
						animals[x,y] = 0
						print "Animal at position (",x,",",y,") died at time", t
				elif y == n-1:		
					for y_poz in range (n-2,n):
						if 0 < x and x < n-1:
							for x_poz in range ( x-1, x+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
								total[x, y] += field[x_poz, y_poz]
					if total[x,y] < min_value:
						animals[x,y] = 0
						print "Animal at position (",x,",",y,") died at time", t
				else:
					for x_poz in range (x-1, x+2):
						for y_poz in range (y-1, y+2):
							if field[x_poz, y_poz] >=c:
								field[x_poz, y_poz] -= c
					total[x, y] += field[x_poz, y_poz]
					print "Sum of food at time",t,"is\n",total
					if total[x,y] < min_value:
							animals[x,y] = 0
							print "Animal at position (",x,",",y,") died at time", t
			
	
			#else:
				#if t%b == 0:
				
								
print "At time ",t+1, "the field is:\n",field
