from __future__ import division, print_function
from visual import *
# from screenshot import GetScreenShot # Required to have screenshot.py

ball1 = sphere()
ball1.pos = vector(0,0,0)
ball1.radius = 0.5
ball1.color = color.green

ball2 = sphere()
ball2.pos = vector(-3,4,0)
ball2.radius = 0.5
ball2.color = color.cyan

pointer = arrow()
pointer.pos = vector(0,0,0)
pointer.axis = ball2.pos - ball1.pos
pointer.color = color.orange

r = vector(-3,4,0)

while r.x < 10:
    rate(10)
    ball2.pos = r
    pointer.axis = ball2.pos
    r.x = r.x + 1

print('end')

