####################################################
# Physics 241 - Dr. Morales-Juberias               #
# Example of particle moving at constant velocity  #
# August 29, 2018                                  #
####################################################

from __future__ import print_function,division
from visual import *
import numpy as np


#Create cartesian axes

x_axis = arrow(pos=vector(0,0,0),axis=10*vector(1,0,0),color=color.red,shaftwidth=0.2)
y_axis = arrow(pos=vector(0,0,0),axis=10*vector(0,1,0),color=color.green,shaftwidth=0.2)
z_axis = arrow(pos=vector(0,0,0),axis=10*vector(0,0,1),color=color.yellow,shaftwidth=0.2)

#Create and object at a given initial position
ball = sphere(pos=vector(0,0,0),radius=0.5,color=color.white,make_trail=True)

#velocity of the object - Constant for this example, but sill 3D
v = vector(x,y,z)

t  = 0   #define my time
dt = 0.1 #define the timestep 

scene.mouse.getclick() #Stop the program till receiving a mouse click. Useful for deubugging initial conditions

while t <= 20*dt:
    rate(10)                      #Controls the rate of the animation. Refer to the Vpython Help for more details
    ball.pos = ball.pos + v * dt     #prognostic equation for the position of the particle
    t = t + dt                      #Update the time to control the duration of the while loop

