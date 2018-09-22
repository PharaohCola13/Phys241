from __future__ import division, print_function
from visual import *

mcraft = 1.5e4 # mass of craft in kg
dt = 10 # in s
t = 0
G = 6.7e-11 # Gravitational Constant

# Creates a sphere representing Earth
Earth = sphere()
Earth.pos = vector(0,0,0)
Earth.radius = 6.4e6 # in m
Earth.m = 6e24 # in kg
Earth.material = materials.BlueMarble

moon = sphere()
moon.pos = vector(-10 * Earth.radius,0, 0)
moon.radius = 1.75e6 # in m
moon.m = 7e22 # in kg

# Creates a craft
craft = sphere(make_trail=True)
craft.v = vector(1.5e3 * cos(pi), 2e3 * cos(pi), 0) # m/s

# vector(1e3*cos(pi), 2e3*sin(pi), 0) --> Elipitical Orbit

craft.m = mcraft
craft.radius = 2e6 # in m
craft.pos = vector(10 * Earth.radius,0,0)
craft.p = craft.m * craft.v # Momentum

while True:
    rate(10000)

    # Distance
    r =  craft.pos - Earth.pos
    rmag = mag(r)
    rhat = norm(r)

    r1 = craft.pos - moon.pos
    r1mag = mag(r1)
    r1hat = norm(r1)
    #print("Rmag = {}".format(rmag))
    
    # Force of gravity
    # Part A
    # fgrav = G * (craft.m * Earth.m)/(rmag**2)
    # fgrav1 = G * (craft.m * moon.m)/(r1mag**2)
##
    # fnet  = - (fgrav1 * r1hat)
##
    
    fgrav  = G * (craft.m * Earth.m)/(rmag**2)
    fgrav1 = G * (craft.m * moon.m)/(r1mag**2)

    fnet  = -(fgrav * rhat) - (fgrav1 * r1hat)
    #print("fnet = {}".format(fnet))
  
    # Updates craft's momentum
    craft.p = craft.p + fnet * dt
    # Updates craft's position
    craft.pos = craft.pos + (craft.p/craft.m) * dt

    t = t + dt
