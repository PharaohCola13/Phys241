from __future__ import division, print_function
from visual import *

star_out            = sphere()
star_out.pos        = vector(0,0,0)
star_out.radius     = 56378.15
star_out.m          = 1.989E30
star_out.color      = color.orange
star_out.opacity    = 0.8

star_in             = sphere()
star_in.pos         = vector(0,0,0)
star_in.radius      = 0.75 * 56378.15
star_in.m           = 0
star_in.color       = color.yellow
star_in.opacity     = 1

planet_one          = sphere(make_trail=True)
planet_one.pos      = vector(15, 15, 0)
planet_one.radius   = 200 * 6.378
planet_one.color    = color.cyan
planet_one.m        = 5.972E24

theta = 0

ij_hat  = vector(15 * cos(theta), 15 * sin(theta), 0) # Defines a unit circle on the xy-plane


while True:
    rate(100)
    # Local Definitions of the components from ij_hat
    ij_hat.x = cos(theta)
    ij_hat.y = sin(theta)
    ij_hat.z = 0

    planet_one.pos = 3 * star_out.radius * ij_hat

    theta = theta + pi/1000