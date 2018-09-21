from __future__ import division, print_function
from visual import *

mcraft = 1.5e4 #kg
dt = 60 # s
t = 0
G = 6.7e-11

Earth = sphere()
Earth.pos = vector(0,0,0)
Earth.radius = 1
Earth.m = 1


craft = sphere(make_trail=True)
craft.v = vector(0,2e3,0) # m/s
craft.m = mcraft
craft.pos = vector(0, 10 * Earth.radius, 0)

craft.p = craft.m * craft.v

while True:
    rate(1)
    r = craft.pos - Earth.pos
    rmag = mag(r)
    rhat = norm(r)

    fgrav = G * (craft.m * Earth.m)/(rmag**2)
    fnet  = -fgrav * rhat

    craft.p = craft.p + fnet * dt
    craft.pos = craft.pos + (craft.p/craft.m) * dt

    t = t + dt