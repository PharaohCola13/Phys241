# Spencer Riley

from __future__ import division, print_function
from visual import *
#from screenshot import GetScreenShot # Required to have screenshot.py


# create a 'cube', of radius 3, with one sphere at each corner
# Part (a)

# Bottom Front Left
one                     = sphere()
one.pos         		= 3 * vector(-1,-1,1)
one.radius      		= 0.5
one.color       		= color.red

# Top Front Right
two             		= sphere()
two.pos         		= 3 * vector(1,1,1)
two.radius      		= 0.5
two.color       		= color.cyan

# Bottom Front Right
three           		= sphere()
three.pos       		= 3 * vector(1, -1, 1)
three.radius    		= 0.5
three.color     		= color.green

# Top Front Left
four            		= sphere()
four.pos        		= 3 * vector(-1,1, 1)
four.radius     		= 0.5
four.color      		= color.blue

# Bottom Back Left
five            		= sphere()
five.pos        		= 3 * vector(-1, -1, -1)
five.radius     		= 0.5
five.color      		= color.yellow

# Top Back Right
six             		= sphere()
six.pos         		= 3 * vector(1, 1, -1)
six.radius      		= 0.5
six.color       		= color.white

# Bottom Back Right
seven           		= sphere()
seven.pos       		= 3 * vector(1, -1, -1)
seven.radius    		= 0.5
seven.color     		= color.orange

# Top Back Left
eight           		= sphere()
eight.pos       		= 3 * vector(-1, 1, -1)
eight.radius    		=  0.5
eight.color     		= color.magenta

#GetScreenShot(1) # Triggers the GetScreenShota Function

# Part (b)
# Produces an arrow that connects from sphere one to sphere six

arrow                 = arrow()
arrow.pos             = one.pos
arrow.axis            = 2 * six.pos
arrow.shaftwidth      = 0.2
arrow.color           = color.cyan

#GetScreenShot(1) # Triggers the GetScreenShotb Function

# Note: that the screenshots displayed in the document have been cropped.
