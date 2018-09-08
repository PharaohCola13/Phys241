from __future__ import division, print_function
from visual import *
# from screenshot import GetScreenShot # Required to have screenshot.py

# 1) initial velocity is equal to (0.5, 0, 0.5)
# 2) the particle is initially located behind the the box
# 3) Line 15
# 4) the value is 0.05
# 5) The particle will travel through the box,

purple = vector(0.4, 0.2, 0.6)

box(pos=vector(0,0,-1),
    size=(5,5,0.5),
    color=color.red,
    opacity = 0.4)

particle = sphere(pos=vector(6,0,0),
                  radius=0.3,
                  color= purple,
                  make_trail = True)

v = vector(-1,0,0)

delta_t = 0.05
t = 0

while t < 20:
    rate(100)
    particle.pos = particle.pos + v * delta_t
    t = t + delta_t