from __future__ import division, print_function
from visual import *
from visual.graph import *
import warnings

warnings.simplefilter("error", RuntimeWarning)

L0  = 0.1 #m
s0  = 0.12
k = 2e9

base                = box()
base.size           = vector(1, 0.01, 1)
base.pos            = vector(0,-0.1,0)
base.color          = color.green

ball                = sphere(make_trail=True)
ball.pos            = vector(s0, 0, 0)
ball.radius         = 0.025
ball.m              = 0.1
ball.p              = ball.m * vector(-2,0,0)
ball.color          = color.cyan

rod                 = cylinder()
rod.pos             = vector(0,0,0)
rod.axis            = vector(0, -0.1, 0)
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

while t < 2000 * dt:
	try:
		rate(100)

		s           = mag(ball.pos) - L0
		Fspring     = -(k * s**7) * norm(ball.pos)
		Fnet        = Fspring

		ball.p      = ball.p + Fnet * dt
		ball.pos    = ball.pos + (ball.p)/(ball.m) * dt

		spring.axis = ball.pos - rod.pos

		t = t + dt
		print(t)

	except OverflowError:
		print("Over Nope")
		break
	except RuntimeWarning:
		print("Running Nope")
		break