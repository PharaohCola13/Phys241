from __future__ import division, print_function
from visual import *
from visual.graph import *
from random import *


rand_color = vector(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)

track       = box()
track.pos   = vector(0, -0.025, 0)
track.size  = vector(2.0, 0.05, 0.10)
track.color = color.white


cart        = box(make_trail=True)
cart.pos    = vector(0.95,0.02,0)
cart.size   = vector(0.1, 0.04, 0.06)
cart.color  = rand_color

cart.m = 0.8
cart.v = vector(-0.5, 0, 0)
cart.p = cart.m * cart.v

print('cart momentum = {}'.format(cart.p))

dt      = 0.01
t       = 0

f1 = gcurve(color=rand_color)
f2 = gcurve(color=rand_color)
# b) time to travel 2 meters is 4 seconds
while t < 15:
    rate(100)
    F_air = vector(0.053, 0, 0)
    cart.p   = cart.p + F_air * dt
    cart.pos = cart.pos + (cart.p/cart.m) * dt
# The shape of the plot is due to the component relating to the square of the time.
    f1.plot(pos=(t,cart.pos.x))
# The shape of the plot is a linear, as a result of the momentum being a linear function. Where F_air represents the slope.
    f2.plot(pos=(t,cart.p.x))
    t = dt + t