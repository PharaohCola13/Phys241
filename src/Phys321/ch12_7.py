####
### Title: 	Chapter 12 Question 7
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
gamma   = 1.06   # Drive strength (dimensionless)
# Additional inputs (defined in terms of the drive frequency w)
w0   = 1.5            # w0 in units of w
beta = w0/4.0        # Damping factor in units of w

# Time range parameters
tmax = 10            # Duration of simulation in units of the drive period T = 2*pi/w
dt   = 1e-2           # Time step for numerical integration in units of T
t = arange(0,tmax,dt)

## Part A
def parta():
# Solve DDP equation
    phi0    = 0     # Initial angle (rad)
    phidot0 = 0     # Initial angular velocity (rad/s)
    phi, phidot, info = cm.solver_DDP(t, phi0, phidot0, gamma, w0, beta)
# Plot Stuff
    fig1 = plt.figure(1)
    plt.title("Chapter 12 Question 7 Part A")
    ax1a = fig1.add_subplot(min(info[1],2),1,1)
# Plots solution
    for i in range(0,info[1]):
        ax1a.plot(t,phi[:,i],'-',label="$\gamma$ = {:}".format(gamma))
# Other Plot details (legend ,etc)
    ax1a.axhline(y=0, color='k')
    ax1a.set_ylabel(r'$\phi$ (rad)')
    ax1a.legend(loc='upper right')
    ax1a.yaxis.set_major_formatter(FuncFormatter(lambda val,pos: '{:.0g}$\pi$'.format(val/pi) if val != 0 else '0'))
    ax1a.yaxis.set_major_locator(MultipleLocator(base=pi))
    ax1a.set_xlim([0, tmax])

## Part B
def partbc():
    # Solve DDP equation
    phidot0 = 0     # Initial angular velocity (rad/s)
    phi0    = [-pi/2, 0, pi/2]     # Initial angle (rad)
    phi, phidot, info = cm.solver_DDP(t, phi0, phidot0, gamma, w0, beta)
# Plot stuff
    fig2 = plt.figure(2)
    ax2a = fig2.add_subplot(min(info[1],2),1,1)
    ax2a.set_title("Chapter 12 Question 7 Part BC")
# Plots solution
    for i in range(0,info[1]):
        ax2a.plot(t,phi[:,i],'-',label="$\phi(0)$={:.0g}$\pi$".format(float(info[2][i])/pi))
# Other plot details (legend, etc)
    ax2a.axhline(y=0, color='k')
    ax2a.set_ylabel(r'$\phi$ (rad)')
    ax2a.legend(loc='upper right')
    ax2a.yaxis.set_major_formatter(FuncFormatter(lambda val,pos: '{:.0g}$\pi$'.format(float(val)/pi) if val != 0 else '0'))
    ax2a.yaxis.set_major_locator(MultipleLocator(base=pi))
    ax2a.set_xlim([0, tmax])

    # Plot Delta phi versus t
    if info[1]>1:
        ax2b = fig2.add_subplot(2,1,2)
        ax2b.plot(t,phi[:,1]-phi[:,0],'-b')
        ax2b.axhline(y=0,ls=':', color='k')
        ax2b.set_ylabel(r'$\Delta\phi$ (rad)')
        ax2b.set_xlabel('Time (s)')
        ax2b.set_xlim([0, tmax])
    else:
        ax2a.set_xlabel('Time (s)')

# Runs the functions for each part
parta()
partbc()

plt.show()
