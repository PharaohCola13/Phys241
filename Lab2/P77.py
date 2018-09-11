from __future__ import division, print_function
from visual import *

ball1           = sphere()
ball1.pos       = vector(0,0,0) # position of the ball
ball1.radius    = 0.5 # size of the ball
ball1.color     = color.green

ball2           = sphere()
ball2.pos       = vector(-3,4,0) # Initial position of the ball
ball2.radius    = ball1.radius # size of the ball
ball2.color     = color.cyan

pointer         = arrow()
pointer.pos     = vector(0,0,0) # initial position of the arrow
pointer.axis    = ball2.pos - ball1.pos # finial position of the arrow
pointer.color   = color.orange

r               = vector(-3,4,0) # Initial position used to update the while loop

while r.x < 10:
    rate(10)

    ball2.pos = r

    pointer.axis = ball2.pos

    r.x = r.x + 1


