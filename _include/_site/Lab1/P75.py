# Spencer Riley

from __future__ import division, print_function
from visual import *
#from screenshot import GetScreenShot # Required to have screenshot.py

i_hat 			  = vector(1, 0, 0) # creates the i hat direction
j_hat 			  = vector(0, 1, 0) # creates the j hat direction
k_hat 			  = vector(0, 0, 1) # creates the k hat direction

while i_hat.x < 10: 	# while the x-component of i_hat is less than 10, create a series of equally spaced boxes along the x-axis
    x_box 		    = box() # creates a box in the positive i hat direction
    x_box.pos 	    = i_hat
    x_box.color     = color.blue

    neg_x_box 	    = box() # creates a box in the negative i hat direction
    neg_x_box.pos   = -1 * i_hat
    neg_x_box.color = x_box.color

    i_hat.x 	    = i_hat.x + 2 # separates each box by 2 units

while j_hat.y < 10: 	# while the y-component of j_hat is less than 10, create a series of equally spaced boxes along the y-axis
    y_box 		    = box() # creates a box in the positive j hat direction
    y_box.pos  	    = j_hat
    y_box.color     = color.magenta

    neg_y_box 	    = box() # creates a box in the negative j hat direction
    neg_y_box.pos   = -1 * j_hat
    neg_y_box.color = y_box.color

    j_hat.y 	    = j_hat.y + 2 # separates each box by 2 units

while k_hat.z < 10:	    # while the z-componet of k_hat is less than 10, create a series of equally spaced boxes along the z-axis
    z_box 		    = box()
    z_box.pos 	    = k_hat
    z_box.color     = color.green

    neg_z_box 	    = box()
    neg_z_box.pos   = -1 * k_hat
    neg_z_box.color = z_box.color

    k_hat.z 	  = k_hat.z + 2 # separates each box by 2 units

# GetScreenShot(1) # Triggers the GetScreenShot Function

# Note: that the screenshots displayed in the document have been cropped.
