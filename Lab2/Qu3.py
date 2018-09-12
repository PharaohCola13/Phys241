from __future__ import division, print_function
from visual import *

s_plane = -1000 # km/hr
d       = -1500 # km
t       = 1.67 # hr
theta   = radians(15) # in degrees

s_net = d/t # Actual speed of plane

# Direction of the plane
d_plane         = arrow()
d_plane.pos     = vector(0,0,0)
d_plane.axis    = vector((s_plane * t) * cos(theta), (s_plane * t) * cos(theta))
d_plane.color   = color.red

v_plane         = vector(s_plane * sin(theta) , ((s_plane * t) * cos(theta)) / t) # Velocity of the plane

# Direction of the net direction of the plane
d_net           = arrow()
d_net.pos       = vector(0,0,0)
d_net.axis      = vector(0, d)
d_net.color     = color.orange

v_net           = vector(d_net.axis.x / t, d / t) # Net velocity

# Direction of the wind
s_wind          = (sin(theta) * s_plane) # Speed of the wind
d_wind          = arrow()
d_wind.pos      = d_net.axis
d_wind.axis     = vector((s_wind * t), (s_wind * t) * tan(theta))

#v_wind          = vector(d_wind.axis.x / t, d_wind.axis.y / t)
v_wind          = v_net - v_plane

print("The Velocity of the wind is {} km/hr".format(v_wind))

