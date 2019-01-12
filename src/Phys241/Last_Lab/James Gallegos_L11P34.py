from __future__ import division, print_function
from visual import *
from visual.graph import *
##################################
#
# Physics 241
# Lab 11
# Chapter 10, P34
# Driver: James Gallegos
# Navigator: James Gallegos
# 28 November 2018
#
##################################

# Program was written using Glowscript

# This program will determine the scattering angle for an alpha particle

# Define constants and parameters for this problem
q_e     = 1.6e-19           # charge of an electron
m_p     = 1.7e-27           # mass of a proton
oofpez  = 9e9               # k
m_Au    = (79 + 118) * m_p  # mass of a gold atom
m_Alpha = (2 + 2) * m_p     # mass of an alpha particle
qAu     = 79 * q_e          # charge of the gold atom
qAlpha  = 2 * q_e           # charge of the alpha particle
k       = 9e9               # in units of Nm^2 / C^2

# Define the objects
Au    = sphere(pos = vector(0, 0, 0),          radius = 4e-15, color = color.yellow,  make_trail = True)
#Alpha = sphere(pos = vec(-1e-13, 5e-15, 0), radius = 1e-15, color = color.magenta, make_trail = True) # original defined by problem

# Use this for experimenting different values for part (d):
#Alpha = sphere(pos = vec(-1e-13, 3e-14, 0), radius = 1e-15, color = color.magenta, make_trail = True) # experimenting

# Use these for part (f):
Alpha = sphere(pos = vector(-1e-13, 5e-15, 0), radius = 1e-15, color = color.magenta, make_trail = True) # 90 degree
#Alpha = sphere(pos = vec(-1e-13, 2e-15, 0), radius = 1e-15, color = color.magenta, make_trail = True) # 168 degrees
#Alpha = sphere(pos = vec(-1e-13, 5e-14, 0), radius = 1e-15, color = color.magenta, make_trail = True) # 38 degrees
#Alpha = sphere(pos = vec(-1e-13, 1.185e-13, 0), radius = 1e-15, color = color.magenta, make_trail = True) # 13 degrees


Au.opacity = 0.5

# Define initial momentum, velocity
p_Au    = m_Au * vector(0, 0, 0)
p_Alpha = vector(1.043e-19, 0, 0)
p_i     = vector(1.043e-19, 0 ,0)

# Define the time
t = 0
deltat  = 1e-23

print ('The impact parameter b is =', Alpha.pos.y - Au.pos.y)

# Calculation Loop
while t < 1.3e-20:
    rate(500)                       # controls the speed at which the program runs such that we can visually see the program execute

    r_a_au = Alpha.pos - Au.pos     # update the position of the gold particle

    F_a_au = norm(r_a_au) * (k * qAu * qAlpha) / mag(r_a_au) ** 2   # update the force vector equation for the gold atom
    Fnet = F_a_au                                                   # update the net force equation

    p_Alpha = p_Alpha + Fnet * deltat   # update the momentum equation for the alpha particle
    p_Au    = p_Au    - Fnet * deltat   # update the momentum equation for the gold atom


    Alpha.pos = Alpha.pos + (p_Alpha / m_Alpha) * deltat    # update the position equation for the alpha particle
    Au.pos    = Au.pos    + (p_Au    / m_Au)    * deltat    # update the position equation for the gold atom

    
    t = t + deltat  # update the time

    # The next 2 lines, it does not matter if they are inside the loop or not, the scattering angle comes out to be the same value.
scatter = dot(norm(p_i), norm(p_Alpha))
s_angle = acos(scatter)

#print("For part e, the calculation that shows the calculation of the scattering angle: ", degrees(acos(scatter)))
print("The scattering angle in degrees is: ", degrees(s_angle))

#print("For part f, the value of impact parameter that leads to the scattering angle of approx. 90 degrees is 1.825e-14 meters.") # print statement for impact parameter for 90 degrees
#print("For part f, the value of impact parameter that leads to the scattering angle of approx. 168 degrees is 2e-15 meters.")    # print statement for impact parameter for 168 degrees
#print("For part f, the value of impact parameter that leads to the scattering angle of approx. 38 degrees is 5e-14 meters.")     # print statement for impact parameter for 38 degrees
#print("For part f, the value of impact parameter that leads to the scattering angle of approx. 13 degrees is 1.185e-13 meters.") # print statement for impact parameter for 13 degrees
