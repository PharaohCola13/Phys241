# Spencer Riley
from numpy import *
import matplotlib
from matplotlib import pyplot as plt

fname = "./velocities.txt"
file = open(fname, "r")

time = loadtxt(fname, skiprows=1, unpack=True)[0]
velx = loadtxt(fname, skiprows=1, unpack=True)[1]

xi = time[0]
xf = time[-1]
dx = time[1] - time[0]

x = arange(xi, xf + dx, dx)

Int = 0
Int_calc = []
plt.figure(2)
for i in range(len(x)):
    Int = Int + dx/3 * (velx[0] + 4*velx[i-1] + velx[i])
    Int_calc.append(Int)

plt.scatter(time, Int_calc, color="deepskyblue")
plt.title("Time vs. Displacement of the object in the x-direction")
plt.xlabel("Time [s]")
plt.ylabel("Position [m]")

plt.figure(1)
plt.scatter(time, velx, color="crimson")
plt.title("Time vs. Velocity of the object in the x-direction")
plt.xlabel("Time [s]")
plt.ylabel("Velocity [m/s]")
plt.show()