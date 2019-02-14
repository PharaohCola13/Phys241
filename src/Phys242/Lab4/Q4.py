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

Pv = 4*pi * (M_N/(2*pi*kb*T))**(3/2) * v**2*exp((-0.5*M_N * v**2)/(kb*T))

avg = average(v)
print(avg)
# Analytic
probable_velocity = sqrt((2*kb*T)/M_N)
plt.axvline(probable_velocity, label=r"$v_{mp}\,=$" + '{:1.2f}'.format(probable_velocity), color="crimson")

# Numerical

# Plots
print("The maximum probability is {:1.3f}".format(max(Pv)))
print("The velocity at the maximum probability is {:1.3f}".format(argmax(Pv)))
plt.scatter(v, Pv, color="green", label="$P(v)$")

## Part B

# Analytic
v_avg = sqrt((8*kb*T)/(pi*M_N))
plt.axvline(v_avg, color="orange", label=r'$v_{avg}=$' + '{:1.2f}'.format(v_avg))

# Numerical

## Part C

# Analytic
v_rms = sqrt((3*kb*T)/M_N)

plt.axvline(v_rms, label=r"$v_{rms}=$"+'{:1.2f}'.format(v_rms), color="deepskyblue")

# Part D

huge = []
for i in range(len(v)):
    if v[i] > 1000:
        huge.append(Pv)
print("The fraction of atoms that have a speed greater than 1000 m/s is {:1.3f} out of {:1.3f}".format(len(huge),len(Pv)))

plt.xlabel("Velocity [m/s]")
plt.ylabel("Velocity Distribution P(v)")
plt.legend()

plt.show()