from __future__ import division, print_function
from visual import *

star        = sphere()
star.pos    = vector(0,0,0)
star.radius = 100
star.color  = color.orange

planet_one          = sphere(make_trail=True)
planet_one.pos      = vector(15, 15, 0)
planet_one.radius   = 1
planet_one.color    = color.cyan

theta = 0

ij_hat  = vector(15 * cos(theta), 15 * sin(theta), 0) # Defines a unit circle on the xy-plane


while True:
    rate(100)
    # Local Definitions of the components from ij_hat
    ij_hat.x = cos(theta)
    ij_hat.y = sin(theta)
    ij_hat.z = 0

    planet_one.pos = 3 * star.radius * ij_hat

    theta = theta + pi/1000