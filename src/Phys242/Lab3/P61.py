# Spencer Riley

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from visual.factorial import *

def parta():
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
		plt.bar(q1, ways1*ways2, width=0.3, color='red')
		q1 = q1+1

def partb():
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
		plt.bar(q1, ways1*ways2, width=0.3, color='red')
		if q1 == 60 and q2 == 40:
			print("\33[92m" + "{}, {}, {}\33[0m".format(q1, q2, ways1*ways2))
		elif q2 == 60 and q1 == 40:
			print("\33[92m" + "{}, {}, {}\33[0m".format(q1, q2, ways1*ways2))
		elif abs((ways1*ways2)) >= 3e+114:
			print("\33[94m" + "{}, {}, {}\33[0m".format(q1, q2, ways1*ways2))
		q1 = q1+1

plt.figure(1)
parta()
plt.title("Correlation between the number of quanta\n and the number of microstates")
plt.xlabel(r"$q_1$ [quanta]")
plt.ylabel(r"ln($\Omega_1\Omega_2$)")

plt.figure(2)
partb()
plt.title("Correlation between the number of quanta\n and the number of microstates")
plt.xlabel(r"$q_1$ [quanta]")
plt.ylabel(r"ln($\Omega_1\Omega_2$)")

plt.show()




