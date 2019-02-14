þ# Spencer Riley

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from visual.factorial import *

plt.figure()

N1      = 300
N2      = 200
qtotal  = 100
q1      = 0

kb      = 1.38e-23
k       = 16 # Spring Constant [N/m]
hbar    = 1.0545718e-34 # Planks Constant divided by 2pi [m^2kg/s]
m       = 26.981 * 1.66e-27
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

	dE = hbar * np.sqrt((4*k)/m)
	dS1 = kb * np.abs(np.log(combin(a1+1,b1+1)) - np.log(ways1))
	T1 = dE/dS1

	dS2 = kb * np.abs(np.log(combin(a2+1, b2+1)) - np.log(ways2))
	T2 	= dE/dS2
# Plot number of ways to arrange energy in both:
	Q1T1 = plt.scatter(q1, T1, color='blue', label=r"$q_1$ vs $T_1$")
	Q1T2 = plt.scatter(q1, T2, color='green', label=r"$q_1$ vs $T_2$")

	if np.abs(T2 - T1) <= 1:
		print(q1, q2, T2-T1)
	q1 = q1 + 1
# Plotting Labels, title, etc
plt.legend(handles=[Q1T1, Q1T2])
plt.title("Correlation between the number of quanta\n and the Temperature")
plt.xlabel(r"$q_1$ [quanta]")
plt.ylabel("Temperature [K]")

# Showin the plot
plt.show()

# The values of q1 and q2 at the point of intersection on the
# temperature plot are 60 and 40 quanta respectively. This is
# significant because these values of the number of quanta
# are identical to the point at which the change in entropy is zero.
