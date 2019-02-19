# Spencer Riley
from numpy import *
import matplotlib
from matplotlib import pyplot as plt

plt.figure()

u    = 1.66e-27
M_N  = 14 * u
T    = 230 # [K]
kb   = 1.38e-23
v    = arange(0, 1500, 1)

## Part A
print("\33[93m" + "---"*5 + " Part A " + "---"*5 + "\33[0m")

Pv = 4*pi * (M_N/(2*pi*kb*T))**(3/2) * v**2*exp((-0.5*M_N * v**2)/(kb*T))

# Analytic
probable_velocity = sqrt((2*kb*T)/M_N)
print("The analytical solution for the most probable velocity is {:1.3f} m/s".format(probable_velocity))
plt.axvline(probable_velocity, label=r"$v_{mp}\,=$" + '{:1.2f}'.format(probable_velocity), color="crimson")
# Numerical
nummax 	= max(Pv)
numvel 	= argmax(Pv)
print("The numerical solution for the most probable velocity is {:1.3f} m/s".format(numvel))
print("The maximum probability is {:1.3f}".format(nummax))
# Comparison
comparea = probable_velocity - numvel
print("Comparison for the most probable velocity is {:1.3f} m/s".format(comparea))
# Plots
plt.scatter(v, Pv, color="green", label="$P(v)$")

## Part B
print("\33[93m" + "---"*5 + " Part B " + "---"*5 + "\33[0m")
# Analytic
v_avg = sqrt((8*kb*T)/(pi*M_N))
plt.axvline(v_avg, color="orange", label=r'$v_{avg}=$' + '{:1.2f}'.format(v_avg))
print("The analytical solution for the average velocity is {:1.3f} m/s".format(v_avg))
# Numerical
def numavg():
	xi = 1
	xf = 1500
	dx = 1
	x = arange(xi, xf + dx, dx)
	Int = 0
	Int1 = 0
	for j in range(1, len(x)):
		try:
			Int 	= Int + j/3. * (Pv[j] + 4*Pv[j+1] + Pv[j+2]) * j
			Int1 	= Int1 + j/3. * (Pv[j] + 4*Pv[j+1] + Pv[j+2])
			avg 	= float(Int)/float(Int1)
		except IndexError:
			continue
	return avg
print("The numerical solution for the average velocity is {:1.3f} m/s".format(numavg()))
# Comparison
compareb = v_avg - numavg()
print("Comparison for the average velocity is {:1.3f} m/s".format(compareb))

## Part C
print("\33[93m" + "---"*5 + " Part C " + "---"*5 + "\33[0m")
# Analytic
v_rms = sqrt((3*kb*T)/M_N)
print("The analytical solution for the root mean squared velocity is {:1.3f} m/s".format(v_rms))
plt.axvline(v_rms, label=r"$v_{rms}=$"+'{:1.2f}'.format(v_rms), color="deepskyblue")
# Numerical
def numrms():
	xi = 1
	xf = 1500
	dx = 1
	x = arange(xi, xf + dx, dx)
	Int = 0
	Int1 = 0
	for j in range(1, len(x)):
		try:
			Int 	= Int + float(j)/3. * ((Pv[j])**2 + 4*(Pv[j+1])**2 + (Pv[j+2])**2) * j**2
			Int1 	= Int1 + float(j)/3. * ((Pv[j])**2 + 4*(Pv[j+1])**2 + (Pv[j+2])**2)
			rms 	= sqrt(float(Int)/float(Int1))
		except IndexError:
			continue
	return rms
print("The numerical solution for the root mean squared velocity is {:1.3f} m/s".format(numrms()))
# Comparison
comparec = v_rms - numrms()
print("Comparison for the root mean squared velocity is {:1.3f} m/s".format(comparec))

# Part D
print("\33[93m" + "---"*5 + " Part D " + "---"*5 + "\33[0m")
huge = []
for i in range(len(v)):
    if v[i] > 1000:
        huge.append(Pv)
print("The fraction of atoms that have a speed greater than 1000 m/s is {:1.3f}".format(float(len(huge))/float(len(Pv))))

plt.xlabel("Velocity [m/s]")
plt.ylabel("Velocity Distribution P(v)")
plt.legend()

plt.show()
