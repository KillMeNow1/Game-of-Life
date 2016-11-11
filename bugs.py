#!usr/bin/env python

### This is a version of Conway's Game of Life ###

import numpy as np
import sys 
import math

 
n = 10 #the size of the 2D array 
time = input("How long do you want to run the game for?: ") #length of test run
field = np.zeros((n,n)) #initialisig 2D array of size n representing amount of food, set to 0
total = np.zeros((n,n))
s = 2 #empty space around population at the start at the edges

#initialising 2D array representing presence of an animal with random distribution of 0 and 1; 0 means dead, 1 means alive, in subset of field
population = np.random.randint(2, size = (n-2*s,n-2*s))
empty_1 = np.zeros((n-2*s,s))
empty_2 = np.zeros((s,n))
anim_1 = np.hstack((empty_1, population, empty_1)) 	#adding buffer with 0s of width s to the left and right of population
animals = np.vstack((empty_2, anim_1, empty_2))		#buffer of 2 rows of 0s on top and bottom; now animals dimensions match field

print "The initial animals grid is:\n", animals  #This tells us what the distribution of animals in the grid is before we start the game
a = 4 # amplitude of food growth variation
b = 1 # horizontal shift of food supply
c = 2 # arbitrary constant for rate of food consumption by an animal
breed = input ("What is the rate of breeding?: ") # rate of breeding 
starve = 5 #minimal amount of food that needs to be consumed for an animal to survive


####### Function to evaluate which animals are dying ###############################################################################################################################

def dying (field, animals): 

	for x in range (0, n):
		for y in range (0, n):
		#need to sum different areas around animals depending on if they're at the edges/corners or not
			if (0 < x < n-1 and 0 < y < n-1):
				for x_poz in range (x-1, x+2):
					for y_poz in range (y-1, y+2):
						total[x,y] += field[x_poz, y_poz]	#centre of the grid
			elif x == 0:	
				for x_poz in range (0,x+2):	
					if y == 0:	
						for y_poz in range (0,y+2): 
							total[x,y] += field[x_poz, y_poz]		#(0,0) corner						
					elif y > 0 and y < n-1:
						for y_poz in range ( y-1, y+2):		
							total[x,y] += field[x_poz, y_poz]		# (0, :) column
					elif y == n-1:
						for y_poz in range (n-2, n):
							total[x,y] += field[x_poz, y_poz]		#bottom corner of the column
			elif y == 0: 		
				for y_poz in range (0,y+2):
					if 0 < x and x < n-1:
						for x_poz in range (x-1, x+2):	
							total[x,y] += field[x_poz, y_poz]		# (:, 0) row
					elif x == n-1:
						for x_poz in range (n-2, n): 
							total[x,y] += field[x_poz, y_poz]		#bottom corner of the column
							
			elif x == n-1: 		
				for x_poz in range (n-2,n):
					if 0 < y and y < n-1:
						for y_poz in range ( y-1, y+2):		
							total[x,y] += field[x_poz, y_poz]		#end column of the grid
					elif y == n-1:
						for y_poz in range (n-2, n):  
							total[x,y] += field[x_poz, y_poz]		#end corner of the grid
							
			elif y == n-1:		
				for y_poz in range (n-2,n):
						if 0 < x and x < n-1:
							for x_poz in range ( x-1, x+2):		
								total[x,y] += field[x_poz, y_poz] 	#end row of the grid
								
			#if there is an animal in position x,y and total amount of food is less than minimal, animal dies					
			if total [x,y] < starve:
				if animals[x,y] == 1:
					animals [x,y] = 0
					print "Animal",x,",",y,"is dead at time", t
													
	#print "Food score at time", t+1,"is\n",total
	return
	
	
###################### Breeding function  #########################################################################################################################################
#### as previous function, but there are fewer affected cells as breeding is more restricted and has more conditions ##############################################################
def replicating (animals):
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
						print "New animal created on",x,",",y+1	
			elif (x == n-1 and y == 0):				
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x-1, y] = 1
						print "New animal created on",x-1,",",y	
					if (animals[x,y] == 1 and animals[x, y+1] == 0):
						animals[x,y+1] = 1
						print "New animal created on",x,",",y+1		
			elif (x == n-1 and y == n-1):				
					if (animals[x,y] == 1 and animals[x-1, y] == 0):
						animals[x-1, y] = 1
						print "New animal created on",x-1,",",y	
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
	#print animals				
	return

##################### Main function ###################################################################

for t in range (1,time+1): #our set run time 
	field += a*math.sin((t%12 -b)*math.pi) + t%12 # function to calculate food growth by a trigonometric function taking t as variable 
	#amount a of food is added with every iteration for all positions in field 
	for x in range (0,n):			
		for y in range (0,n): 
			#if an animal lives, all positions distant by 1 around field(x,y) decrease by c if animal present in animals (x,y)
			if animals[x,y] == 1: 	
				#special case for corners and edge rows/columns as can't have negative values or values larger than n		
				if x == 0:	
					for x_poz in range (0,x+2):	
						if y == 0:	
							for y_poz in range (0,y+2): 
								if field[x_poz, y_poz] >= c:
									field[x_poz, y_poz] -= c	#food cannot be negative; need to make sure there's more than c!
									
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
									field[x_poz, y_poz] -= c 		
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
	
	
	dying (field, animals) #calling function to evaluate the which animals are alive
	
	if (t+1)%b == 0:			#b is replication rate and decides how often the replicating function is called
		replicating (animals)

#final print of the status of both the amount of resources after t iterations and number of animals and their positions		
	
print "The state of the field after", t,"is:\n", field	
print "The state of the animals after",t,"is:\n", animals
	

		
	
	
				
	
		
	
			
								

