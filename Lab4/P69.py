from __future__ import division, print_function
from visual import *

dt = 10 # in s
t = 0
G = 6.7e-11 # Gravitational Constant

Sun             = sphere()
Sun.pos         = vector(0,0,0)
Sun.m           = 2e30
Sun.radius      = 6.9e10
Sun.color       = color.yellow
Sun.material    = materials.emissive

Mars            = sphere(make_trail=True)
Mars.pos        = vector(20.3e10,0,0)
Mars.m          = 6.4e23 # in kg
Mars.radius     = 3.39e10 # in m
Mars.color      = color.red

Mars.v          = vector(50e3*cos(pi),50e3*cos(pi),0)
Mars.p          = Mars.m * Mars.v
while True:
    rate(1000000)

    r       = Mars.pos - Sun.pos
    rmag    = mag(r)
    rhat    = norm(r)

    fgrav   = G * (Sun.m * Mars.m)/rmag**2

    fnet    = -fgrav * rhat

    Mars.p  = Mars.p + fnet * dt
    Mars.pos = Mars.pos + (Mars.p/Mars.m)*dt

    t = t + dt
