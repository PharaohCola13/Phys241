from __future__ import division, print_function
from visual import *

scene.width = 900
scene.height = 900

# Constants
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
dt     = 60
t      = 0

Earth = sphere()
Earth.pos = vector(0,0,0)
Earth.radius = 6.4e6
Earth.color = color.cyan

craft = sphere(make_trail=True)
craft.pos = vector(-10*Earth.radius, 0, 0)
craft.radius = 1e6
craft.color = color.yellow

vcraft = vector(0, 2e3, 0)
pcraft = mcraft * vcraft

momentum = arrow()
momentum.color = color.green

force = arrow()
force.color = color.magenta

while True:
    rate(100)

    r = craft.pos - Earth.pos
    rmag = mag(r)
    rhat = norm(r)

    fgrav = G * (mEarth * mcraft)/rmag**2
    fnet = -fgrav * rhat

    pcraft = pcraft + fnet * dt
    craft.pos = craft.pos + (pcraft/mcraft)*dt

    force.pos = craft.pos
    force.axis = fnet

    momentum.pos = craft.pos
    momentum.axis = pcraft

    t = t + dt