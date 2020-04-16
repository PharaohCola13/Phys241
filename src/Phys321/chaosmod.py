#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chaos Module:
Auxiliary functions to solve the driven damped oscillator (DDP) equation

This set of scripts have been developed to assist with the understanding of
Chapter 12 of Classical Mechanics by J.R. Taylor; see equation (12.11) in page 463

The input variables in the main file 'solve_DDP.py' are:

gamma    = Drive strength (dimensionless)
phi0     = Initial angle (rad)
phidot0  = Initial angular velocity (rad/s)
w0       = Fundamental frequency of small oscillations of a pendulum around the
           equlibrium position; w0 = sqrt(gravity/length); w0 is given in units
           of the drive frequency w
beta     = Damping factor in units of w
tmax     = Duration of simulation in units of the drive period T = 2*pi/w
dt       = Time step for numerical integration in units of T
tssrange = Time range used to determine the attractor behavior and to plot the
           bifurcation diagram, state-space orbit, and Poincare section

Author: Caitano da Silva, NMT
Created: Nov/11/2019
Last modification: Nov/13/2019

If you find any errors in these python scripts please
report them to caitano.dasilva@nmt.edu

"""
import numpy as np
from scipy.integrate import odeint


# Define constants
pi     = np.pi
twopi  = 2.*pi
twopi2 = twopi**2


# Define the RHS of the DDP equation
def rhs_DDP(phivec, t0, gamma, w0, beta):

    # Allocate vars
    # t0 is the time of interest in unit of T
    phi1    = phivec[0] # phi (rad)
    phidot1 = phivec[1] # d(phi)/dt (rad/s)

    # Define the force terms
    w02 = w0**2
    friction_f      = -2.*twopi*beta*phidot1
    gravitational_f = - twopi2*w02*np.sin(phi1)
    driving_f       = twopi2*gamma*w02*np.cos(twopi*t0)

    # Allocate the rhs
    rhs_DDP0 = phidot1
    rhs_DDP1 = friction_f + gravitational_f + driving_f

    return np.array([rhs_DDP0, rhs_DDP1])


# Solve DDP problem for multiple initial conditions
# phi_initial, phidot initial, or gamma can be a list of values
def solver_DDP(t, phi_initial, phidot_initial, gamma, w0, beta):

    # Decide which var to loop through
    if np.size(phi_initial)>1:
        Ncases = np.size(phi_initial)
        loopvar = 2
        dispvars = phi_initial
    elif np.size(phidot_initial)>1:
        Ncases = np.size(phidot_initial)
        loopvar = 3
        dispvars = phidot_initial
    else:
        Ncases = np.size(gamma)
        loopvar = 1
        if Ncases==1:
            dispvars = [gamma]
        else:
            dispvars = gamma

    gamma_in        = np.zeros((1,Ncases))
    gamma_in[0,:]   = gamma
    phivec0_in      = np.zeros((Ncases,2))
    phivec0_in[:,0] = phi_initial
    phivec0_in[:,1] = phidot_initial


    # Allocate auxiliary arrays
    phi = np.zeros( (np.size(t), Ncases) )
    phidot = np.zeros( (np.size(t), Ncases) )


    # Solve DDP equation
    for i in range(0,Ncases):
        sol = odeint(rhs_DDP, phivec0_in[i,:], t, args=(gamma_in[0,i], w0, beta), rtol=1e-6)
        phi[:,i]    = sol[:,0]
        phidot[:,i] = sol[:,1]


    # Output basic info about solution
    labels = []
    varname = ['gamma', 'phi(0)', 'phidot(0)']
    for i in range(0,Ncases):
        labels.append("{:.3f}".format(dispvars[i]))
    info = [loopvar, Ncases, labels]
    return phi, phidot, info


# Constrain angle between -pi and +pi by removing the rolling effect
def unroll_angle(angle):

    # Get info about input vector
    unrolled = angle.copy()
    angle_shape = np.shape(angle)
    Nangle = angle_shape[0]

    # Unroll algorithm
    if np.size(angle_shape)==1:
        for i in range(0,Nangle):
            if unrolled[i]<-pi:
                unrolled[i:] = unrolled[i:] + twopi
            elif unrolled[i]>pi:
                unrolled[i:] = unrolled[i:] - twopi
    else:
        Ncases = angle_shape[1]
        for j in range(0,Ncases):
            for i in range(0,Nangle):
                if unrolled[i,j]<-pi:
                    unrolled[i:,j] = unrolled[i:,j] + twopi
                elif unrolled[i,j]>pi:
                    unrolled[i:,j] = unrolled[i:,j] - twopi

    return unrolled


# Get indexes of a vector x that contain the values closest to x0
def get_indexes_in_array(x,x0):

    # Find pertinent indexes
    N = np.size(x0)
    indexes = np.empty((N,), dtype=int)
    for i in range(0,N):
        if x0[i]<np.min(x):
            indexes[i] = 1
        elif x0[i]>np.max(x):
            indexes[i] = np.size(x)-1
        else:
            indexes[i] = np.argmin(np.abs((x - x0[i])))

    # Correction if x0 is outside of the ranges of x
    if N==2 and np.min(indexes)==np.max(indexes):
        indexes = np.array( (1, np.size(x)-1) )


    return indexes
