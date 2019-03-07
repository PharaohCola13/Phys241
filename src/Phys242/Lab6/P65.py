# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

oofpez = 9e9
Q_tot = 4e-8
L = 0.12  # [m]

slices = []
def parta(n, h):
    i = 0
    W = 0.02  # [m]
    H = 0.04
    E_net = vector(0, 0, 0)
    while i < n:
        strip = box()
        strip.pos = vector(0, H*i, 0)
        strip.size = vector(L, H, W)
        strip.color = color.red
        strip.q     = Q_tot/n

        slices.append(strip)
        i = i + 1

    j = 0
    b = int((n/2) - 0.5)
    print(b)
    r_obs = (slices[b].pos) + vector(0, 0, 0.03)
    while j < n:
        rate(100)
        r = r_obs - slices[j].pos
        rhat = norm(r)
        E = (oofpez * slices[j].q/mag(r)**2) * rhat
        E_net = E_net + E
        j = j + 1
    return E_net, r_obs
scene = display()
Enets = [parta(8, 0.01)]
Enets.append(parta(3, 0.04))
scene1 = display()
for k in range(0,2):
    scl = 0.75 * L / mag(Enets[k][0])
    E_arrow = arrow()
    E_arrow.pos = Enets[k][1]
    E_arrow.axis = scl * Enets[k][0]
    E_arrow.color = color.green
#print("{}".format(partb(8, 0.01) - parta(3, 0.04)))