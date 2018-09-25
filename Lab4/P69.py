# Spencer Riley
from __future__ import division, print_function
from visual import *

G       = 6.7e-11 # Gravitational Constant in Nm^2/kg^2
YinS    = 365.*24.*60.*60 # Seconds in a Earth year
AU      = 1.5e11 # Distance from Earth to the sun in meters

# First star
star             = sphere()
star.pos         = vector(0,0,0)
star.radius      = 0.1
star.m           = 2e30 # kg
star.color       = color.yellow
star.material    = materials.emissive

star.v0          = vector(0,0,0) # In m/s
star.p           = star.m * star.v0

# Second Star
star2            = sphere(make_trail = True)
star2.pos        = vector(1, 0, 0)
star2.radius     = 0.1
star2.m          = 0.5 * star.m # kg
star2.color      = color.orange
star2.material   = materials.emissive

star2.v          = vector(0, 2*pi*AU/YinS, 0) # Velocity of the Earth in m/s
star2.p          = star2.m * star2.v

t   = 0 # Initial Time
dt  = YinS/10000 # Time step

while True:
    rate(1e3)

    # Distance between the two stars
    r           = (star.pos - star2.pos)*AU
    rmag        = mag(r)
    rhat        = norm(r)

    # Gravitational Force
    Fmag        = G*(star.m * star2.m)/rmag**2
    Fnet        = -Fmag * rhat

    # Update star's momentum and position
    star.p      = star.p + Fnet * dt
    star.pos    = star.pos + (star.p/star.m/AU) * dt # In m/s

    # Updates star2's momentum and position
    star2.p     = star2.p + (-Fnet) * dt
    star2.pos   = star2.pos + (star2.p/star2.m/AU) * dt # In m/s


    t= t + dt
