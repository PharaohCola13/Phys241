# Spencer Riley

from __future__ import division, print_function
from visual import *
#from screenshot import GetScreenShot # Required to have screenshot.py

theta = 0 # Initial definition of theta

# Equation of a circle -> r*sin(theta) + r*cos(theta)

ij_hat  = vector(cos(theta), sin(theta), 0) # Defines a unit circle on the xy-plane
jk_hat  = vector(0, cos(theta), sin(theta)) # Defines a unit circle on the yz-plane
ik_hat  = vector(cos(theta), 0, sin(theta)) # Defines a unit circle on the zy-plane

while theta < 6:
# Local Definitions of the components from ij_hat
    ij_hat.x = cos(theta)
    ij_hat.y = sin(theta)
    ij_hat.z = 0

# Local Definitions of the components from jk_hat
    jk_hat.x = 0
    jk_hat.y = cos(theta)
    jk_hat.z = sin(theta)

# Local Definitions of the components from ik_hat
    ik_hat.x = cos(theta)
    ik_hat.y = 0
    ik_hat.z = sin(theta)

# Produces the xy-plane ring of spheres
    xy_ball         = sphere()
    xy_ball.pos     = 7 * ij_hat
    xy_ball.color   = color.red

# Produces the yx-plane ring of spheres
    yz_ball          = sphere()
    yz_ball.pos      = 7 * jk_hat
    yz_ball.color    = color.blue

# Produces the xz-plane ring of spheres
    xz_ball          = sphere()
    xz_ball.pos      = 7 * ik_hat
    xz_ball.color    = color.orange

    theta = theta + pi / 10 # Every pi/10 adds a new sphere

# GetScreenShot(1) # Triggers the GetScreenShot Function

# Note: that the screenshots displayed in the document have been cropped.
