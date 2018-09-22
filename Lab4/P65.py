from __future__ import division, print_function
from visual import *

mcraft = 1.5e4 # mass of craft in kg
dt = 60 # in s
t = 0
G = 6.7e-11 # Gravitational Constant
Fscale = 1e-1 # Scaling Factor for momentum
Fscale2 = 3e2 # Scaling Factor for force


# Creates a sphere representing Earth
Earth = sphere()
Earth.pos = vector(0,0,0)
Earth.radius = 6.4e6 # in m
Earth.m = 6e24 # in kg
Earth.material = materials.BlueMarble

# Creates a craft
craft = sphere(make_trail=True)
craft.v = vector(-2e3,0,0) # m/s

# part c
# vector(1e3*cos(pi), 2e3*sin(pi), 0) --> Elipitical Orbit

craft.m = mcraft
craft.radius = 1e6 # in m
craft.pos = vector(0,10 * Earth.radius,0)
craft.p = craft.m * craft.v # Momentum

# Creates an arrow to track momentum
momentum = arrow()
momentum.color = color.green

# Creates an arrow to track the Net Force
force = arrow()
force.color = color.orange

while True:
    rate(100)

    # Updates arrow's position
    momentum.pos = craft.pos
    momentum.axis = Fscale * craft.p

    # Distance
    r =  craft.pos - Earth.pos
    rmag = mag(r)
    rhat = norm(r)
    
    # Force of gravity
    fgrav = G * (craft.m * Earth.m)/(rmag**2) 
    fnet  = -fgrav * rhat

    # Updates arrow's position
    force.pos = craft.pos
    force.axis = Fscale2 * fnet
    
    # Updates craft's momentum
    craft.p = craft.p + fnet * dt
    # Updates craft's position
    craft.pos = craft.pos + (craft.p/craft.m) * dt

    t = t + dt
