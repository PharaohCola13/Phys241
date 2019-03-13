# Spencer Riley
from __future__ import division, print_function
from visual import *

Qtot    = 50e-9
oofpez  = 9e-9

N       = 20
slices  = []
theta   = 0
dtheta  = (2*pi)/N
R       = 0.1

electron        = sphere(make_trail=True)
#electron.pos    = vector(0.15, 0, 0)
electron.pos    = vector(0.3, -0.05,0)
electron.q      = -1.6e-19
electron.m      = 9.11e-31
#electron.p      = vector(0,0,0)
electron.p      = electron.m * vector(1e-3, 1e-3, 1e-2)
electron.radius = (pi * R)/N

while theta < 2 * pi:
    rate(1000)
    a           = sphere()
    a.radius    = (pi * R)/N
    a.pos       = vector(0,R*cos(theta), R*sin(theta))
    a.color     = color.red
    a.q         = Qtot/N
    slices.append(a)
    theta = theta + dtheta

t       = 0
dt      = 6e-3
while t < 1e3:
    E_net = vector(0, 0, 0)
    for i in range(N):
        rate(10000000000000)
        r        = electron.pos - slices[i].pos
        E_net    = E_net + ((oofpez * slices[i].q/(mag(r)**2)) * norm(r))
    Fnet = E_net * electron.q
    electron.p = electron.p + Fnet * dt
    electron.pos = electron.pos + (electron.p / electron.m) * dt

    t = t + dt
