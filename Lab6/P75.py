from __future__ import division, print_function
from visual import *
from visual.graph import *


L0  = 0.1 #m
s0  = 0.02

#base                = box()
#base.size           = vector(1, 0.01, 1)
##base.pos            = vector(0,0,0)
#base.color          = color.green

ball                = sphere(make_trail=True)
ball.pos            = vector(0.02, 0, 0)
ball.radius         = 0.025
ball.m              = 0.1
ball.p              = ball.m * vector(0,0,0)
ball.color          = color.cyan

rod                 = cylinder()
rod.pos             = vector(0,0,0) #base.pos
rod.axis            = vector(0, 0.15, 0)
rod.radius          = 0.01

spring              = helix()
spring.pos          = ball.pos
spring.axis         = rod.axis
spring.thickness    = 0.003
spring.radius       = 0.01
spring.coils        = 10
spring.color        = color.orange

t = 0
dt = 0.01

#while t <200 *dt:
while True:
	rate(10)

	s           = mag(ball.pos) - L0
	Fspring     = -(1.5e9 * s**7) * norm(ball.pos)
	print(Fspring)
	#print(s)
	Fnet        = Fspring

	ball.p     = ball.p + Fnet * dt
	ball.pos   = ball.pos + ball.p/ball.m * dt

	#spring.pos  = spring.pos
	spring.axis = ball.pos - rod.pos

	t = t + dt