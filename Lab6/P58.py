from __future__ import division, print_function
from visual import *
from visual.graph import *


k   = 0.9 # in N/m
L0  = 0.20 # in m
g   = 9.81

base                = box()
base.size           = vector(0.2, 0.01, 0.2)
base.pos            = vector(0,0,0)
base.color          = color.green

block               = sphere(make_trail=True)
#block.pos           = vector(0, -0.418, 0)
block.pos           = vector(0.1, -0.1, 0)

block.radius        = 0.025
block.m             = 0.02
block.p             = block.m * vector(0,0,0)
block.color         = color.orange

spring              = helix()
spring.pos          = base.pos
spring.axis         = block.pos - base.pos
spring.thickness    = 0.003
spring.radius       = 0.01
spring.coils        = 40

fgrav = block.m * g * vector(0,-1,0)
fpara =  dot(fgrav,norm(block.p)) * norm(block.p)
fortho = fgrav - fpara


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

t   = 0
dt  = 0.001


while True:
	rate(100)

	s           = mag(block.pos) - L0
	Fspring     = -k * s * norm(block.pos)
	Fnet        = fgrav + Fspring

	block.p     = block.p + Fnet*dt
	block.pos   = block.pos + block.p/block.m * dt

	spring.axis = block.pos - base.pos

	fgrav = block.m * g * vector(0, -1, 0)
	fpara = dot(Fnet, norm(block.p)) * norm(block.p)
	fortho = Fnet - fpara

	fnet.pos    = block.pos
	fnet.axis   = Fnet

	fp.pos = block.pos
	fp.axis = 1.1 * fpara

	fo.pos = block.pos
	fo.axis = 2 *fortho

	t = t + dt
