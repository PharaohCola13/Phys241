from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for position
gd1 = gdisplay(x=550,y=0,width=700,height=500,
			   title='Position of ball1',
			   xtitle='Time [s]',
			   ytitle='Position [m]')


k   = 50 # in N/m
L0  = 14 # in m

wall1                = box()
wall1.pos            = vector(2 *L0, 0, 0)
wall1.size           = vector(0.1, 5, 5)
wall1.color          = color.green

wall2               = box()
wall2.pos            = vector(-2 *L0, 0, 0)
wall2.size           = vector(0.1, 5, 5)
wall2.color          = color.green

ball1                = sphere()
#ball1.pos            = vector(L0/2,0,0)
ball1.pos 			 = vector(L0/2, 0, -L0/2)
ball1.radius         = 2
ball1.m              = 3
ball1.p              = ball1.m *vector(0, 0,0)
ball1.color          = color.red

ball2                = sphere()
#ball2.pos            = vector(-L0/2,0,0)
ball2.pos		     = vector(-L0/2, 0, L0/2)
ball2.radius         = 2
ball2.m              = 3
ball2.p              = ball1.m *vector(0,0,0)
ball2.color          = color.orange

spring1              = helix()
spring1.pos          = wall1.pos
spring1.axis         = ball1.pos - wall1.pos
spring1.thickness    = 0.3
spring1.radius       = 1
spring1.coils        = 10
spring1.color        = color.blue

spring2              = helix()
spring2.pos          = ball2.pos
spring2.axis         = ball1.pos - ball2.pos
spring2.thickness    = 0.3
spring2.radius       = 1
spring2.coils        = 10
spring2.color        = color.blue

spring3              = helix()
spring3.pos          = wall2.pos
spring3.axis         = ball2.pos - wall2.pos
spring3.thickness    = 0.3
spring3.radius       = 1
spring3.coils        = 10
spring3.color        = color.blue

t   = 0
dt  = 0.001

f1 = gcurve(gdisplay = gd1, color=color.white) # Define functions to plot


while True:
	rate(100)

	s           = L0 - mag(ball1.pos)
	#Fspring 	 = -k * s * norm(ball1.pos)
	Fspring     = -k * s * vector(0,0,1)
	Fnet        = Fspring

	s2           = L0 - mag(ball2.pos)
	#Fspring 	 = k * s2 * norm(ball2.pos)
	Fspring2     = k * s2 * vector(0, 0, 1)
	Fnet2        = Fspring2


	ball1.p     = ball1.p + Fnet*dt
	ball1.pos   = ball1.pos + ball1.p/ball1.m * dt

	ball2.p     = ball2.p + Fnet2*dt
	ball2.pos   = ball2.pos + ball2.p/ball2.m * dt


	spring1.axis = ball1.pos - wall1.pos
	spring2.pos  = ball2.pos
	spring2.axis = ball1.pos - ball2.pos
	spring3.axis = ball2.pos - wall2.pos

	f1.plot(pos=(t, ball1.pos.z))  # Plots position vs time

	t = t + dt