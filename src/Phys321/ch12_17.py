####
### Title: 	Chapter 12 Question 17
### Author: Spencer Riley
### Python Version: 3.5.3
####
# Import Stuff
from numpy import *
import matplotlib.pyplot as plt
import chaosmod as cm
from scipy.interpolate import interp1d
from matplotlib.ticker import MultipleLocator, FuncFormatter

# Main input parameters (any of the three can be a list of inputs)
gamma   = 1.503         # Drive strength (dimensionless)
# Additional inputs (defined in terms of the drive frequency w)
w0   = 1.5              # w0 in units of w
beta = w0/4.0           # Damping factor in units of w

# Time range in units of seconds
tmax = 8                # Duration of simulation in units of the drive period T = 2*pi/w
dt   = 1e-2             # Time step for numerical integration in units of T
t = arange(0,tmax,dt)

# Solve DDP equation
phi0    = 0     # Initial angle (rad)
phidot0 = 0     # Initial angular velocity (rad/s)
phi, phidot, info = cm.solver_DDP(t, phi0, phidot0, gamma, w0, beta)

# Plot Stuff
fig1 = plt.figure(1)
plt.title("Chapter 12 Question 17 Part A")
ax1a = fig1.add_subplot(min(info[1],2),1,1)
# Plots both curves
for i in range(0,info[1]):
    ax1a.plot(t,phi[:,i],'-',label="$\gamma$ = {:}".format(gamma))
    ax1a.plot(t,phi[:,i]+(2*pi*t))
# Other plot details (legend, etc)
ax1a.axhline(y=0, color='k')
ax1a.set_ylabel(r'$\phi_1(t)$ (rad)')
ax1a.legend(loc='upper right')
ax1a.set_xlim([0, tmax])

plt.show()
