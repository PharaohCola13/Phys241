# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

scene.height = 800
oofpez = 9e9
Qtot = -2e-9
L = 0.5
N = 50
dx = L/N

r_obs = vector(-0.4, 0.3, 0.3)
E_net = vector(0,0,0)
slices = []
i = 0
x0 = -L/2 + dx/2
while i < N:
    a = sphere()
    a.pos = vector(x0+i*dx, 0, 0)
    a.radius = dx/2
    a.color = color.red
    a.q     = Qtot/N

    slices.append(a)
    i = i + 1
i = 0
while i < N:
    rate(100)
    r = r_obs - slices[i].pos
    rhat = norm(r)
    E = (oofpez * slices[i].q/mag(r)**2) * rhat
    E_net = E_net + E
    i = i + 1

scl = 0.25 * L/mag(E_net)
E_arrow = arrow()
E_arrow.pos = r_obs
E_arrow.axis = scl* E_net
E_arrow.color = color.green

E_analy = oofpez * Qtot/(mag(r_obs)*sqrt(mag(r_obs)**2+(L/2)**2)) * rhat

print("The numerical electric field is {} N/C".format(E_net))
print("The analytical electric field is {} N/C".format(E_analy))
print("The difference between the solutions is {} N/C".format(E_net - E_analy))