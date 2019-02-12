import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from visual.factorial import *
from visual.graph import *
from random import random


def parta():
	waygraph = gvbars(delta=0.3, color=color.red)

	Ntotal  = 6      # total number of oscillators
	N1      = 3      # number of oscillators in object 1
	N2      = 3      # number of oscillators in object 2
	qtotal  = 4      # total quanta of energy available
	q1      = 0      # initially 0 quanta in object 1
	while q1 <= qtotal: # for each possible value of energy in 1
		q2  = qtotal - q1         # number of quanta of energy in 2
	# Calculate number of ways to arrange q1 quanta in 1:
		a1 = q1 + N1 - 1
		b1 = q1
		ways1 = combin(a1, b1)
	# Calculate number of ways to arrange q2 quanta in 2:
		a2 = q2 + N2 - 1
		b2 = q2
		ways2 = combin(a2, b2)
	# Plot number of ways to arrange energy in both:
		waygraph.plot(pos=(q1, ways1*ways2))
		q1 = q1+1

def partb():
	waygraph = gvbars(delta=0.3, color=color.red)

	N1      = 300
	N2      = 200
	qtotal  = 100
	q1      = 0
	while q1 <= qtotal: # for each possible value of energy in 1
		q2  = qtotal - q1         # number of quanta of energy in 2
	# Calculate number of ways to arrange q1 quanta in 1:
		a1 = q1 + N1 - 1
		b1 = q1
		ways1 = combin(a1, b1)
	# Calculate number of ways to arrange q2 quanta in 2:
		a2 = q2 + N2 - 1
		b2 = q2
		ways2 = combin(a2, b2)
	# Plot number of ways to arrange energy in both:
		plot = waygraph.plot(pos=(q1, ways1*ways2))
		#plot = plt.hist(q1, ways1*ways2)
		if q1 == 60 and q2 == 40:
			print("\33[92m" + "{}, {}, {}\33[0m".format(q1, q2, ways1*ways2))
		elif q2 == 60 and q1 == 40:
			print("\33[92m" + "{}, {}, {}\33[0m".format(q1, q2, ways1*ways2))
		elif abs((ways1*ways2 - float(((6.86630544448e+114)/2.)))) == float(((6.86630544448e+114)/2.)):
			print("\33[94m" + "{}, {}, {}\33[0m".format(q1, q2, ways1*ways2))
		q1 = q1+1
	return plot

def partc():
	Ntotal  = 500
	qtotal  = 100
	q1      = 0
	N1      = 0
	N2      = Ntotal - N1
	while q1 <= qtotal: # for each possible value of energy in 1
		q2  = qtotal - q1         # number of quanta of energy in 2
	# Calculate number of ways to arrange q1 quanta in 1:
		a1 = q1 + N1 - 1
		b1 = q1
		ways1 = combin(a1, b1)
	# Calculate number of ways to arrange q2 quanta in 2:
		a2 = q2 + N2 - 1
		b2 = q2
		ways2 = combin(a2, b2)
		q1 = q1+1
	return ways1 * ways2

parta()
partb()
#partc() #Needs work, Ihave no fucking idea what to do.



