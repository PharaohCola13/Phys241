# Spencer Riley
from __future__ import print_function, division
from visual import *

# Declare constants
AU2m    = 6.4e7 #meters in an AU
G       = 6.7e-11  # Nm2/kg2
ScaleP = 1e-8
ScaleF = 1e-4

# Create objects
earth           = sphere()
earth.pos       = vector(0, 0, 0)
earth.radius    = 0.1
earth.material  = materials.earth

earth.v0        = vector(0, 0, 0)
earth.m         = 6e24  # kg
earth.p         = earth.m * earth.v0

craft           = sphere(make_trail=True)
craft.pos       = vector(1, 0, 0)
craft.radius    = 0.01
craft.color     = color.white

craft.m         = 1.5e4 # kg
# Circular Orbit
craft.v0        = vector(0, sqrt(G * earth.m/(mag(craft.pos) * AU2m)), 0)


# Elliptical Orbit
#craft.v0        = 0.75 * vector(0, sqrt(G * earth.m/(mag(craft.pos) * AU2m)), 0)

# momentum = arrow()
# momentum.color = color.green
#
# force = arrow()
# force.color = color.magenta
# a)
#craft.v0        = vector(0, sqrt(G * earth.m/(mag(craft.pos) * AU2m)), 0)
craft.p         = craft.m * craft.v0

t   = 0
dt  = 60

while True:
    rate(1e3)

    r           = (craft.pos - earth.pos) * AU2m
    rmag        = mag(r)
    rhat        = norm(r)

    Fmag        = G * (earth.m * craft.m)/rmag**2
    Fnet        = -Fmag * rhat

    craft.p     = craft.p + Fnet * dt
    craft.pos   = craft.pos + (craft.p /craft.m/AU2m) * dt

    # momentum.pos = craft.pos
    # momentum.axis = ScaleP * craft.p
    #
    # force.pos = craft.pos
    # force.axis = ScaleF * Fnet

    t = t + dt








