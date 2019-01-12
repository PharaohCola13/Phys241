from __future__ import division, print_function
from visual import *
from random import *


rand_color = vector(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)

track       = box()
track.pos   = vector(0, -0.025, 0)
track.size  = vector(2.0, 0.05, 0.10)
track.color = color.white


cart        = box()
cart.pos    = vector(0.95,0.02,0)
cart.size   = vector(0.1, 0.04, 0.06)
cart.color  = rand_color

cart.m = 0.8
cart.p = cart.m * vector(-0.5, 0, 0)

print('cart momentum = {}'.format(cart.p))

dt      = 0.01
t       = 0

while t < 100:
    rate(100)
    F_air = vector(0.053, -0.01, 0)
    cart.p   = cart.p + F_air * dt
    cart.pos = cart.pos + (cart.p/cart.m) * dt

    t = dt + t