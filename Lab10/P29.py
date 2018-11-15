from __future__ import division, print_function
from visual import *
from visual.graph import *
#from visual.materials import  *

from random import random

Natoms = 10000
# Natoms = 300
#P is the probability for an atom to emit during the time interval dt
P = 0.1
dt = 0.2 # ns
t = 0
tmax = (5 * dt)/P # 5 mean lifetimes

#Create Bar graph
gdisplay(xtitle='t, ns',
		 ytitle='Atoms in excited state', title="Not a Graph")
excited = gvbars(color=color.yellow, delta=dt/2)

while t < tmax:
	rate(1000)
	#SHow number of excited atoms remaining
	excited.plot(pos=(t, Natoms))
	emissions = 0
	atom = 0

	while atom < Natoms:
		if random() < P: #emits?
			if Natoms >= 10000 * 0.368:
				print("Mean Lifetime: {}".format(t))
			# Count emissions in dt
			emissions = emissions + 1
		atom = atom + 1
	Natoms = Natoms - emissions
	t = t  + dt


# Part A) In the if statement where random() is greater than P
# Part B) P = 0.5 for 1 ns
# Part C) Natoms = Natoms - emissions
# Part D) Maximum -> 8.8 ns Minimum -> 1.8 ns
# Part E) ~300 atoms
# Part F) Mean lifetime ~ ??? ns, dt/P = 0.5 ns