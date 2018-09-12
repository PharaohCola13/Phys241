from __future__ import division, print_function
from visual import *

s_plane = -1000 # km/hr
d       = -1500 # km
t       = 1.67 # hr
theta   = degrees(15)

s_net = d/t # Actual speed of plane

d_plane         = arrow()
d_plane.pos     = vector(0,0,0)
d_plane.axis    = vector((s_plane * t) * cos(theta), (s_plane * t) * cos(degrees(90) - theta))
d_plane.color   = color.red

v_plane         = vector(d_plane.axis.x / t, d_plane.axis.y / t)

#
d_net           = arrow()
d_net.pos       = vector(0,0,0)
d_net.axis      = vector(0, d)
d_net.color     = color.orange

v_net           = vector(d_net.axis.x / t, d / t)

#
s_wind          = (sin(theta) * s_plane)
d_wind          = arrow()
d_wind.pos      = d_plane.axis
d_wind.axis     = vector((s_wind * t), (s_wind * t) * tan(theta))

#v_wind          = vector(d_wind.axis.x / t, d_wind.axis.y / t)
v_wind          = v_plane - v_net

# = vector(258.82, 258.82 * tan(90-theta))
#v_wind = v_net - v_plane

print(v_plane)
print(v_net)
print(v_wind)

#print(d_plane.axis)
#print(d_net.axis)
#print(d_wind.axis)