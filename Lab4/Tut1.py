from __future__ import division, print_function
from visual import *

# Constants
G = 6.7e-11
Fscale = 4.5e4

mcraft  = 15e3
mplanet = 6e24

planet              = sphere()
planet.radius       = 6.4e6
planet.pos          = vector(0,0,0)
planet.color        = color.magenta
planet.m            = mplanet

craft               = sphere()
craft.radius        = 3e6
craft.pos           = vector(-13e7, 6.5e7, 0)
craft.color         = color.red
craft.m             = mcraft

craft_one           = sphere()
craft_one.radius    = 3e6
craft_one.pos       = vector(-6.5e7, 6.5e7, 0)
craft_one.color     = color.orange
craft_one.m         = mcraft

craft_two           = sphere()
craft_two.radius    = 3e6
craft_two.pos       = vector(0, 6.5e7, 0)
craft_two.color     = color.yellow
craft_two.m         = mcraft

craft_three         = sphere()
craft_three.radius  = 3e6
craft_three.pos     = vector(6.5e7, 6.5e7, 0)
craft_three.color   = color.green
craft_three.m       = mcraft

craft_four          = sphere()
craft_four.radius   = 3e6
craft_four.pos      = vector(13e7, 6.5e7, 0)
craft_four.color    = color.cyan
craft_four.m        = mcraft

r       = craft.pos - planet.pos
rmag    = mag(r)
rhat    = Fscale * norm(r)

r1       = craft_one.pos -  planet.pos
rmag1    = mag(r1)
rhat1    = Fscale * norm(r1)

r2       = craft_two.pos -  planet.pos
rmag2    = mag(r2)
rhat2    = Fscale * norm(r2)

r3       = craft_three.pos -  planet.pos
rmag3    = mag(r3)
rhat3    = Fscale * norm(r3)

r4       = craft_four.pos -  planet.pos
rmag4    = mag(r4)
rhat4    = Fscale * norm(r4)


Fgrav    = G * (mplanet * mcraft)/(rmag**2)
Fgrav1   = G * (mplanet * mcraft)/(rmag1**2)
Fgrav2   = G * (mplanet * mcraft)/(rmag2**2)
Fgrav3   = G * (mplanet * mcraft)/(rmag3**2)
Fgrav4   = G * (mplanet * mcraft)/(rmag4**2)

Fnet     = -Fgrav  * rhat
Fnet1    = -Fgrav1 * rhat1
Fnet2    = -Fgrav2 * rhat2
Fnet3    = -Fgrav3 * rhat3
Fnet4    = -Fgrav4 * rhat4


print("Fnet = {} N".format(Fnet))

print(rmag)
gvector             = arrow()
gvector.pos         = craft.pos
gvector.axis        = Fnet
gvector.color       = color.yellow

gvector_one         = arrow()
gvector_one.pos     = craft_one.pos
gvector_one.axis    = Fnet1
gvector_one.color   = color.yellow

gvector_two         = arrow()
gvector_two.pos     = craft_two.pos
gvector_two.axis    = Fnet2
gvector_two.color   = color.yellow

gvector_three       = arrow()
gvector_three.pos   = craft_three.pos
gvector_three.axis  = Fnet3
gvector_three.color = color.yellow

gvector_four        = arrow()
gvector_four.pos    = craft_four.pos
gvector_four.axis   = Fnet4
gvector_four.color  = color.yellow