from __future__ import division, print_function
from visual import *
from visual.graph import *

M = 2
# mass of uniform-density disk
R = 0.2
# radius of disk
thick = 0.02
# thickness of disk
I = M*R**2
# moment of inertia of disk
r = 0.9*R
# peg in disk at this radius
Lpeg = 5*thick # length of peg


wall        = box()
wall.pos    = vector(-1.2*R,0,0)
wall.size   = (0.01,2.4*R,0.8*R)
wall.color  = color.green
# Center of disk is at <0,0,0>:

disk            = cylinder()
disk.pos        = vector(0,0,-thick/2)
disk.radius     = R
disk.axis       = vector(0,0,thick)
disk.color      = color.white
disk.opacity    = 0.7
disk.material   = materials.rough

axle        = cylinder()
axle.pos    = vector(0,0,-Lpeg/2)
axle.radius = 0.05*R
axle.color  = color.red
axle.axis   = vector(0,0,Lpeg)
# Place peg in the disk on x axis:
peg         = cylinder()
peg.pos     = (r,0,-Lpeg/2)
peg.radius  = 0.03*R
peg.color   = color.red
peg.axis    = vector(0,0,Lpeg)

# Rotate to initial position:
theta = pi/6
# radians; CCW from x axis
peg.rotate(angle=theta, axis=axle.axis, origin=axle.pos)
rspring = 0.05*R # spring radius
# Front spring:
springF             = helix()
springF.pos         = (wall.x,r,1.5*thick)
springF.radius      = 0.05*R
springF.color       = color.orange
springF.coils       = 15
springF.thickness   = 0.4*rspring
# Back spring:
springB             = helix()
springB.pos         = (wall.x,r,-1.5*thick)
springB.radius      = 0.05*R
springB.color       = color.orange
springB.coils       = 15
springB.thickness   = 0.4*rspring
# Attach springs to peg:
end = peg.pos+vector(0, 0, Lpeg/2+springF.pos.z)

springB.axis = springF.axis = end - springF.pos

t       = 0
deltat  = 0.01
dtheta  = 0
ks      = 1.5   # stiffness of each spring
L0      = 0.26  # relaxed length of each spring
L       = vector(0,0,0) # initial angular momentum

while True:
	rate(100)
# Calculate spring force F acting on peg
	s = 1
	Fspring = ks * s
# Calculate torque due to springs
# Update angular momentum L
# Calculate angular velocity omega
# Calculate dtheta and theta
# Update disk and peg positions:
	disk.rotate(angle=dtheta, axis=axle.axis,origin=axle.pos)
	peg.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)
# Update spring lengths:
	end = peg.pos+vector(0,0,Lpeg/2+springF.pos.z)
	springF.axis = end - springF.pos
	springB.axis = springF.axis

	t = t + deltat