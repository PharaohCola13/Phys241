from __future__ import division, print_function
from visual import *

# 1) initial velocity is equal to (0.5, 0, 0.5)
# 2) the particle is initially located behind the the box
# 3) Line 15
# 4) the value is 0.05
# 5) The particle will travel through the box,

purple = vector(0.4, 0.2, 0.6) # Defines the color purple

solid_box           = box()
solid_box.pos       = vector(0, 0, -1) # Position of box
solid_box.size      = (5, 5, 0.5) # Dimensions of box
solid_box.color     = red # color of box
solid_box.opacity   = 0.4 # transparency of box

particle            = sphere(make_trail = True)
particle.pos        = vector(6,0,0) # Initial position of particle
particle.radius     = 0.3 # radius of the particle
particle.color      = purple

v       = vector(-1,0,0) # velocity of particle

delta_t = 0.05 # Time step

t       = 0 # Initial value of time

while t < 20:
    rate(100)

    particle.pos = particle.pos + v * delta_t # Position prognostic equation

    t = t + delta_t

