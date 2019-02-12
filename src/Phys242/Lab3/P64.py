import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from visual.factorial import *
from visual.graph import *

tempAl = gdots()
tempA2 = gcurve()
tempdata = gdots()


N1      = 105
qtotal  = 300
q1      = 0

kb      = 1.38e-23 			# Boltzmann's Constant
avacado = 6.0221408e23
hbar    = 1.0545718e-34 	# Planks Constant divided by 2pi [m^2kg/s]
mAl     = 26.98 * 1.66e-27 # Atomic Mass of Aluminium [kg]
mPb 	= 207.2 * 1.66e-27 	# Atomic Mass of Peanut Butter [kg]

T_data = [20, 40, 60, 80, 100, 150, 200, 250, 300, 400]
while q1 <= qtotal:
# Calculate number of ways to arrange q1 quanta in 1:
	a1 = q1 + N1 - 1
	b1 = q1
	ways1 = combin(a1, b1)

	def Aluminium():
		C_data = [0.23, 2.09, 5.77, 9.65, 13.04, 18.52, 21.58, 23.25, 24.32, 25.61]

		k = 16  # Spring Constant [N/m]
		dE = hbar * np.sqrt((4 * k) / mAl)
		dS_1 = kb * np.abs(np.log(combin(a1 + 1, b1 + 1)) - np.log(ways1))
		dS_2 = kb * np.abs(np.log(combin(a1 + 2, b1 + 2)) - np.log(combin(a1 + 1, b1 + 1)))

		T_1 = dE/dS_1
		T_2 = dE/dS_2
		dT = T_2 - T_1

		C = (dE/dT) * (1./35.) * avacado
		tempAl.plot(pos=(T_1, C))
		tempA2.plot(pos=(T_1, (3 * kb) * avacado), color=color.cyan)
		for i in range(len(T_data)):
			tempdata.plot(pos=(T_data[i], C_data[i]), color=color.green)
		#if np.abs(T_1 - 100) <= 1:
		#	print("Temp [K]: {:1.2f}; C [J/K/mol]: {:1.2f}".format(T_1, C))

	def Lead():
		C_data = [11.01, 19.57, 22.43, 23.69, 24.43, 25.27, 25.87, 26.36, 26.82, 27.45]

		k = 5  # Spring Constant [N/m]
		dE = hbar * np.sqrt((4 * k) / mPb)
		dS_1 = kb * np.abs(np.log(combin(a1 + 1, b1 + 1)) - np.log(ways1))
		dS_2 = kb * np.abs(np.log(combin(a1 + 2, b1 + 2)) - np.log(combin(a1 + 1, b1 + 1)))

		T_1 = dE/dS_1
		T_2 = dE/dS_2
		dT = T_2 - T_1

		C = (dE/dT) * (1./35.) * avacado
		tempAl.plot(pos=(T_2, C))
		tempA2.plot(pos=(T_1, (3 * kb) * avacado), color=color.cyan)
		for i in range(len(T_data)):
			tempdata.plot(pos=(T_data[i], C_data[i]), color=color.green)
		#if np.abs(T_1 - 100) <= 1:
		#	print("Temp [K]: {:1.2f}; C [J/K/mol]: {:1.2f}".format(T_1, C))
	#Aluminium()
	Lead()
	q1 = q1 + 1