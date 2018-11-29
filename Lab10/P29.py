# Spencer Riley
# Code copied from the book roughly verbatim cause the question told me too
from __future__ import division, print_function
from visual import *
from visual.graph import *

from random import random

Natoms = 10000
#Natoms = 5
#Natoms = 300
#P is the probability for an atom to emit during the time interval dt
P = 0.1
dt = 0.2 # ns
t = 0
tmax = (5 * dt)/P # 5 mean lifetimes

#Create Bar graph
gdisplay(xtitle='t, ns',ytitle='Atoms in excited state', title="Not a Graph")
excited = gvbars(color=color.yellow, delta=dt/2)

while t < tmax:
	rate(1000)
	#SHow number of excited atoms remaining
	excited.plot(pos=(t, Natoms))
	emissions = 0
	atom = 0

	while atom < Natoms:
		if random() < P: #emits?
			# Count emissions in dt
			emissions = emissions + 1
			#print(t)
		atom = atom + 1
	Natoms = Natoms - emissions
# used to get values for Part F for the mean lifetime
	#if Natoms >= 3400:
	#	print(t, Natoms)
	t = t  + dt