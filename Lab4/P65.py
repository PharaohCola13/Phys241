from __future__ import division, print_function
from visual import *

mcraft = 1.5e4 # mass of craft in kg
dt = 60 # in s
t = 0
G = 6.7e-11 # Gravitational Constant

# Creates a sphere representing Earth
Earth = sphere()
Earth.pos = vector(0,0,0)
Earth.radius = 1
Earth.m = 1

# Creates a craft
craft = sphere(make_trail=True)
craft.v = vector(0,2e3,0) # m/s
craft.m = mcraft
craft.pos = vector(0, 10 * Earth.radius, 0)

craft.p = craft.m * craft.v

while True:
    rate(1)
    # Distance
    r = craft.pos - Earth.pos
    rmag = mag(r)
    rhat = norm(r)
    
    # Force of gravity
    fgrav = G * (craft.m * Earth.m)/(rmag**2)
    fnet  = -fgrav * rhat
    
    # Updates craft's momentum
    craft.p = craft.p + fnet * dt
    # Updates craft's position
    craft.pos = craft.pos + (craft.p/craft.m) * dt

    t = t + dt
