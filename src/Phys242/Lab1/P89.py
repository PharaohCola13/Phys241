from __future__ import division, print_function
from visual import *
from visual.graph import *

gdx = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", ytitle="Theta [rads]",
title='Theta vs Time')

plot_theta = gcurve(color=color.magenta)

gdx1 = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", ytitle="Energy [J]",
title='Energy vs Time')

plot_kinetic = gcurve(color=color.cyan)
plot_pot	 = gcurve(color=color.yellow)
plot_sum	 = gcurve(color=color.red)

label(display=gdx1.display, pos=(1, 0), text="Rotational Kinetic Energy [J]", color=color.cyan)
label(display=gdx1.display, pos=(10, 0), text="Spring Potential [J]", color=color.yellow)
label(display=gdx1.display, pos=(15, 0), text='Sum of Energy [J]', color=color.red)

M = 2 			# mass of uniform-density disk
R = 0.2			# radius of disk
thick = 0.02	# thickness of disk
I = M*R**2		# moment of inertia of disk
r = 0.9*R		# peg in disk at this radius
Lpeg = 5*thick 	# length of peg

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
deltat  = 0.001
dtheta  = 0

ks      = 1.5   # stiffness of each spring
L0      = 0.26  # relaxed length of each spring
L       = vector(0,0,0) # initial angular momentum

aor = axle.axis
while t < 20:
	rate(1000)
# Calculate spring force F acting on peg
	d = springF.axis
	s = (mag(d) - L0)
	Fspring = ks * s * norm(d)
	Fnet = -2 * Fspring
# Calculate torque due to springs
	torque = cross(peg.pos, Fnet)
# Update angular momentum L
	L = L + torque * deltat
# Calculate angular velocity omega
	omega = L/I
	omega_scalar = dot(omega, norm(aor))
# Calculate dtheta and theta
	dtheta = omega_scalar * deltat
# Update disk and peg positions:
	disk.rotate(angle=dtheta, axis=axle.axis,origin=axle.pos)
	peg.rotate(angle=dtheta, axis=axle.axis, origin=axle.pos)
# Update spring lengths:
	end = peg.pos+vector(0,0,Lpeg/2+springF.pos.z)

	springF.axis = end - springF.pos

	springB.axis = springF.axis

	K_rot = 0.5 * I * omega_scalar**2
	U_spring = 2*(0.5 * ks * s**2)
	E_sum = K_rot + U_spring

	plot_kinetic.plot(pos=(t, K_rot))
	plot_pot.plot(pos=(t, U_spring))
	plot_sum.plot(pos=(t, E_sum))

	if peg.pos.x < 0:
		angle = pi + arctan(peg.pos.y/peg.pos.x)
	else:
		angle = arctan(peg.pos.y/peg.pos.x)
	plot_theta.plot(pos=(t, angle))

	t = t + deltat
	theta = theta + dtheta
