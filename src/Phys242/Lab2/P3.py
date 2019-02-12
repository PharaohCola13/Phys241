# Spencer Riley
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

fname = "./phys_pend.txt"
file = open(fname, "r")

time    = np.loadtxt(fname, skiprows=1, unpack=True)[0]
theta   = np.loadtxt(fname, skiprows=1, unpack=True)[1]
omega   = np.loadtxt(fname, skiprows=1, unpack=True)[2]

f = np.deg2rad(theta)
Nd = np.zeros(len(theta))

def centered(a,f):
    print("Starting Centered Derivative Calculations")
    i = 0
    y = []
    while i <= len(a)-1:
        if i == 0:
            Nd[i] = (f[i+1] - f[i])/(a[i+1]-a[i])
        elif i == len(a)-1:
            Nd[i] = (f[i]-f[i-1])/(a[i]-a[i-1])
        else:
            Nd[i] = (f[i+1]-f[i-1])/(a[i+1]-a[i-1])
        y.append(Nd[i])
        i = i + 1
    print("Completed")
    return y

plt.figure(1)
plt.plot(time, theta, label=r"$\theta$")
plt.xlabel("Time [s]")
plt.ylabel("Angle [$^o$]")
plt.legend()

plt.figure(2)
plt.plot(time, omega, label=r"$\omega$")
plt.plot(time, centered(time, f), label="Centered Derivative")
plt.xlabel("Time [s]")
plt.ylabel("Angular Speed [rads/s]")
plt.legend()

plt.show()