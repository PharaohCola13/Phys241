from __future__ import division, print_function
from visual import *
from visual.graph import *
from random import *

rand_color = vector(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)

# Creates the graphical display for position
gd1 = gdisplay(x=550,y=0,width=700,height=500,
               title='Position of Cart',
               xtitle='Time [s]',
               ytitle='Position [m]')

# Creates the graphical display for momentum
gd2 = gdisplay(x=550, y=510, width=700, height=500,
               title='Linear Momentum of Cart',
               xtitle='Time [s]',
               ytitle='Momentum [kg * m/s]'
               )

# The track
track       = box()
track.pos   = vector(0, -0.025, 0)
track.size  = vector(2.0, 0.05, 0.10)
track.color = color.white

# The cart
cart        = box(make_trail=True)
cart.pos    = vector(0.95,0.02,0)
cart.size   = vector(0.1, 0.04, 0.06)
cart.color  = rand_color

cart.m = 0.8 # mass of cart
cart.v = vector(-0.5, 0.2, 0) # Initial velocity of cart
cart.p = cart.m * cart.v # Initial momentum of cart

dt      = 0.01 # Time step
t       = 0 # Initial time

f1 = gcurve(gdisplay = gd1, color=color.white) # Define functions to plot
f2 = gcurve(gdisplay = gd2, color=color.cyan) # Define functions to plot

while t < 15:
    rate(100)
    F_air = vector(0.053, 0, 0) # Force of air
    cart.p   = cart.p + F_air * dt # Update momentum
    cart.pos = cart.pos + (cart.p/cart.m) * dt # Update position
    f1.plot(pos=(t,cart.pos.x)) # Plots position vs time
    f2.plot(pos=(t,cart.p.x)) # plots momentum vs time
    t = dt + t # Updates time