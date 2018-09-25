# Spencer Riley
from __future__ import print_function, division
from visual import *

G = 6.7e-11  # Nm2/kg2
MinS = 30. * 24. * 60. * 60  # seconds in a month
Lunar = 3.8e8  # Distance from Earth and moon in meters

# Create objects
earth           = sphere(make_trail=True)
earth.pos       = vector(0, 0, 0)
earth.radius    = 0.1
earth.material  = materials.earth

earth.v0        = vector(0, 0, 0)
earth.m         = 6e24  # kg
earth.p         = earth.m * earth.v0

moon           = sphere(make_trail=True)
moon.pos       = vector(1, 0,0)
moon.radius    = 0.05

moon.v0        = vector(0,sqrt(G * earth.m / (mag(moon.pos) * Lunar * 0.92)), 0)  # m/s
moon.m         = 7e22  # kg
moon.p         = moon.m * moon.v0

t = 0 # Initial Time
dt = MinS / 1000 # Time Step

#Add timestamp label
timestamp = label(pos=vector(0,0.5,0),color=color.red,text='Time in Months: ')


while t < 1000 *  dt:
    rate(1e2)
    # Timestamp update
    timestamp.text ='Time in Months: {:6.2f}'.format(t/(MinS))

    # Distance between Earth and moon
    r = (moon.pos - earth.pos) * Lunar
    rmag = mag(r)
    rhat = norm(r)
    
    # Gravitational force
    Fmag = G * earth.m * moon.m / rmag**2
    Fnet = -Fmag * rhat
    
    # Update momentum and position of the moon
    moon.p = moon.p + Fnet * dt
    moon.pos = moon.pos + (moon.p / moon.m / Lunar) * dt
    
    # Update momentum and position of the Earth
    earth.pos = earth.pos + (earth.p / earth.m / Lunar) * dt
    earth.p = earth.p + (-Fnet) * dt

    t = t + dt # Time update
