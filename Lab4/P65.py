# Spencer Riley
from __future__ import print_function, division
from visual import *

# Declare constants
D       = 6.4e7 # 10 times the radius of the Earth
G       = 6.7e-11  # Nm2/kg2
ScaleP = 1e-8 # Scalar factor for the momentum arrow
ScaleF = 1e-4 # Scalar factor for the force arrow

# Create objects
earth           = sphere()
earth.pos       = vector(0, 0, 0)
earth.radius    = 0.1
earth.material  = materials.earth

earth.v        = vector(0, 0, 0)
earth.m         = 6e24  # kg
earth.p         = earth.m * earth.v

craft           = sphere(make_trail=True)
craft.pos       = vector(1, 0, 0)
craft.radius    = 0.01
craft.color     = color.white

craft.m         = 1.5e4 # kg

# Circular Orbit
craft.v        = vector(0, sqrt(G * earth.m/(mag(craft.pos) * D)), 0)

# Elliptical Orbit
#craft.v0        = 0.75 * vector(0, sqrt(G * earth.m/(mag(craft.pos) * AU2m)), 0)

# Arrow used to represent the momentum 
# momentum = arrow()
# momentum.color = color.green
#
# Arrow used to represent the net force
# force = arrow()
# force.color = color.magenta

craft.p         = craft.m * craft.v

t   = 0 # Initial Time
dt  = 60 # Time step

while True:
    rate(1e3)
    
    # Distance between the craft and the earth
    r           = (craft.pos - earth.pos) * D
    rmag        = mag(r)
    rhat        = norm(r)
    
    # Gravitational Force
    Fmag        = G * (earth.m * craft.m)/rmag**2
    Fnet        = -Fmag * rhat

    # Update Momentum of craft
    craft.p     = craft.p + Fnet * dt
    # Update Position of craft
    craft.pos   = craft.pos + (craft.p /craft.m/D) * dt

    # momentum.pos = craft.pos
    # momentum.axis = ScaleP * craft.p
    #
    # force.pos = craft.pos
    # force.axis = ScaleF * Fnet

    t = t + dt








