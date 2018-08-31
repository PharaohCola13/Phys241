from __future__ import division, print_function
from visual import *

# 69(a)
# create a cube, of radius 3,with one sphere at each corner

# one             		= sphere()
# one.pos         		= 3 * vector(-1,-1,1)
# one.radius      		= 0.5
# one.color       		= color.red
#
# two             		= sphere()
# two.pos         		= 3 * vector(1,1,1)
# two.radius      		= 0.5
# two.color       		= color.cyan
#
# three           		= sphere()
# three.pos       		= 3 * vector(1, -1, 1)
# three.radius    		= 0.5
# three.color     		= color.green
#
# four            		= sphere()
# four.pos        		= 3 * vector(-1,1, 1)
# four.radius     		= 0.5
# four.color      		= color.blue
#
# five            		= sphere()
# five.pos        		= 3 * vector(-1, -1, -1)
# five.radius     		= 0.5
# five.color      		= color.yellow
#
# six             		= sphere()
# six.pos         		= 3 * vector(1, 1, -1)
# six.radius      		= 0.5
# six.color       		= color.white
#
# seven           		= sphere()
# seven.pos       		= 3 * vector(1, -1, -1)
# seven.radius    		= 0.5
# seven.color     		= color.orange
#
# eight           		= sphere()
# eight.pos       		= 3 * vector(-1, 1, -1)
# eight.radius    		=  0.5
# eight.color     		= color.magenta
#

# 69(b)
# arrow                 = arrow()
# arrow.pos             = one.pos
# arrow.axis            = 2 * six.pos
# arrow.shaftwidth      = 0.2
# arrow.color           = color.cyan



# 70
# Create an x,y,z axis with cylinders of different colors

# The x-axis
# x_axis      		= cylinder()
# x_axis.pos  		= vector(1, 0, 0)
# x_axis.axis 		= 10 * vector(1, 0, 0)
# x_axis.color 		= color.red

# neg_x_axis      	= cylinder()
# neg_x_axis.pos  	= -1 * x_axis.pos
# neg_x_axis.axis 	= -1 * x_axis.axis
# neg_x_axis.color 	= x_axis.color

# The y-axis

# y_axis      		= cylinder()
# y_axis.pos  		= vector(0, 1, 0)
# y_axis.axis 		= 10 * vector(0, 1, 0)
# y_axis.color 		= color.blue
#
# neg_y_axis      	= cylinder()
# neg_y_axis.pos  	= -1 * y_axis.pos
# neg_y_axis.axis 	= -1 * y_axis.axis
# neg_y_axis.color 	= y_axis.color

# The z-axis

# z_axis      		= cylinder()
# z_axis.pos  		= vector(0, 0, -1)
# z_axis.axis 		= 10 * vector(0, 0, 1)
# z_axis.color 		= color.green
#
# neg_z_axis      	= cylinder()
# neg_z_axis.pos  	= -1 * z_axis.pos
# neg_z_axis.axis 	= -1 * z_axis.axis
# neg_z_axis.color 	= z_axis.color

# 73 ***

# box_1             = box()
# box_1.pos         = 10 * vector(1, 0, 0)
# box_1.color       = color.orange
#
# box_2             = box()
# box_2.pos         =
# box_2.color       = color.magenta
#
# arrow             = arrow()
# arrow.pos         = box_1.pos
# arrow.axis        = box_2.pos
# arrow.shaftwidth  = 0.5


# 74
# Use a while loop to produce the sequence 0,4,1,5,2,6,3,7,4,8,5,9,6,10,7,11,8,12,9,13
# Divide the sequence into two starting inputs

# 0,1,2,3,4,5,6,7,8,9
# x = -1 # first input (0-1)
 
# 4,5,6,7,8,9,10,11,12,13
# y = 3 # second input (4-1)
#
# while y < 13: # y is the largest number, and thus will act as the limiting variable 
#     x = x + 1 # adds one to the first input
#     y = y + 1 # adds one to the second input
#
#     print(x)
#     print(y)

# 75

# i_hat 			= vector(1, 0, 0) # creates the i hat direction
# j_hat 			= vector(0, 1, 0) # creates the j hat direction
# k_hat 			= vector(0, 0, 1) # creates the k hat direction
#
# while i_hat.x < 10: 	# while the x-component of i_hat is less than 10, create a series of equally spaced boxes along the x-axis
#     x_box 		= box() # creates a box in the positive i hat direction
#     x_box.pos 	= i_hat
#
#     neg_x_box 	= box() # creates a box in the negative i hat direction
#     neg_x_box.pos = -1 * i_hat
#
#     i_hat.x 		= i_hat.x + 2 # separates each box by 2 units
#
# while j_hat.y < 10: 	# while the y-componet of j_hat is less than 10, create a series of equally spaced boxes along the y-axis
#     y_box 		= box() # creates a box in the positive j hat direction
#     y_box.pos 	= j_hat
#
#     neg_y_box 	= box() # creates a box in the negative j hat direction
#     neg_y_box.pos = -1 * j_hat
#
#     j_hat.y 		= j_hat.y + 2 # separates each box by 2 units
#
# while k_hat.z < 10:	# while the z-componet of k_hat is less than 10, create a series of equally spaced boxes along the z-axis
#     z_box 		= box() 
#     z_box.pos 	= k_hat
#
#     neg_z_box 	= box()
#     neg_z_box.pos = -1 * k_hat
#
#     k_hat.z 		= k_hat.z + 2 # separates each box by 2 units


hat = vector(1,1,1)
i_hat = vector(hat.x, 0, 0)
j_hat = vector(0, hat.y, 0)
k_hat = vector(0, 0, hat.z)



while mag(hat) < 100:
    x_box = box()
    x_box.pos = i_hat
#
    neg_x_box = box()
    neg_x_box.pos = -1 * i_hat

    hat.x = hat.x + 2

    y_box = box()
    y_box.pos = j_hat

    neg_y_box = box()
    neg_y_box.pos = -1 * j_hat

    hat.y = hat.y + 2

    z_box = box()
    z_box.pos = k_hat

    neg_z_box = box()
    neg_z_box.pos = -1 * k_hat

    hat.z = hat.z + 2
