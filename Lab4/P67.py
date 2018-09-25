from __future__ import division, print_function
from visual import *

G = 6.67e-11  # N*m2/Kg2
MinS = 1. * 30. * 24. * 60. * 60.  # 1 month in seconds

AU2m = 384e6# Distance from earth to moon

# Create the objects in our program
earth           = sphere()
earth.pos       = vector(0, 0, 0)
earth.radius    = 6.4e6 * 10
earth.color     = color.white

moon        = sphere(make_trail=True)
moon.pos    = vector(AU2m, 0, 0)
moon.radius = 1.7e6 * 10
moon.color  = color.blue

# Define the masses of our objects
earth.m = 6e24  # Kg
moon.m = 7.35e22  # Kg

# We assume the earth is initially not moving
earth.v = vector(0, 0, 0)

# For the moon we know it takes one year to go around one orbit
CircOrb = 2 * pi * AU2m
moon.v = vector(0, .1 * CircOrb/MinS, 0)

# Create the momentum vectors
moon.p = earth.m * earth.v
moon.p = moon.m * moon.v

t = 0
dt = MinS/1000

while True:
    rate(1e2)

    # 1st calculate the relative position   
    r = (moon.pos - earth.pos) * AU2m
    rmag = mag(r)
    rhat = norm(r)

    # 2nd Calculate the force magnitude
    Fmag = G * (moon.m * earth.m)/ rmag**2
    Fnet = -Fmag * rhat

    moon.p = moon.p + Fnet * dt
    moon.pos = moon.pos + (moon.p/moon.m/AU2m) * dt

    # Update the time
    t = t + dt
