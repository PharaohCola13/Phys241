from __future__ import division, print_function
from visual import *
from visual.graph import *


k = 2 #N/m
L0 = 0.16 #m

base                = box()
base.size           = vector(1, 0.01, 1)
base.pos            = vector(0,-0.1,0)
base.color          = color.green

ball                = sphere(make_trail=True)
ball.pos            = vector(0.1, 0, 0.1)
ball.radius         = 0.025
ball.m              = 0.2
ball.p              = ball.m * vector(1,0,-0.6)
ball.color          = color.cyan

rod                 = cylinder()
rod.pos             = base.pos
rod.axis            = vector(0, 0.15, 0)
rod.radius          = 0.01

spring              = helix()
spring.pos          = vector(0,0,0)
spring.axis         = ball.pos + vector(0, 0, 0)
spring.thickness    = 0.003
spring.radius       = 0.01
spring.coils        = 10
spring.color        = color.orange

t = 0
dt = 0.01

while True:
	rate(100)


	s           =  mag(ball.pos) - L0
	Fspring     = -k * s * norm(ball.pos)
	Fnet        = Fspring

	ball.p     = ball.p + Fnet * dt
	ball.pos   = ball.pos + ball.p/ball.m * dt

	spring.pos  = spring.pos
	spring.axis = ball.pos - base.pos - vector(0, 0.1, 0)

	t = t + dt