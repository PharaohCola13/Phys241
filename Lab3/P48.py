from __future__ import division, print_function
from visual import *
from random import *

sys.path.insert(0, '../Computational Tools/')
from screenshot import GetScreenShot

# Random Color
rand_color = vector(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)

# The track
track       = box()
track.pos   = vector(0, -0.025, 0)
track.size  = vector(2.0, 0.05, 0.10)
track.color = color.white

# The cart
cart        = box(make_trail=True)
cart.pos    = vector(0.95,0.02,0) # initial position
cart.size   = vector(0.1, 0.04, 0.06) # size of cart
cart.color  = rand_color
cart.m = 0.8 # cart's mass
cart.v = vector(-0.5, 0, 0) # cart's velocity
cart.p = cart.m * cart.v # cart's momentum

dt      = 0.01 # Time step
t       = 0 # inital time

GetScreenShot(1)
# b) time to travel 2 meters is 4 seconds
while t < 100:
    rate(100)
    F_air = vector(0.053, 0, 0) # Force of the air
    cart.p   = cart.p + F_air * dt # Momentum update
    cart.pos = cart.pos + (cart.p/cart.m) * dt # Position update

    t = dt + t