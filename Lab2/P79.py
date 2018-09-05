from __future__ import division, print_function
from visual import *

circle = box()
circle.pos = vector(0,0,-1)
circle.size = (5,5,0.5)
circle.color = color.red
circle.opacity = 0.4

particle = sphere(make_trail = True)
particle.pos = vector(-5,0, -5)
particle.radius = 0.3
particle.color = color.cyan

v = vector(0.5, 0, 0.5)
delta_t = 0.05
t = 0

while t < 20:
    rate(100)
    particle.pos = particle.pos + v * delta_t

    if particle.pos.z == circle.pos.z:
        v.z = v.z - 2
    
    t = t + delta_t
    
