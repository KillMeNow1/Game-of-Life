#!usr/bin/env python

#first draft of the code of game of life

import numpy as np
import sys 

#n = raw_input("What's the size of our game?") 
n = 4 #the size of the 2D array for both animals and food arrays
time = 4 #length of test run
field = np.zeros((n,n)) #initialisig 2D array of size n representing amount of food, set to 0
s = 1 #empty space around population at the edges
#have this as input and evaluate by if statement
#initialising 2D array representing presence of an animal with random distribution of 0 and 1; 0 means dead, 1 means alive, in subset of a field
population = np.random.randint(2, size = (n-2*s,n-2*s))
empty_1 = np.zeros((n-2*s,s))
empty_2 = np.zeros((s,n))
anim_1 = np.hstack((empty_1, population, empty_1)) 	#adding buffer with 0s of width s to the left and right of population
animals = np.vstack((empty_2, anim_1, empty_2))		#buffer of 2 rows of 0s on top and bottom; now animals dimensions match field

print "The initial animals grid is:\n", animals 
a = 1 # arbitrary constant for rate of food growth
b = 3 # rate of breeding
c = 1 # arbitrary constant for rate of food consumption by an animal
starve = 3 #minimal amount of food that needs to be consumed for an animal to survive
field += n-2*s #initial amount of food per square set to dimension of population
total = np.zeros((n,n))

####### Function to evaluate which animals are dying ###############################################################################################################################

def dying (field, animals): 
	total = np.zeros((n,n))
	for x in range (0, n):
		for y in range (0, n):
		#need to sum different areas around animals depending on if they're at the edges/corners or not
			if 0 < x < n-1 and 0 < y < n-1:
				for x_poz in range (x-1, x+2):
					for y_poz in range (y-1, y+2):
						total[x,y] += field[x_poz, y_poz]	
			elif x == 0:	
				for x_poz in range (0,x+2):	
					if y == 0:	
						for y_poz in range (0,y+2): 
							total[x,y] += field[x_poz, y_poz]								
					elif y > 0 and y < n-1:
						for y_poz in range ( y-1, y+2):		
							total[x,y] += field[x_poz, y_poz]
					elif y == n-1:
						for y_poz in range (n-2, n):
							total[x,y] += field[x_poz, y_poz]
			elif y == 0: 		
				for y_poz in range (0,y+2):
					if 0 < x and x < n-1:
						for x_poz in range (x-1, x+2):	
							total[x,y] += field[x_poz, y_poz]
					elif x == n-1:
						for x_poz in range (n-2, n): 
							total[x,y] += field[x_poz, y_poz]
							
			elif x == n-1: 		
				for x_poz in range (n-2,n):
					if 0 < y and y < n-1:
						for y_poz in range ( y-1, y+2):		
							total[x,y] += field[x_poz, y_poz]
					elif y == n-1:
						for y_poz in range (n-2, n):  
							total[x,y] += field[x_poz, y_poz]
							
			elif y == n-1:		
				for y_poz in range (n-2,n):
						if 0 < x and x < n-1:
							for x_poz in range ( x-1, x+2):		
								total[x,y] += field[x_poz, y_poz]
								
			#if there is an animal in position x,y and total amount of food is less than minimal, animal dies					
			if total [x,y] < starve:
				if animals[x,y] == 1:
					animals [x,y] = 0
					print "Animal",x,",",y,"is dead at time", t+1
													
	print "Food score at time", t+1,"is\n",total
	return
	
	
###################### Breeding function  #########################################################################################################################################

def replicating (animals, total):
	for x in range (0, n):
		for y in range (0, n):
			if (0 < x < n-1 and 0 < y < n-1):				
					if (animals[x,y] == 1 and animals[x+1,y] == 0):
						animals[x+1, y] = 1
						print "New animal created on",x+1,",",y
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x-1, y] = 1
						print "New animal created on",x-1,",",y
					if (animals[x,y] == 1 and animals[x,y+1] == 0): 
						animals[x, y+1] = 1
						print "New animal created on",x,",",y+1
					if (animals[x,y] == 1 and animals [x, y-1] == 0):
						animals[x, y-1] = 1
						print "New animal created on",x,",",y-1			
			elif (x == 0 and y == 0):				
					if (animals[x,y] == 1 and animals[x+1, y] == 0):
						animals[x+1, y] = 1
						print "New animal created on",x+1,",",y
					if (animals[x,y] == 1 and animals[x, y+1] == 0):
						animals[x,y+1] = 1
						print "New animal created on",x,",",y+1,"at",t		
			elif (x == n-1 and y == 0):				
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x-1, y] = 1
						print "New animal created on",x-1,",",y,"at",t	
					if (animals[x,y] == 1 and animals[x, y+1] == 0):
						animals[x,y+1] = 1
						print "New animal created on",x,",",y+1,"at",t		
			elif (x == n-1 and y == n-1):				
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x-1, y] = 1
						print "New animal created on",x-1,",",y,"at",t	
					if (animals[x,y] == 1 and animals[x, y-1] == 0):
						animals[x,y-1] = 1
						print "New animal created on",x,",",y-1				
			elif (0 < y < n-1 and x == 0):				
					if (animals[x,y] == 1 and animals[x+1, y] == 0):
						animals[x+1, y] = 1
						print "New animal created on",x+1,",",y
					if (animals[x,y] == 1 and animals[x, y+1] == 0):
						animals[x, y+1] = 1
						print "New animal created on",x,",",y+1	
					if (animals[x,y] == 1 and animals[x, y-1] == 0):
						animals[x, y-1] = 1
						print "New animal created on",x,",",y-1	
			elif (0 < y < n-1 and x == n-1):				
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x-1, y] = 1
						print "New animal created on",x-1,",",y
					if (animals[x,y] == 1 and animals[x, y+1] == 0):
						animals[x, y+1] = 1
						print "New animal created on",x,",",y+1	
					if (animals[x,y] == 1 and animals[x, y-1] == 0):
						animals[x, y-1] = 1
						print "New animal created on",x,",",y-1				
			elif (y == n-1 and x == 0):				
					if (animals[x,y] == 1 and animals[x+1, y] == 0):
						animals[x+1, y] = 1
						print "New animal created on",x+1,",",y
					if (animals[x,y] == 1 and animals[x, y-1] == 0):
						animals[x,y-1] = 1
						print "New animal created on",x,",",y-1					
			elif (y == 0 and 0 < x < n-1):	
					if (animals[x,y] == 1 and animals[x+1, y] == 0):
						animals[x+1, y] = 1
						print "New animal created on",x+1,",",y
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x-1, y] = 1
						print "New animal created on",x-1,",",y	
					if (animals[x,y] == 1 and animals[x, y+1] == 0):
						animals[x, y+1] = 1
						print "New animal created on",x,",",y+1
			elif (y == n-1 and 0 < x < n-1):	
					if (animals[x,y] == 1 and animals[x+1, y] == 0):
						animals[x+1, y] = 1
						print "New animal created on",x+1,",",y
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x, y-1] = 1
						print "New animal created on",x,",",y-1	
					if (animals[x,y] == 1 and animals[x, y-1] == 0):
						animals[x, y-1] = 1
						print "New animal created on",x,",",y-1			
	print animals				
	return

##################### Main function ###################################################################

for t in range (0,time): #our set run time 
	field += a
	#print "Time is:", t, "and field is:", field
	#amount a of food is added with every iteration for all positions in field 
	for x in range (0,n):			
		for y in range (0,n): 
			#if an animal alives, all positions distant by 1 around field(x,y) decrease by c if animal present in animals (x,y)
			if animals[x,y] == 1: 	
				#special case for corners and edge rows/columns as can't have negative values or values larger than n		
				if x == 0:	
					for x_poz in range (0,x+2):	
						if y == 0:	
							for y_poz in range (0,y+2): 
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
									
						elif y > 0 and y < n-1:
							for y_poz in range ( y-1, y+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c	#all rows except for first and last
						elif y == n-1:
							for y_poz in range (n-2, n):
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c	#once y == n, i.e. last row
				elif y == 0: 		
					for y_poz in range (0,y+2):
						if 0 < x and x < n-1:
							for x_poz in range (x-1, x+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c 	# don't need if x == 0 as (0,0) covered previously	
						elif x == n-1:
							for x_poz in range (n-2, n): 
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
				elif x == n-1: 		
					for x_poz in range (n-2,n):
						if 0 < y and y < n-1:
							for y_poz in range ( y-1, y+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
						elif y == n-1:
							for y_poz in range (n-2, n):  
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
				elif y == n-1:		
					for y_poz in range (n-2,n):
						if 0 < x and x < n-1:
							for x_poz in range ( x-1, x+2):		
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c
				else:
					for x_poz in range (x-1, x+2):
						for y_poz in range (y-1, y+2):
							if field[x_poz, y_poz] >=c:
								field[x_poz, y_poz] -= c
	
	
	dying (field, animals) 
	
	if (t+1)%b == 0:
		replicating (animals, total)
		
	
print "Field is:\n", field
print "Animals are:\n", animals
	

		
	
	
				
	
		
	
			
								

