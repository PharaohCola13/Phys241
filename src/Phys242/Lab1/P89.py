#Spencer Riley
from __future__ import division, print_function
from visual import *
from visual.graph import *
#Plots the angle with repsect to time
gdx = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", ytitle="Theta [rads]",
title='Theta vs Time', foreground=color.black, background=color.white)

plot_theta = gcurve(color=color.magenta)

# Plots the energies with respect to time
gdx1 = gdisplay(x=0,y=600, width=1000, height=500, xtitle="Time [s]", ytitle="Energy [J]",
title='Energy vs Time', foreground=color.black, background=color.white)

plot_kinetic = gcurve(color=color.blue)
plot_pot	 = gcurve(color=color.green)
plot_sum	 = gcurve(color=color.red)

label(display=gdx1.display, pos=(1, 0), text="Rotational Kinetic Energy [J]", color=color.blue)
label(display=gdx1.display, pos=(10, 0), text="Spring Potential [J]", color=color.green)
label(display=gdx1.display, pos=(15, 0), text='Sum of Energy [J]', color=color.red)

M = 2 		# mass of uniform-density disk [kg]
R = 0.2		# radius of disk [m]
thick = 0.02	# thickness of disk [m]
I = M*R**2	# moment of inertia of disk [kg*m^2]
r = 0.9*R	# peg in disk at this radius [m]
Lpeg = 5*thick 	# length of peg [m]

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
theta = pi/6 #[rads]

# radians; CCW from x axis
peg.rotate(angle=theta, axis=axle.axis, origin=axle.pos)
rspring = 0.05*R # spring radius[m]

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

t       = 0	#Initial Time
deltat  = 0.001 #Change in time
dtheta  = 0	#Change in angle

ks      = 1.5   # stiffness of each spring
L0      = 0.26  # relaxed length of each spring [m]
L       = vector(0,0,0) # initial angular momentum [kg*m^2]

aor = axle.axis
while t < 20:
	rate(1000)
# Calculate spring force F acting on peg
	d = springF.axis #Displacement vector [m]
	s = (mag(d) - L0) #Stretch [m]
	Fspring = ks * s * norm(d) # Spring force [N]
	Fnet = -2 * Fspring # Net Force [N]
# Calculate torque due to springs [Nm]
	torque = cross(peg.pos, Fnet)
# Update angular momentum [kg*m^2/s]
	L = L + torque * deltat
# Calculate angular velocity omega [rads/s]
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

# Calaculates the energies [J]
	K_rot = 0.5 * I * omega_scalar**2
	U_spring = 2*(0.5 * ks * s**2)
	E_sum = K_rot + U_spring
# Plots the energies with respect to time
	plot_kinetic.plot(pos=(t, K_rot))
	plot_pot.plot(pos=(t, U_spring))
	plot_sum.plot(pos=(t, E_sum))
# This is for the asympotic behavoir of the arctan function
	if peg.pos.x < 0:
		angle = pi + arctan(peg.pos.y/peg.pos.x)
	else:
		angle = arctan(peg.pos.y/peg.pos.x)
# Plots the angle with respect to time
	plot_theta.plot(pos=(t, angle))
# Updates time and angle
	t = t + deltat
	theta = theta + dtheta
