# Spencer Riley

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from visual.factorial import *

plt.figure()

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
	One = plt.scatter(q1, np.log(ways1), color='blue', label=r"ln($\Omega_1$)")
	Two = plt.scatter(q1, np.log(ways2), color='green', label=r"ln($\Omega_2$)")
	All = plt.scatter(q1, np.log(ways1*ways2), color='red', label=r"ln($\Omega_1\Omega_2$)")
	if q1 == 60 and q2 == 40:
		print(q1, q2, np.log(ways1*ways2))
	q1 = q1 + 1
# Plots the point of maximum q1
Max = plt.axvline(60, color='black', label=r"$q_1 = 60$")
# Labels, Title, etc for the plot
plt.legend(handles=[One, Two, All, Max])
plt.title("Correlation between the number of quanta and the number of microstates.")
plt.xlabel(r"$q_1$ [quanta]")
plt.ylabel(r"ln($\Omega$)")

# Showin the plot
plt.show()

# The significance of value of maximum value of q1, 60, is that
# the change in entropy with respect to q1 is zero.

