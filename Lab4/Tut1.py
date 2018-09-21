from __future__ import division, print_function
from visual import *

# Constants
G = 6.7e-11 # Gravitational constant 
Fscale = 4.5e4 # Scaling Factor

mcraft  = 15e3 # Mass of the crafts
mplanet = 6e24 # Mass of the planet

# Creates the planet
planet           = sphere()
planet.radius    = 6.4e6
planet.pos       = vector(0,0,0)
planet.color     = color.magenta
planet.m         = mplanet

craft1           = sphere()
craft1.radius    = 3e6
craft1.pos       = vector(-13e7, 6.5e7, 0)
craft1.color     = color.red
craft1.m         = mcraft

craft2           = sphere()
craft2.radius    = 3e6
craft2.pos       = vector(-6.5e7, 6.5e7, 0)
craft2.color     = color.orange
craft2.m         = mcraft

craft3           = sphere()
craft3.radius    = 3e6
craft3.pos       = vector(0, 6.5e7, 0)
craft3.color     = color.yellow
craft3.m         = mcraft

craft4          = sphere()
craft4.radius   = 3e6
craft4.pos      = vector(6.5e7, 6.5e7, 0)
craft4.color    = color.green
craft4.m        = mcraft

craft5          = sphere()
craft5.radius   = 3e6
craft5.pos      = vector(13e7, 6.5e7, 0)
craft5.color    = color.cyan
craft5.m        = mcraft

# Calculates the distance between the planet and the craft 
r1       = craft1.pos - planet.pos
r1mag    = mag(r1)
r1hat    = Fscale * norm(r1)

r2       = craft2.pos -  planet.pos
r2mag    = mag(r2)
r2hat    = Fscale * norm(r2)

r3       = craft3.pos -  planet.pos
r3mag    = mag(r3)
r3hat    = Fscale * norm(r3)

r4       = craft4.pos -  planet.pos
r4mag    = mag(r4)
r4hat    = Fscale * norm(r4)

r5       = craft5.pos -  planet.pos
r5mag    = mag(r5)
r5hat    = Fscale * norm(r5)

# Calculates the magnitude of gravitational force acting on the craft
Fgrav1   = G * (mplanet * mcraft)/(r1mag**2)
Fgrav2   = G * (mplanet * mcraft)/(r2mag**2)
Fgrav3   = G * (mplanet * mcraft)/(r3mag**2)
Fgrav4   = G * (mplanet * mcraft)/(r4mag**2)
Fgrav5   = G * (mplanet * mcraft)/(r5mag**2)

# Calculates the net force acting on the the crafts
Fnet1    = -F1grav  * r1hat
Fnet2    = -F2grav * r2hat
Fnet3    = -F3grav * r3hat
Fnet4    = -F4grav * r4hat
Fnet5    = -F5grav * r5hat

# Creates a vector pointing in the direction of the planet with a magnitude of the gravitational force
gvector1         = arrow()
gvector1.pos     = craft1.pos
gvector1.axis    = Fnet1
gvector1.color   = color.yellow

gvector2         = arrow()
gvector2.pos     = craft2.pos
gvector2.axis    = Fnet2
gvector2.color   = color.yellow

gvector3         = arrow()
gvector3.pos     = craft3.pos
gvector3.axis    = Fnet3
gvector3.color   = color.yellow

gvector4         = arrow()
gvector4.pos     = craft4.pos
gvector4.axis    = Fnet4
gvector4.color   = color.yellow

gvector5         = arrow()
gvector5.pos     = craft5.pos
gvector5.axis    = Fnet5
gvector5.color   = color.yellow
