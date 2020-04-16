####
### Title: 	Chapter 12 Question 14
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
gamma   = 1.084         # Drive strength (dimensionless)
# Additional inputs (defined in terms of the drive frequency w)
w0   = 1.5              # w0 in units of w
beta = w0/4.0           # Damping factor in units of w

# Time range parameters
tmax = 7                # Duration of simulation in units of the drive period T = 2*pi/w
dt   = 1e-2             # Time step for numerical integration in units of T
t = arange(0,tmax,dt)

# Solve DDP equation
phi0    = 0     # Initial angle (rad)
phidot0 = 0     # Initial angular velocity (rad/s)
phi, phidot, info = cm.solver_DDP(t, phi0, phidot0, gamma, w0, beta)

# Plot Stuff
fig1 = plt.figure(1)
ax1a = fig1.add_subplot(2,1,1)
ax1a.set_title("Chapter 12 Question 14")
# Plots solution of DDP
for i in range(0,info[1]):
    ax1a.plot(t,phi[:,i],'-',label="$\phi_1(0)$={:}".format(phi0))
# Other plot details (legend, etc)
ax1a.axhline(y=0, color='k')
ax1a.set_ylabel(r'$\phi_1$ (rad)')
ax1a.legend(loc='upper left')
ax1a.yaxis.set_major_formatter(FuncFormatter(lambda val,pos: '{:.0g}$\pi$'.format(val/pi) if val != 0 else '0'))
ax1a.yaxis.set_major_locator(MultipleLocator(base=pi))
ax1a.set_xlim([0, tmax])

# Solve DDP equation
phi0    = 1e-5    # Initial angle (rad)
phi2, phidot2, info2 = cm.solver_DDP(t, phi0, phidot0, gamma, w0, beta)
# Additional subplot
ax1b = fig1.add_subplot(2,1,2)
# Plots solution
for i in range(0,info2[1]):
    ax1b.plot(t,phi2[:,i],'-',label="$\phi_2(0)$={:}".format(phi0))
# Other subplot details (legend, etc)
ax1b.axhline(y=0, color='k')
ax1b.set_ylabel(r'$\phi_2$ (rad)')
ax1b.legend(loc='upper left')
ax1b.yaxis.set_major_formatter(FuncFormatter(lambda val,pos: '{:.0g}$\pi$'.format(val/pi) if val != 0 else '0'))
ax1b.yaxis.set_major_locator(MultipleLocator(base=pi))
ax1b.set_xlim([0, tmax])
ax1b.set_xlabel("Time (s)")

# Supplemental plot
fig2 = plt.figure(2)
plt.title("Chapter 12 Question 14")
ax2a = fig2.add_subplot(1,1,1)
# Plot log of absolute difference in phi
ax2a.plot(t,log(abs(phi2[:,0]-phi[:,0])),'-b')
# Other plot details (labels, etc)
ax2a.axhline(y=0,ls=':', color='k')
ax2a.set_ylabel(r'$log(|\Delta\phi|)$')
ax2a.set_xlabel('Time (s)')
ax2a.set_xlim([0, tmax])

plt.show()
