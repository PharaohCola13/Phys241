from __future__ import division, print_function
from visual import *
from visual.graph import *


k = 30 #in N/m
L0 = 0.50 # in meters

wall1 		= box()
wall1.color = color.yellow
wall1.pos 	= vector(L0, 0,0)
wall1.size	= vector(0.01, 1, 1)

wall2 = box()
wall2.color = color.yellow
wall2.pos = vector(-L0, 0,0)
wall2.size = vector(0.01, 1, 1)

wall3 = box()
wall3.color = color.yellow
wall3.pos = vector(0, L0, 0)
wall3.size = vector(1, 0.01, 1)

wall4 = box()
wall4.color = color.yellow
wall4.pos = vector(0, -L0, 0)
wall4.size = vector(1, 0.01, 1)

wall5 = box()
wall5.color = color.yellow
wall5.pos = vector(0, 0, -L0)
wall5.size = vector(1, 1, 0.01)

ball        = sphere(make_trail = True)
ball.pos    = vector(-0.1,0, 0)
ball.radius = 0.1
ball.m      = 0.03
ball.color  = color.magenta
ball.p      = ball.m * vector(0.4, 0.4,0.4)

spring1 			 = helix()
spring1.pos          = wall1.pos
spring1.axis         = ball.pos - wall1.pos
spring1.thickness    = 0.01
spring1.radius       = 0.05
spring1.coils        = 5
spring1.color        = color.blue

spring2 = helix()
spring2.pos          = wall2.pos
spring2.axis         = ball.pos - wall2.pos
spring2.thickness    = 0.01
spring2.radius       = 0.05
spring2.coils        = 5
spring2.color        = color.blue

spring3 = helix()
spring3.pos          = wall3.pos
spring3.axis         = ball.pos - wall3.pos
spring3.thickness    = 0.01
spring3.radius       = 0.05
spring3.coils        = 5
spring3.color        = color.blue

spring4 = helix()
spring4.pos          = wall4.pos
spring4.axis         = ball.pos - wall4.pos
spring4.thickness    = 0.01
spring4.radius       = 0.05
spring4.coils        = 5
spring4.color        = color.blue

spring5 = helix()
spring5.pos          = wall5.pos
spring5.axis         = ball.pos - wall5.pos
spring5.thickness    = 0.01
spring5.radius       = 0.05
spring5.coils        = 5
spring5.color        = color.blue

spring6 = helix()
spring6.pos          = vector(0,0, L0)
spring6.axis         = ball.pos - vector(0,0,L0)
spring6.thickness    = 0.01
spring6.radius       = 0.05
spring6.coils        = 5
spring6.color        = color.blue

t = 0
dt = 0.001

while True:
	rate(100)

	s 		= mag(ball.pos) - L0
	Fspring = k * s * norm(ball.pos)
	Fnet 	=  Fspring

	ball.p     = ball.p + Fnet*dt
	ball.pos   = ball.pos + ball.p/ball.m * dt

	spring1.axis = ball.pos - wall1.pos
	#print(spring1.axis)
	spring2.axis = ball.pos - wall2.pos
	spring3.axis = ball.pos - wall3.pos
	spring4.axis = ball.pos - wall4.pos
	spring5.axis = ball.pos - wall5.pos
	spring6.axis = ball.pos - vector(0,0,L0)

	t = t +dt