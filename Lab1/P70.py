from __future__ import division, print_function
from visual import *
from commands import *

# Used to get a screenshot
def GetScreenShot(FrameNumber):
    tmp          = getoutput('/usr/bin/gnome-screenshot') # Uses gnome-screenshot to take screenshot
    tmp          = getoutput('mv ~/Pictures/Screenshot*.png ~/PycharmProjects/Physics/Lab1/P70.png') # moves it from default directory to Lab1


scene.width  = 500 # Changes the width of the vpython visual
scene.height = 500 # Changes the height of the vpython visual

FrameNumber = 1 # Denotes a single frame

# 70
# Create an x,y,z axis with cylinders of different colors

# The x-axis
x_axis      		= cylinder()
x_axis.pos  		= vector(1, 0, 0)
x_axis.axis 		= 10 * vector(1, 0, 0)
x_axis.color 		= color.red

neg_x_axis      	= cylinder()
neg_x_axis.pos  	= -1 * x_axis.pos
neg_x_axis.axis 	= -1 * x_axis.axis
neg_x_axis.color 	= x_axis.color

# The y-axis

y_axis      		= cylinder()
y_axis.pos  		= vector(0, 1, 0)
y_axis.axis 		= 10 * vector(0, 1, 0)
y_axis.color 		= color.blue

neg_y_axis      	= cylinder()
neg_y_axis.pos  	= -1 * y_axis.pos
neg_y_axis.axis 	= -1 * y_axis.axis
neg_y_axis.color 	= y_axis.color

# The z-axis

z_axis      		= cylinder()
z_axis.pos  		= vector(0, 0, -1)
z_axis.axis 		= 10 * vector(0, 0, 1)
z_axis.color 		= color.green

neg_z_axis      	= cylinder()
neg_z_axis.pos  	= -1 * z_axis.pos
neg_z_axis.axis 	= -1 * z_axis.axis
neg_z_axis.color 	= z_axis.color

GetScreenShot(FrameNumber) # Triggers the GetScreenShot Function

# Note: that the screenshots displayed in the document have been cropped.