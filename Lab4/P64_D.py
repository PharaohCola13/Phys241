from __future__ import division, print_function
from visual import *

# Constants
G = 6.7e-11 # Gravitational Constant
#Fscale1 = 4.5e4 # Scaling factor
Fscale2 = 4.5e5

mcraft  = 15e3 # mass of crafts in kg
mplanet = 6e24 # mass of planet in kg

# Creates planet
planet              = sphere()
planet.radius       = 6.4e6 # in meters
planet.pos          = vector(0,0,0)
planet.color        = color.magenta
planet.m            = mplanet

# Creates first craft
craft1              = sphere()
craft1.radius       = 3e6 # in meters
craft1.pos          = vector(-13e7, 6.5e7, 0)
craft1.color        = color.red
craft1.m            = mcraft

# Creates second craft
craft2              = sphere()
craft2.radius       = 3e6 # in meters
craft2.pos          = vector(-6.5e7, 6.5e7, 0)
craft2.color        = color.orange
craft2.m            = mcraft

# Creates third craft
craft3              = sphere()
craft3.radius       = 3e6 # in meters
craft3.pos          = vector(0, 6.5e7, 0)
craft3.color        = color.yellow
craft3.m            = mcraft

# Creates fourth craft
craft4            = sphere()
craft4.radius     = 3e6 # in meters
craft4.pos        = vector(6.5e7, 6.5e7, 0)
craft4.color      = color.green
craft4.m          = mcraft

# Creates fifth craft
craft5            = sphere()
craft5.radius     = 3e6 # in meters
craft5.pos        = vector(13e7, 6.5e7, 0)
craft5.color      = color.cyan
craft5.m          = mcraft

# Calculates the distance between the planet and the crafts
r1       = craft1.pos - planet.pos
r1mag    = mag(r1)
r1hat    = Fscale2 * norm(r1)

r2       = craft2.pos -  planet.pos
r2mag    = mag(r2)
r2hat    = Fscale2 * norm(r2)

r3       = craft3.pos -  planet.pos
r3mag    = mag(r3)
r3hat    = Fscale2 * norm(r3)

r4       = craft4.pos -  planet.pos
r4mag    = mag(r4)
r4hat    = Fscale2 * norm(r4)

r5       = craft5.pos -  planet.pos
r5mag    = mag(r5)
r5hat    = Fscale2  * norm(r5)

# Magnitude of the gravitational force acting on the crafts
Fgrav1   = G * (mplanet * mcraft)/(r1mag**2)
Fgrav2   = G * (mplanet * mcraft)/(r2mag**2)
Fgrav3   = G * (mplanet * mcraft)/(r3mag**2)
Fgrav4   = G * (mplanet * mcraft)/(r4mag**2)
Fgrav5   = G * (mplanet * mcraft)/(r5mag**2)
# Part D
# Calculates the net force acting on the planet (Newton's 3rd Law)
Fnet1p = -Fgrav1 * r1hat
Fnet2p = -Fgrav2 * r2hat
Fnet3p = -Fgrav3 * r3hat
Fnet4p = -Fgrav4 * r4hat
Fnet5p = -Fgrav5 * r5hat

# Creates the arrows points towards the crafts
gvector1p        = arrow()
gvector1p.pos    = Fnet1p
gvector1p.axis   = craft1.pos
gvector1p.color  = color.red
gvector1p.shaftwidth = 5e6

gvector2p        = arrow()
gvector2p.pos    = Fnet2p
gvector2p.axis   = craft2.pos
gvector2p.color  = color.orange
gvector2p.shaftwidth = 5e6

gvector3p        = arrow()
gvector3p.pos    = Fnet3p
gvector3p.axis   = craft3.pos
gvector3p.color  = color.yellow
gvector3p.shaftwidth = 5e6

gvector4p        = arrow()
gvector4p.pos    = Fnet4p
gvector4p.axis   = craft4.pos
gvector4p.color  = color.green
gvector4p.shaftwidth = 5e6

gvector5p        = arrow()
gvector5p.pos    = Fnet5p
gvector5p.axis   = craft5.pos
gvector5p.color  = color.cyan
gvector5p.shaftwidth = 5e6

# Prints out the force acting on the planet by the crafts
print("The force of gravity acting on the planet by craft one is {} N".format(Fnet1p))
print("The force of gravity acting on the planet by craft two is {} N".format(Fnet2p))
print("The force of gravity acting on the planet by craft three is {} N".format(Fnet3p))
print("The force of gravity acting on the planet by craft four is {} N".format(Fnet4p))
print("The force of gravity acting on the planet by craft five is {} N".format(Fnet5p))
