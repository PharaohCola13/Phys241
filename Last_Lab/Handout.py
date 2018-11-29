from __future__ import division, print_function
from visual import *
from visual.graph import *

scene = display(width=1000, height=1000)
scene.up = vector(-1, 1, 1)
scene.forward = vector(-55,55, -55)
scene.autocenter = True
#scene.center = vector(45, 45, 45)
#scene.center = vector(25, 25, 25)
scene.userspin = True
scene.userzoom = True

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

theta   = radians(8)
g       = vector(0, 0 , -9.81) # in m/s^2
alpha   = radians(40)
decayfactor = 0.65

ball        = sphere(make_trail=True)
ball.pos    = vector(0, 0, 0)
ball.v      = 30 * vector(sin(theta)*cos(alpha), sin(theta)*sin(alpha), cos(theta))# in m/s
ball.radius = 1
ball.color  = color.green
ball.m      = 1
ball.p      = ball.m * ball.v

Fgrav = ball.m * g
Fnet = Fgrav
t = 0
dt = 0.01

ballstop = []
while True:
    rate(400)
    if ball.pos.z < 0.0:
        print("Bounce #{}".format(len(ballstop)+1))
        ball.p.z  = -0.65 * ball.p.z
        ballstop.append(ball.p.z)
    if ball.p.z < 0.0:
        if ball.p.z > -0.1:
            ball.p.z = 0.65 * ball.p.z
    if len(ballstop) == 6:
        break
    if ball.pos.x > 75:
        break

    ball.p      = vector(ball.p.x, ball.p.y, ball.p.z) + Fnet * dt
    ball.pos    = ball.pos + (ball.p/ball.m) * dt

    t = t + dt