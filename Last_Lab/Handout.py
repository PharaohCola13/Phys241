# Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *

# Sets up display to approximently match the figure in the handout
scene = display(width=1000, height=1000)
scene.up = vector(-1, 1, 1)
scene.forward = vector(-55,55, -55)
scene.autocenter = True
scene.userspin = True
scene.userzoom = True

# Constants
theta   = radians(8)
g       = vector(0, 0 , -9.81) # in m/s^2
alpha   = radians(40)
decay   = 0.65

# X-axis
x_axis          = arrow()
x_axis.pos      = vector(0,0,0)
x_axis.axis     = 75 * vector(1, 0, 0)
x_axis.color    = color.red
x_axis.shaftwidth = 1

# Y-axis
y_axis          = arrow()
y_axis.pos      = vector(0,0,0)
y_axis.axis     = 75 * vector(0, 1, 0)
y_axis.color    = color.cyan
y_axis.shaftwidth = 1

# Z-axis
z_axis          = arrow()
z_axis.pos      = vector(0,0,0)
z_axis.axis     = 75 * vector(0, 0, 1)
z_axis.color    = color.yellow
z_axis.shaftwidth = 1

# Creates the ball
ball        = sphere(make_trail=True)
ball.pos    = vector(0, 0, 0)
ball.v      = 30 * vector(sin(theta)*cos(alpha), sin(theta)*sin(alpha), cos(theta))# in m/s
ball.radius = 1
ball.color  = color.green
ball.m      = 1
ball.p      = ball.m * ball.v

# Creates the base
base        = box()
base.pos    = vector(37.5, 37.5, 0)
base.size   = vector(75, 75, 0)
base.color  = color.blue
base.material = materials.wood

# Force of Gravity acting on the ball
Fgrav = ball.m * g
Fnet = Fgrav

# Initial Time
t = 0
# Time step
dt = 0.01
# List used to stop printing bounce info
ballstop = []
while True:
	rate(400)
# Stuff that happens when the ball hits the floor
	if ball.pos.z < 0.0:
		if len(ballstop) + 1 <= 6:
			print("Bounce #{}:\nt = {} s\nv = {} m/s".format(len(ballstop) + 1, t, ball.p / ball.m))
		ball.p.z  = -decay * ball.p.z
		ballstop.append(ball.p.z)
# Stuff that happens when the ball reaches zmax
	if ball.p.z < 0.0:
		if ball.p.z > -0.1:
			ball.p.z = decay * ball.p.z
# Breaks loop when ball position exceeds the boundary
	if ball.pos.x > 75:
		break
# Updates ball momentum
	ball.p      = vector(ball.p.x, ball.p.y, ball.p.z) + Fnet * dt
# Updates ball position
	ball.pos    = ball.pos + (ball.p/ball.m) * dt
# Updates time
	t = t + dt