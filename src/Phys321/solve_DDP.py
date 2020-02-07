#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to numerically solve the driven damped oscillator (DDP) problem

For use in PHYS 321 - Intermediate Mechanics

Author: Caitano da Silva, NMT
Created: Nov/11/2019
Last modification: Nov/13/2019

Place the file chaosmod.py in the same folder that you
running this script from

"""
import numpy as np
import matplotlib.pyplot as plt
import chaosmod as cm
from scipy.interpolate import interp1d
pi = cm.pi

# Main input parameters (any of the three can be a list of inputs)
gamma   = 0.2   # Drive strength (dimensionless)
phi0    = 0     # Initial angle (rad)
phidot0 = 0     # Initial angular velocity (rad/s)


# Additional inputs (defined in terms of the drive frequency w)
w0   = 1.5            # w0 in units of w
beta = 1.5/4.0        # Damping factor in units of w
tmax = 50             # Duration of simulation in units of the drive period T = 2*pi/w
dt   = 1e-2           # Time step for numerical integration in units of T
tssrange = [40, tmax] # Range of time to determine the attractor behavior


# First plotting flag: Plot bifurcation diagram instead of time series?
iplot_bifurcation =1   # =0 : Do not plot bifurcation diagram
                        # =1 : Plot bifurcation diagram for phi
                        # =2 : Plot bifurcation diagram for phidot

# Second plotting flag: Plot state space orbits in addition to time series?
iplot_statespace =0   # =0 : Do not plot state space orbit
                       # =1 : Plot state space orbit
                       # =2 : Plot state space orbit and Poincare section
                       # =3 : Plot Poincare section (only)


# Time array
t = np.arange(0,tmax,dt)


# Solve DDP equation
phi, phidot, info = cm.solver_DDP(t, phi0, phidot0, gamma, w0, beta)


# Plot (cosmetics)
plt.ion()
LFS = 17
tlimits = [0, tmax]
#tlimits = [28, 40] # ** Change the horizontal-axis limits if needed **
#tlimits = tssrange

## Figure 1: Plot phi(t)
if iplot_bifurcation==0:

    # Plot phi(t)
    fig1 = plt.figure(1)
    plt.clf()
    ax1a = fig1.add_subplot(min(info[1],2),1,1)
    for i in range(0,info[1]):
        ax1a.plot(t,phi[:,i],'-',label=info[2][i])
#    ax1a.plot(t,-2*pi*t,':k')
    ax1a.axhline(y=0,ls=':', color='k')
    ax1a.set_ylabel(r'$\phi$ (rad)', fontsize=LFS)
    ax1a.legend(loc='best')
    ax1a.set_xlim(tlimits)

    # Plot Delta phi versus t
    if info[1]>1:
        ax1b = fig1.add_subplot(2,1,2)
        ax1b.plot(t,phi[:,1]-phi[:,0],'-b')
#        ax1b.semilogy(t,np.abs(phi[:,1]-phi[:,0]),'-b') # ** Use log scale if needed **
        ax1b.axhline(y=0,ls=':', color='k')
        ax1b.set_ylabel(r'$\Delta\phi$ (rad)', fontsize=LFS)
        ax1b.set_xlabel('Time (T)', fontsize=LFS)
        ax1b.set_xlim(tlimits)
    else:
        ax1a.set_xlabel('Time (T)', fontsize=LFS)


## Lookup phi values at selected times of interest
#finterp = interp1d(t, phi[:,0])
#phi_interest = finterp(np.arange(30,39,1))


## Figure 2: Plot bifurcation diagram (np.size(gamma) must be greater than one)
if iplot_bifurcation>0:
    if 'fig1' in locals():
        plt.close(fig1)

    # Select time range of interest for plotting
    irange = cm.get_indexes_in_array(t,np.arange(tssrange[0],tssrange[1],1))

    # Plot phi or phidot?
    if iplot_bifurcation==1:
        yplot = phi
        ylabelplot = r'$\phi$ (rad)'
    elif iplot_bifurcation==2:
        yplot = phidot
        ylabelplot = r'$\dot{\phi}$ (rad/s)'

    # Plot bifurcation diagram
    fig2 = plt.figure(2)
    plt.clf()
    ax2 = fig2.add_subplot(1,1,1)
    for i in range(0,np.size(gamma)):
        ax2.plot(gamma[i]*np.ones((np.size(irange),)),yplot[irange,i],'.',markersize=2)
    ax2.set_ylabel(ylabelplot, fontsize=LFS)
    ax2.set_xlabel(r'$\gamma$', fontsize=LFS)
    ax2.set_xlim((np.min(gamma),np.max(gamma)))
    ax2.set_title('Bifurcation diagram')

else:
    if 'fig2' in locals():
            # plt.close(fig2)
            print("Fuck")

## Figure 3: Plot state-space orbit and/or Poincare section
if iplot_statespace>0:

    # Select time range of interest for plotting
    irange = cm.get_indexes_in_array(t,tssrange)
    ivec = cm.get_indexes_in_array(t,np.arange(tssrange[0],tssrange[1],1))
    tlabel = "{:.0f}".format(t[irange[0]]) + r' $\leq t \leq$ ' + "{:.0f}".format(t[irange[1]])

    # Unroll angle ** Edit this one if needed **
    xplot = phi
#    xplot = cm.unroll_angle(phi)

    # Determine plot axis limits
    philims = np.max(np.abs(xplot[irange[0]:irange[1],:]))*1.2*np.array([-1,1])
    phidotlims = np.max(np.abs(phidot[irange[0]:irange[1],:]))*1.2*np.array([-1,1])

    # Plot state-space orbit and/or Poincare section
    fig3 = plt.figure(3)
    plt.clf()
    ax3 = fig3.add_subplot(1,1,1)

    if iplot_statespace==1 or iplot_statespace==2:
        MS = 8
        for i in range(0,info[1]): # State-space orbit
            ax3.plot(xplot[irange[0]:irange[1],i],phidot[irange[0]:irange[1],i],'.',markersize=1,label='State-space orbit')
    else:
        MS = 2
    if iplot_statespace>1:
        for i in range(0,info[1]): # Poincare section
            ax3.plot(xplot[ivec,i],phidot[ivec,i],'.',markersize=MS,label='Poincare section')
    ax3.axhline(y=0,ls=':', color='k')
    ax3.axvline(x=0,ls=':', color='k')
    ax3.set_xlim( philims )
    ax3.set_ylim( phidotlims )
    ax3.set_xlabel(r'$\phi$ (rad)', fontsize=LFS)
    ax3.set_ylabel(r'$\dot{\phi}$ (rad/s)', fontsize=LFS)
    ax3.set_title(tlabel)
    ax3.legend(loc='best')

else:
    if 'fig3' in locals():
        plt.close(fig3)
