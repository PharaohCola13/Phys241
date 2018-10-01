from __future__ import division, print_function
from visual import *
from visual.graph import *

# Creates the graphical display for position
gd1 = gdisplay(x=550,y=0,width=700,height=500,
			   title='Position of ball1 and ball2',
			   xtitle='Time [s]',
			   ytitle='Position [m]')

gd2 = gdisplay(x=1100,y=0,width=700,height=500,
			   title='Momentum of ball1 and ball2',
			   xtitle='Time [s]',
			   ytitle='Momentum [kg m/s]')


k   = 50 # in N/m
L0  = 14 # in m

wall1                = box()
wall1.pos            = vector(2 *L0, 0, 0)
wall1.size           = vector(0.1, L0, L0)
wall1.color          = color.yellow

wall2               = box()
wall2.pos            = vector(-2 *L0, 0, 0)
wall2.size           = vector(0.1, L0, L0)
wall2.color          = color.yellow

ball1                = sphere()
#ball1.pos            = vector(L0/2,0,0)
ball1.pos 	     	 = vector(L0/2, L0/2, 0)
ball1.radius         = 2
ball1.m              = 3
ball1.p              = ball1.m *vector(0, -10, 0)
ball1.color          = color.orange

ball2                = sphere()
#ball2.pos            = vector(-L0/2,0,0)
ball2.pos	    	 = vector(-L0/2, -L0/2, 0)
ball2.radius         = 2
ball2.m              = 3
#ball2.p 			 = ball2.m *vector(0, 0, 0)
ball2.p              = ball2.m *vector(0,10,0)
ball2.color          = color.green

spring1              = helix()
spring1.pos          = wall1.pos
spring1.axis         = ball1.pos - wall1.pos
spring1.thickness    = 0.3
spring1.radius       = 1
spring1.coils        = 10
spring1.color        = color.orange

spring2              = helix()
spring2.pos          = ball2.pos
spring2.axis         = ball1.pos - ball2.pos
spring2.thickness    = 0.3
spring2.radius       = 1
spring2.coils        = 10
spring2.color        = color.cyan

spring3              = helix()
spring3.pos          = wall2.pos
spring3.axis         = ball2.pos - wall2.pos
spring3.thickness    = 0.3
spring3.radius       = 1
spring3.coils        = 10
spring3.color        = color.magenta

t   = 0
dt  = 0.01

f1 = gcurve(gdisplay = gd1) # Define functions to plot
f2 = gcurve(gdisplay = gd2) # Define functions to plot


while True:
	rate(100)
	
	s           = L0 - mag(ball1.pos)
	Fspring 	 = -k * s * norm(ball1.pos)
	#Fspring     = -k * s * vector(0,0,1)
	Fnet        = Fspring

	print(norm(ball1.pos))

	s2           = L0 - mag(ball2.pos)
	Fspring2 	 = k * s2 * norm(ball2.pos)
	#Fspring2     = k * s2 * vector(0, 0, 1)
	Fnet2        = Fspring2


	ball1.p     = ball1.p + Fnet*dt
	ball1.pos   = ball1.pos + ball1.p/ball1.m * dt

	ball2.p     = ball2.p + Fnet2*dt
	ball2.pos   = ball2.pos + ball2.p/ball2.m * dt


	spring1.axis = ball1.pos - wall1.pos
	spring2.pos  = ball2.pos
	spring2.axis = ball1.pos - ball2.pos
	spring3.axis = ball2.pos - wall2.pos

	f1.plot(pos=(t, ball1.pos.y), color=ball1.color)  # Plots position vs time
	f1.plot(pos=(t, ball2.pos.y), color=ball2.color)  # Plots position vs time
	f2.plot(pos=(t, ball1.p.x), color=ball1.color)  # Plots position vs time
	f2.plot(pos=(t, ball2.p.x), color=ball2.color)  # Plots position vs time

	t = t + dt
