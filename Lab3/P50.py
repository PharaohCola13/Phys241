from __future__ import division, print_function
from visual import *
from visual.graph import *
from random import *


theta = radians(15)

x_axis  = arrow()
x_axis.pos = vector(0,0,0)
x_axis.axis = 100 * vector(1, 0, 0)
x_axis.color = color.red

y_axis  = arrow()
y_axis.pos = vector(0,0,0)
y_axis.axis = 100 * vector(0, 1, 0)
y_axis.color = color.blue

z_axis  = arrow()
z_axis.pos = vector(0,0,0)
z_axis.axis = 100 * vector(0, 0, 1)
z_axis.color = color.green


rand_color = vector(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)

# racket      = box()
# racket.pos  = vector(0,0,0)
# racket.size = vector(0.3, 0.3, 0.3)

tennis_ball     = sphere(make_trail=True)
tennis_ball.pos = (0, 0, 0)
tennis_ball.m   = 0.055
tennis_ball.v   = vector((31.75)*cos(pi/4), (31.75)*sin(pi/4), 31.75)
tennis_ball.radius = 5
tennis_ball.p   = tennis_ball.m * tennis_ball.v
tennis_ball.color = rand_color
mag(tennis_ball.v)

t = 0
dt = 0.1

while t < 100 * dt:

    rate(10)
    F_grav = tennis_ball.m * vector(0, -9.81, 0)
    tennis_ball.p = tennis_ball.p + F_grav * dt
    tennis_ball.pos = tennis_ball.pos + (tennis_ball.p/tennis_ball.m) * dt

    if tennis_ball.pos.y < 0:
        break

    t = t + dt