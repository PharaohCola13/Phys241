# Spencer Riley
from __future__ import division, print_function
from visual import *

observation = []
slices = []

yobs = 0.4
oofpez = 9e9

R = 0.15

Qtot = 1e-9
def calc(m, n, L):
    scene = display()
    dtheta = pi / 6
    theta = 0
    dy = L / n
    y0 = -L / 2 + dy / 2
    i = 0
    while i < n:
        a           = sphere()
        a.pos       = vector(0, y0+i*dy, 0)
        a.radius    = dy/2
        a.color     = color.red
        a.q         = Qtot/n

        slices.append(a)
        i = i + 1
    while theta < 2 * pi:
        k = 0
        while k < L:
            a       = arrow()
            a.pos   = vector(R * cos(theta), -(L)*yobs+k, R*sin(theta))
            a.color = color.orange
            a.axis  = vector(0,0,0)
            observation.append(a)
            k = k + L/m
        theta   = theta + dtheta

    af = 0.0009
    j = 0
    while j < len(observation):
        rate(5e5)
        earrow = observation[j]
        i = 0
        E_net = vector(0,0,0)
        while i < n:
            r = earrow.pos - slices[i].pos
            rhat = norm(r)
            E_net = E_net + ((oofpez) * slices[i].q/mag(r)**2) * rhat
            i = i + 1

        earrow.axis = af * E_net
        j = j + 1
    return E_net

l = 1
r = vector(0, yobs, 0)
E = (oofpez) * (Qtot/(mag(r)*sqrt(mag(r)**2 + (l/2)**2))) * norm(r)
print(E)
Ea = calc(5, 10, l)
Eb = calc(5, 16, l)

print(E-Ea)
print(E-Eb)