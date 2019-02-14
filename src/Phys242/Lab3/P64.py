# Spencer Riley

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from visual.factorial import *

# Plotting environments
plt.figure(1)
plt.figure(2)

# Used for plotting the Calculated data outside of the functions
T_Al = []
C_Al = []

T_Pb = []
C_Pb = []

# Temperature Data from the Question
T_data = [20, 40, 60, 80, 100, 150, 200, 250, 300, 400]

N1      = 105 	# Number of Oscillators
qtotal  = 300 	# Total Number of Quanta
q1      = 0		# Initial value of quanta

kb      = 1.38e-23 			# Boltzmann's Constant
avacado = 6.0221408e23		# Avacado's Number [atms/mol]
hbar    = 1.0545718e-34 	# Planks Constant divided by 2pi [m^2kg/s]
mAl     = 26.98 * 1.66e-27 	# Atomic Mass of Aluminium [kg]
mPb 	= 207.2 * 1.66e-27 	# Atomic Mass of Peanut Butter [kg]

def Aluminium():
	C_data = [0.23, 2.09, 5.77, 9.65, 13.04, 18.52, 21.58, 23.25, 24.32, 25.61]

# Spring Constant [N/m]
	k = 16
# Change in energy [J/atm]
	dE = hbar * np.sqrt((4 * k) / mAl)
# Calculations for the change in entropy
	dS_1 = kb * np.abs(np.log(combin(a1 + 1, b1 + 1)) - np.log(ways1))
	dS_2 = kb * np.abs(np.log(combin(a1 + 2, b1 + 2)) - np.log(combin(a1 + 1, b1 + 1)))
# Temperature Calculations [K]
	T_1 = dE/dS_1
	T_2 = dE/dS_2
	dT = T_2 - T_1
# Specific Heat of Aluminum [J/K/mol]
	C = (dE/dT) * (1./35.) * avacado
# Plotting
	plt.figure(1)
	Al_Data = plt.scatter(T_data, C_data, color='red', label="Expected C$_{Al}$")
	#if np.abs(T_1 - 100) <= 1:
	#	print("Temp [K]: {:1.2f}; C [J/K/mol]: {:1.2f}".format(T_1, C))
	return T_1, C, Al_Data
def Lead():
# Specific Heat data from the question
	C_data = [11.01, 19.57, 22.43, 23.69, 24.43, 25.27, 25.87, 26.36, 26.82, 27.45]
# Spring Constant [N/m]
	k = 5
# Energy Calculation [J/atm]
	dE = hbar * np.sqrt((4 * k) / mPb)
# Calculations for the change in energy
	dS_1 = kb * np.abs(np.log(combin(a1 + 1, b1 + 1)) - np.log(ways1))
	dS_2 = kb * np.abs(np.log(combin(a1 + 2, b1 + 2)) - np.log(combin(a1 + 1, b1 + 1)))
# Temperature Calculations [K]
	T_1 = dE/dS_1
	T_2 = dE/dS_2
	dT = T_2 - T_1
# Specific Heat of Lead [J/K/mol]
	C = (dE/dT) * (1./35.) * avacado
# Plotting
	plt.figure(2)
	Pb_Data = plt.scatter(T_data, C_data, color='red', label="Expected C$_{Pb}$")
	return T_1, C, Pb_Data

while q1 <= qtotal:
# Calculate number of ways to arrange q1 quanta in 1:
	a1 = q1 + N1 - 1
	b1 = q1
	ways1 = combin(a1, b1)
# Aluminium Function is called and puts the returned values into a list
	T_1, C, Al_Data = Aluminium()
	T_Al.append(T_1)
	C_Al.append(C)
# Lead Function is called and puts the returned values into a list
	T_1, C, Pb_Data = Lead()
	T_Pb.append(T_1)
	C_Pb.append(C)

	q1 = q1 + 1

# Plots the calculated values of Specific Heat against Temperature
# Aluminium Plotting
plt.figure(1)
plt.title("Correlation between Temperature and Specific Heat per mol in Aluminium")
Kb_cons = plt.axhline((3 * kb) * avacado, color='green', label=r"$3\cdot k_b$")
Al_Calc = plt.scatter(T_Al,C_Al, color='blue', label=r"Calculated C$_{Al}$")

plt.legend(handles=[Al_Data, Al_Calc, Kb_cons])
plt.xlabel("Temperature [K]")
plt.ylabel("Specific Heat [J/K/mol]")

# Lead Plotting
plt.figure(2)
plt.title("Correlation between Temperature and Specific Heat per mol in Lead")
Kb_cons = plt.axhline((3 * kb) * avacado, color='green', label=r"$3\cdot k_b$")
Pb_Calc = plt.scatter(T_Pb, C_Pb, color='blue', label=r"Calculated C$_{Pb}$")

plt.legend(handles=[Pb_Data, Pb_Calc, Kb_cons])
plt.xlabel("Temperature [K]")
plt.ylabel("Specific Heat [J/K/mol]")

# Showin the plots
plt.show()