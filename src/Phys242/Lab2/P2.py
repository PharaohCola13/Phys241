# Spencer Riley
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

fname = "./trig.spaghetti"
file = open(fname, "r")

angle   = np.loadtxt(fname, skiprows=2, unpack=True)[0]
sint    = np.loadtxt(fname, skiprows=2, unpack=True)[1]
cost    = np.loadtxt(fname, skiprows=2, unpack=True)[2]

dtheta = angle[1] - angle[0]
theta  = np.arange(np.deg2rad(angle[0]), np.deg2rad(angle[-1]+dtheta), np.deg2rad(dtheta))

f   = np.sin(theta)
Nd  = np.zeros(len(theta))

def forwards(a, f):
    print("Starting Forward Derivative Calculations")
    i = 0
    y = []
    while i <= len(a)-1:
        if i == len(a) - 1:
            Nd[i] = (f[i] - f[i-1])/(a[i] - a[i-1])
        else:
            Nd[i] = (f[i+1] - f[i])/(a[i+1] - a[i])
        y.append(Nd[i])
        i = i + 1
    print("Completed")
    return y

def backwards(a, f):
    print("Starting Backward Derivative Calculations")
    i = 0
    y = []
    while i <= len(a)-1:
        if i == 0:
            Nd[i] = (f[i + 1] - f[i]) / (a[i + 1] - a[i])
        else:
            Nd[i] = (f[i] - f[i - 1]) / (a[i] - a[i - 1])
        y.append(Nd[i])
        i = i + 1
    print("Completed")
    return y

def centered(a,f):
    print("Starting Centered Derivative Calculations")
    i = 0
    y = []
    while i <= len(a) -1:
        if i == 0:
            Nd[i] = (f[i+1] - f[i])/(a[i+1]-a[i])
        elif i == len(a) -1:
            Nd[i] = (f[i]-f[i-1])/(a[i]-a[i-1])
        else:
            Nd[i] = (f[i+1]-f[i-1])/(a[i+1]-a[i-1])
        y.append(Nd[i])
        i = i + 1
    print("Completed")
    return y

plt.figure(1)
plt.title("Comparison of Forward Derivative Scheme")
plt.plot(theta, forwards(theta,f), color='blue', label='Forward Derivative')
plt.plot(theta, cost, color='red', label=r'$\cos(\theta)$')
plt.plot(theta, sint, color='black', label=r'$\sin(\theta)$')

plt.xlabel(r"Angle ($^o$)")
plt.legend()

plt.figure(2)
plt.title("Comparison of Backward Derivative Scheme")
plt.plot(theta, backwards(theta, f), color='blue', label="Backward Derivative")
plt.plot(theta, cost, color='red', label=r'$\cos(\theta)$')
plt.plot(theta, sint, color='black', label=r'$\sin(\theta)$')

plt.xlabel(r"Angle ($^o$)")
plt.legend()
#
plt.figure(3)
plt.title("Comparison of Centered Derivative Scheme")
plt.plot(theta, centered(theta, f), color='blue', label="Centered Derivative")
plt.plot(theta, cost, color='red', label=r'$\cos(\theta)$')
plt.plot(theta, sint, color='black', label=r'$\sin(\theta)$')

plt.xlabel(r"Angle ($^o$)")
plt.legend()

plt.ylim(-1, 1)
plt.show()