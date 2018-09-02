from __future__ import division, print_function
from visual import *
from commands import *

# Used to get a screenshot
def GetScreenShot(FrameNumber):
    tmp          = getoutput('/usr/bin/gnome-screenshot') # Uses gnome-screenshot to take screenshot
    tmp          = getoutput('mv ~/Pictures/Screenshot*.png ~/PycharmProjects/Physics/Lab1/P75.png') # moves it from default directory to Lab1


scene.width  = 500 # Changes the width of the vpython visual
scene.height = 500 # Changes the height of the vpython visual

FrameNumber = 1 # Denotes a single frame

i_hat 			= vector(1, 0, 0) # creates the i hat direction
j_hat 			= vector(0, 1, 0) # creates the j hat direction
k_hat 			= vector(0, 0, 1) # creates the k hat direction

while i_hat.x < 10: 	# while the x-component of i_hat is less than 10, create a series of equally spaced boxes along the x-axis
    x_box 		= box() # creates a box in the positive i hat direction
    x_box.pos 	= i_hat

    neg_x_box 	= box() # creates a box in the negative i hat direction
    neg_x_box.pos = -1 * i_hat

    i_hat.x 		= i_hat.x + 2 # separates each box by 2 units

while j_hat.y < 10: 	# while the y-component of j_hat is less than 10, create a series of equally spaced boxes along the y-axis
    y_box 		= box() # creates a box in the positive j hat direction
    y_box.pos 	= j_hat

    neg_y_box 	= box() # creates a box in the negative j hat direction
    neg_y_box.pos = -1 * j_hat

    j_hat.y 		= j_hat.y + 2 # separates each box by 2 units

while k_hat.z < 10:	# while the z-componet of k_hat is less than 10, create a series of equally spaced boxes along the z-axis
    z_box 		= box()
    z_box.pos 	= k_hat

    neg_z_box 	= box()
    neg_z_box.pos = -1 * k_hat

    k_hat.z 		= k_hat.z + 2 # separates each box by 2 units

GetScreenShot(FrameNumber) # Triggers the GetScreenShot Function

# Note: that the screenshots displayed in the document have been cropped.