# Spencer Riley

from __future__ import division, print_function
from visual import *
from screenshot import GetScreenShot


# create a 'cube', of radius 3, with one sphere at each corner
# Part (a)

one                     = sphere()
one.pos         		= 3 * vector(-1,-1,1)
one.radius      		= 0.5
one.color       		= color.red

two             		= sphere()
two.pos         		= 3 * vector(1,1,1)
two.radius      		= 0.5
two.color       		= color.cyan

three           		= sphere()
three.pos       		= 3 * vector(1, -1, 1)
three.radius    		= 0.5
three.color     		= color.green

four            		= sphere()
four.pos        		= 3 * vector(-1,1, 1)
four.radius     		= 0.5
four.color      		= color.blue

five            		= sphere()
five.pos        		= 3 * vector(-1, -1, -1)
five.radius     		= 0.5
five.color      		= color.yellow

six             		= sphere()
six.pos         		= 3 * vector(1, 1, -1)
six.radius      		= 0.5
six.color       		= color.white

seven           		= sphere()
seven.pos       		= 3 * vector(1, -1, -1)
seven.radius    		= 0.5
seven.color     		= color.orange

eight           		= sphere()
eight.pos       		= 3 * vector(-1, 1, -1)
eight.radius    		=  0.5
eight.color     		= color.magenta

GetScreenShot(1) # Triggers the GetScreenShota Function

# Produces an arrow that connects from sphere one to sphere six
# Part (b)
arrow                 = arrow()
arrow.pos             = one.pos
arrow.axis            = 2 * six.pos
arrow.shaftwidth      = 0.2
arrow.color           = color.cyan

GetScreenShot(1) # Triggers the GetScreenShotb Function

# Note: that the screenshots displayed in the document have been cropped.