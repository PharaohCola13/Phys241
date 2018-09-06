# Spencer Riley

from __future__ import division, print_function
from visual import *
#from screenshot import GetScreenShot # Required to have screenshot.py

# Create an x,y,z axis with cylinders of different colors

# The x-axis
# Positve
x_axis      		= cylinder()
x_axis.pos  		= vector(1, 0, 0)
x_axis.axis 		= 10 * vector(1, 0, 0)
x_axis.color 		= color.red

# Negative
neg_x_axis      	= cylinder()
neg_x_axis.pos  	= -1 * x_axis.pos
neg_x_axis.axis 	= -1 * x_axis.axis
neg_x_axis.color 	= x_axis.color

# The y-axis
# Positive
y_axis      		= cylinder()
y_axis.pos  		= vector(0, 1, 0)
y_axis.axis 		= 10 * vector(0, 1, 0)
y_axis.color 		= color.blue

# Negative
neg_y_axis      	= cylinder()
neg_y_axis.pos  	= -1 * y_axis.pos
neg_y_axis.axis 	= -1 * y_axis.axis
neg_y_axis.color 	= y_axis.color

# The z-axis
# Positve
z_axis      		= cylinder()
z_axis.pos  		= vector(0, 0, -1)
z_axis.axis 		= 10 * vector(0, 0, 1)
z_axis.color 		= color.green

# Negative
neg_z_axis      	= cylinder()
neg_z_axis.pos  	= -1 * z_axis.pos
neg_z_axis.axis 	= -1 * z_axis.axis
neg_z_axis.color 	= z_axis.color

# GetScreenShot(1) # Triggers the GetScreenShot Function

# Note: that the screenshots displayed in the document have been cropped.
