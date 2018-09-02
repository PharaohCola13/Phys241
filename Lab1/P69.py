# Spencer Riley

from __future__ import division, print_function
from visual import *
from commands import *


# Used to get a screenshot for part (a)
def GetScreenShota(FrameNumber):
    tmp          = getoutput('/usr/bin/gnome-screenshot') # Uses gnome-screenshot to take screenshot
    tmp          = getoutput('mv ~/Pictures/Screenshot*.png ~/PycharmProjects/Physics/Lab1/P69a.png') # moves it from default directory to Lab1

# Used to get a screenshot for part (b)
def GetScreenShotb(FrameNumber):
    tmp          = getoutput('/usr/bin/gnome-screenshot') # Uses gnome-screenshot to take screenshot
    tmp          = getoutput('mv ~/Pictures/Screenshot*.png ~/PycharmProjects/Physics/Lab1/P69b.png') # moves it from default directory to Lab1



scene.width  = 500 # Changes the width of the vpython visual
scene.height = 500 # Changes the height of the vpython visual

FrameNumber = 1 # Denotes a single frame

# 69(a)
# create a 'cube', of radius 3, with one sphere at each corner

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

GetScreenShota(FrameNumber) # Triggers the GetScreenShota Function

# 69(b)
arrow                 = arrow()
arrow.pos             = one.pos
arrow.axis            = 2 * six.pos
arrow.shaftwidth      = 0.2
arrow.color           = color.cyan

GetScreenShotb(FrameNumber) # Triggers the GetScreenShotb Function

# Note: that the screenshots displayed in the document have been cropped.