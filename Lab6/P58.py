from __future__ import division, print_function
from visual import *


k   = 0.9 # in N/m
L0  = 0.20 # in m
g   = 9.81 # in m/s^2

base                = box()
base.size           = vector(0.2, 0.01, 0.2)
base.pos            = vector(0,0,0)
base.color          = color.green

block               = sphere(make_trail=True)
#block.pos           = vector(0, -0.418, 0)
block.pos           = vector(0.1, -0.1, 0)

block.radius        = 0.025
block.m             = 0.02 # in kg
block.p             = block.m * vector(0,0,0)
block.color         = color.orange

spring              = helix()
spring.pos          = base.pos
spring.axis         = block.pos - base.pos
spring.thickness    = 0.003
spring.radius       = 0.01
spring.coils        = 40

# Gravitational Force
fgrav = block.m * g * vector(0,-1,0) # in N

# Parallel Force
fpara =  dot(fgrav,norm(block.p)) * norm(block.p) # in N

# Perpendicular Force 
fortho = fgrav - fpara # in N

fp          = arrow()
fp.pos      = block.pos
fp.axis     = fpara
fp.color    = color.blue

fo          = arrow()
fo.pos      = block.pos
fo.axis     = fortho
fo.color    = color.magenta

fnet        = arrow()
fnet.pos    = block.pos
fnet.axis   = fgrav
fnet.color  = color.red

# Initial Time
t   = 0
# Time Step
dt  = 0.001


while True:
	rate(100)
# Spring Force
	s           = mag(block.pos) - L0
	Fspring     = -k * s * norm(block.pos)
	Fnet        = fgrav + Fspring
# Updates Momentum of Ball
	block.p     = block.p + Fnet*dt
# Updates Position of Ball
	block.pos   = block.pos + block.p/block.m * dt
# Updates the position of the end of the spring
	spring.axis = block.pos - base.pos
# Updates Parallel Force
	fpara = dot(Fnet, norm(block.p)) * norm(block.p)
# Updates Perpendicular Force
	fortho = Fnet - fpara
# Updates Net Force arrow
	fnet.pos    = block.pos
	fnet.axis   = Fnet
# Updates Parallel Force Arrow
	fp.pos = block.pos
	fp.axis = 1.1 * fpara
# Updates Perpendicular Force Arrow
	fo.pos = block.pos
	fo.axis = 2 *fortho
# Updates Time
	t = t + dt
