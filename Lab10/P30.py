# Spencer Riley
# Code copied from the book verbatim cause the question told me too

from visual import *
from visual.graph import *
from random import random

# Start with 100 atoms in an excited state
# (try larger or smaller numbers)

Natoms = 100
# P is the probability for an atom to emit
# during a time interval dt
P = 0.1

# Pgreen is the probability that when an
# atom emits, it emits a green photon
Pgreen = 0.3

dt = 0.2 # ns
t = 0
tmax = 5*dt/P # 5 mean lifetimes

# Create bar graphs
gdisplay(xtitle='t, ns', xmax=tmax,
		 ytitle='Emissions of green photons')

greeng = gvbars(color=color.green, delta=dt/2)

#gdisplay(y=400, xtitle='t, ns', xmax=tmax,
#		 ytitle='Emissions of red photons')
#redg = gvbars(color=color.red, delta=dt/2)

greens = reds = 0
while t < tmax:
	rate(100)
	atom = 0
	g = r = 0
	while atom < Natoms:
		if random() < P: # emits?
			if random() < Pgreen: # green?
				g = g + 1
			else:
	# emits red
				r = r + 1
		atom = atom + 1
	greeng.plot(pos=(t,g))
#	redg.plot(pos=(t,r))
	greens = greens + g
	reds = reds + r
	Natoms = Natoms - (g + r)
	t = t + dt
print(greens,'green emissions,',reds,'red emissions')

# Part A) Emission of photons vs time in ns
# Part B) Red Photons
# Part C) The emission of green photons do not vary significantly
# Part D) Experimental Average = 29.933; fraction of trails within the range = 25/30
# Range = 30 +- 5