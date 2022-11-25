#imports
from numpy import arange
from random import randint
from vpython import sphere, rate, vector

#Boundaries and initial positions
L = 101
i = 50
j = 50

#Create a sphere
s=sphere(pos=vector(i,j,0),radius=1)


#Produce a loop for the spehere's motion
for t in arange(1e6):
	rate(100)  #Number of frames/loops per second
	s.pos = vector(i-50,j-50,0)
	a = randint(1,4)	#introduce randomness
    #Conditions for movements
	if a==1: 
		if i==L: continue
		i+=1
	elif a==2:
		if i==0: continue
		i-=1
	elif a==3:
		if j==L: continue
		j+=1
	elif a==4:
		if j==0: continue
		j-=1

    




