from __future__ import division, print_function
from visual import *
from screenshot import GetScreenShot # Required to have screenshot.py


# Vector A, given in the problem
A       = arrow()
A.pos   = vector(0, 0, 0)
A.axis  = vector(5, 2, -1)
A.color = color.cyan

# Vector B, given in the problem
B       = arrow()
B.pos   = vector(0,0,0)
B.axis  = vector(3, 7, 3)
B.color = color.red

# positive x direction # Used for visual
i_hat       = arrow()
i_hat.pos   = vector(0,0,0)
i_hat.axis  = 10 * vector(1,0,0)
i_hat.color = color.orange

# positive y direction # Used for visual
j_hat       = arrow()
j_hat.pos   = vector(0,0,0)
j_hat.axis  = 10 * vector(0,1,0)
j_hat.color = color.white

# positive z direction
k_hat       = arrow()
k_hat.pos   = vector(0,0,0)
k_hat.axis  = 10 * vector(0,0,1)
k_hat.color = color.green


# Vector pointing from A to B
C = B.axis - A.axis

# The distance required to travel from A to B
mag_C = mag(C)

# Dot product between the vector C and the individual unit vectors
dot_x = dot(C, i_hat.axis)
dot_y = dot(C, j_hat.axis)
dot_z = dot(C, k_hat.axis)

# Method to solve for the cos(theta) for each of the axes
cos_theta_x = dot_x / (mag(C) * mag(i_hat.axis))
cos_theta_y = dot_y / (mag(C) * mag(j_hat.axis))
cos_theta_z = dot_z / (mag(C) * mag(k_hat.axis))

# The values of theta with respect to each of the axes
theta_x = degrees(arccos(cos_theta_x))
theta_y = degrees(arccos(cos_theta_y))
theta_z = degrees(arccos(cos_theta_z))

GetScreenShot(1)

# Prints
print("The distance need to travel is {}".format(mag_C))
print("The value of theta with respect to the x axis is {}".format(theta_x))
print("The value of theta with respect to the y axis is {}".format(theta_y))
print("The value of theta with respect to the z axis is {}".format(theta_z))