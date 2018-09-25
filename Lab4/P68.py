# Spencer Riley
from __future__ import print_function, division
from visual import *

G = 6.7e-11  # Nm2/kg2
YinS = 687 * 24. * 60. * 60  # seconds in a Martian Year
Lunar = 2.28e11  # Distance from sun and mars in meters
ScaleF = 1e-21
ScaleP = 1e-28

# Create objects
sun = sphere(make_trail=True)
sun.pos = vector(0, 0, 0)
sun.radius = 0.1
sun.color = color.yellow
sun.material = materials.emissive

sun.v0 = vector(0, 0, 0)
sun.m = 2e30  # kg
sun.p = sun.m * sun.v0

mars = sphere(make_trail=True)
mars.pos = vector(1, 0, 0)
mars.radius = 0.05
mars.color = color.red

mars.v0 = vector(0, sqrt(G * sun.m / (mag(mars.pos) * Lunar)), 0)  # m/s
mars.m = 6.4e23  # kg
mars.p = mars.m * mars.v0
print(mars.p)

momentum = arrow()
momentum.color = color.green

force = arrow()
force.color = color.magenta

# While loop somewhere in here
t = 0
dt = YinS / 1000

# Add timestamp label
timestamp = label(pos=vector(0, 0.5, 0), color=color.red, text='Time in Martian Years: ')

while t < 1000 * dt:
    rate(1e2)

    timestamp.text = 'Time in Martian Years: {:6.2f}'.format(t / (YinS))

    r = (mars.pos - sun.pos) * Lunar
    rmag = mag(r)
    rhat = norm(r)

    Fmag = G * sun.m * mars.m / rmag ** 2
    Fnet = -Fmag * rhat

    mars.p = mars.p + Fnet * dt
    sun.p = sun.p + (-Fnet) * dt

    # update our position
    mars.pos = mars.pos + (mars.p / mars.m / Lunar) * dt
    sun.pos = sun.pos + (sun.p / sun.m / Lunar) * dt


    momentum.pos = mars.pos
    momentum.axis = mars.p
    #
    force.pos = ScaleP * mars.pos
    force.axis = ScaleF * Fnet

    t = t + dt