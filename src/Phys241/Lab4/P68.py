# Spencer Riley
from __future__ import print_function, division
from visual import *

G = 6.7e-11  # Gravitational constant in Nm2/kg2
YinS = 687 * 24. * 60. * 60  # seconds in a Martian Year
Martian = 2.28e11  # Distance from sun and mars in meters
ScaleF = 1e-22 # Scale factor for force arrow
ScaleP = 1e-29 # Sale factor for momentum

# Create objects
sun = sphere(make_trail=True)
sun.pos = vector(0, 0, 0)
sun.radius = 0.1
sun.color = color.yellow
sun.material = materials.emissive

sun.v = vector(0, 0, 0)
sun.m = 2e30  # in kg
sun.p = sun.m * sun.v

mars = sphere(make_trail=True)
mars.pos = vector(1, 0, 0)
mars.radius = 0.05
mars.color = color.red

mars.v = vector(0, sqrt(G * sun.m / (mag(mars.pos) * Martian)), 0)  # in m/s
mars.m = 6.4e23  # in kg
mars.p = mars.m * mars.v

# Creates arrow to track momentum
momentum = arrow()
momentum.color = color.green

# Creates arrow to track net force
force = arrow()
force.color = color.magenta

t = 0 # Initial Time
dt = YinS / 1000 # Time Step

# Add timestamp label
timestamp = label(pos=vector(0, 0.5, 0), color=color.red, text='Time in Martian Years: ')

while t < 1000 * dt:
    rate(1e2)

    timestamp.text = 'Time in Martian Years: {:6.2f}'.format(t / (YinS))

    # Distance from sun to mars
    r = (mars.pos - sun.pos) * Martian
    rmag = mag(r)
    rhat = norm(r)

    # Gravitational force
    Fmag = G * (sun.m * mars.m)/rmag**2
    Fnet = -Fmag * rhat

    # Update momentum and position of mars
    mars.p = mars.p + Fnet * dt
    mars.pos = mars.pos + (mars.p / mars.m / Martian) * dt

    # Update momentum and position of sun
    sun.pos = sun.pos + (sun.p / sun.m / Martian) * dt
    sun.p = sun.p + (-Fnet) * dt

    # Updates arrow's position
    momentum.pos = mars.pos
    momentum.axis = ScaleP *  mars.p

    # Updates arrow's position
    force.pos =  mars.pos
    force.axis = ScaleF * Fnet

    # Update time
    t = t + dt
