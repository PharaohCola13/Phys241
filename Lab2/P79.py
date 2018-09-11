from __future__ import division, print_function
from visual import *

circle          = box()
circle.pos      = vector(0, 0, -1) # Position of box
circle.size     = (5, 5, 0.5)
circle.color    = color.red
circle.opacity  = 0.4 # Transparency of box

particle        = sphere(make_trail=True)
particle.pos    = vector(-5, 0, -5) # Initial position of particle
particle.radius = 0.3 # Radius of particle
particle.color  = color.cyan

v       = vector(0.5, 0, 0.5) # Initial velocity vector
delta_t = 0.05 # The time step
t       = 0 # Initial time

while t < 20:
    rate(100)
    particle.pos = particle.pos + v * delta_t # Changing the position of the particle

    if particle.pos.x >= (circle.pos.x - 1.25):
        v = vector(0.75, 0, -0.75) # The change in the velocity vector (bouncing off of the box)

    t = t + delta_t
