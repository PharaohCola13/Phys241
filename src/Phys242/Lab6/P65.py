# Spencer Riley
from __future__ import division, print_function
from visual import *

oofpez = 9e9
Q_tot = 4e-8
L = 0.12  # [m]

def calc(n, w, h):
    slices  = []
    i       = 0
    E_net   = vector(0, 0, 0)
    while i < n:
        strip       = box()
        strip.pos   = vector(0, h*i, 0)
        strip.size  = vector(L, h, w)
        strip.color = color.red
        strip.q     = Q_tot/n

        slices.append(strip)
        i   = i + 1
    j       = 0
    b       = int((n/2) - 0.5)
    r_obs   = (slices[b].pos) + vector(0, 0, 0.03)
    while j < n:
        rate(100)
        r       = r_obs - slices[j].pos
        rhat    = norm(r)
        E_net   = E_net + (oofpez * slices[j].q/mag(r)**2) * rhat
        j       = j + 1
    return E_net, r_obs

def parta():
    scene          = display()
    E, R           = calc(3, 0.02, 0.04)
    scl            = 0.75 * L / mag(E)
    E_arrow        = arrow()
    E_arrow.pos    = R
    E_arrow.axis   = scl * E
    E_arrow.color  = color.green
    return E

def partb():
    sceneb         = display()
    E, R           = calc(8, 0.01, 0.03)
    scl            = 0.75 * L / mag(E)
    E_arrow        = arrow()
    E_arrow.pos    = R
    E_arrow.axis   = scl * E
    E_arrow.color  = color.cyan
    return E

def partc():
    scenec         = display()
    E, R           = calc(100, 0.01, 0.01)
    scl            = 0.75 * L /mag(E)
    E_arrow        = arrow()
    E_arrow.pos    = R
    E_arrow.axis   = scl * E
    E_arrow.color  = color.magenta
    return E

Ea = parta()
Eb = partb()
print("{}".format(mag(Eb)-mag(Ea)))

Ec = partc()
print("{}".format(mag(Ec) - mag(Eb)))