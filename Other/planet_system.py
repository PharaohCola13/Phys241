from __future__ import division, print_function
from visual import *

def canvas(scene):  # return canvas bounding box, excluding frames
    bar, d = 30, 8  # title bar and frame thickness for Windows
    return (int(scene.x+d), int(scene.y+bar),
            int(scene.width-d), int(scene.height-d))

G       = 6.7e-11 # Nm^2/kg^2
YinS    = 365.*24.*60.*60 # s
AU      = 1.5e11 # m
def color():
    spaghetti = vector(1,0.267, 0)
    return spfhetti
# star_out            = sphere()
# star_out.pos        = vector(0,0,0)
# star_out.radius     = 56378.15
# star_out.m          = 1.989E30
# star_out.color      = color.orange
# star_out.opacity    = 0.8

# X-axis
# x_axis          = arrow()
# x_axis.pos      = vector(0,0,0)
# x_axis.axis     = 1 * vector(1, 0, 0)
# x_axis.color    = color.red
#
# # Y-axis
# y_axis          = arrow()
# y_axis.pos      = vector(0,0,0)
# y_axis.axis     = 1 * vector(0, 1, 0)
# y_axis.color    = color.blue
#
# # Z-axis
# z_axis          = arrow()
# z_axis.pos      = vector(0,0,0)
# z_axis.axis     = 1  * vector(0, 0, 1)
# z_axis.color    = color.green


star_in             = sphere()
star_in.pos         = vector(0,0,0)
star_in.radius      = 0.1
star_in.m           = 2e30
star_in.color       = spaghetti
star_in.opacity     = 1
star_in.materials   = materials.emissive 

planet_one          = sphere(make_trail=True)
planet_one.pos      = vector(1, 0, 0)
planet_one.radius   = 0.05
planet_one.color    = color.cyan
planet_one.m        = 6e24
planet_on.materials = materials.BlueMarble

planet_one_ring             = ring()
planet_one_ring.pos         = planet_one.pos
planet_one_ring.axis        = vector(1, 1, 0)
planet_one_ring.radius      = 0.1
planet_one_ring.thickness   = 0.01
planet_one_ring.color       = color.green

planet_two          = sphere()
planet_two.pos      = vector(0.5, 0.6, 0)
planet_two.radius   = 0.1
planet_two.color    = color.white
planet_two.m        = 1e15
planet_two.materials = materials.blazed

star_in.v0          = vector(0,0,0)
planet_one.v0       = vector(0, (2 * pi * AU)/YinS, 0)
planet_one_ring.v0  = planet_one.v0

planet_two.v0       = vector(0, (2 * pi * AU)/YinS, 0)

star_in.p           = star_in.m * star_in.v0
planet_one.p        = planet_one.m * planet_one.v0
planet_one_ring.p   = planet_one.p

planet_two.p    = planet_two.m * planet_two.v0

t = 0
dt = YinS/1000
#dt = 1

while (planet_two.pos - star_in.pos) >= 1 :
    rate(100)

#     r_one = (planet_one.pos - star_in.pos) * AU
#     r_one_mag  = mag(r_one)
#     r_one_hat = norm(r_one)

    r_two = (planet_two.pos - star_in.pos)*AU
    r_two_mag = mag(r_two)
    r_two_hat = norm(r_two)

#     F_one_mag = G*(star_in.m * planet_one.m)/r_one_mag**2
#     F_one_net = -F_one_mag * r_one_hat

    F_two_mag = G*(star_in.m * planet_two.m)/r_two_mag**2
    F_two_net = -F_two_mag * r_two_hat

#     planet_one.p = planet_one.p + F_one_net * dt
#     planet_one_ring.p = planet_one.p

    planet_two.p = planet_two.p + F_two_net * dt

#     planet_one.pos = planet_one.pos + (planet_one.p/planet_one.m/AU) * dt
#     planet_one_ring.pos = planet_one.pos

    #planet_two.pos = planet_two.pos + (planet_two.p/planet_two.m/AU) * dt
    planet_two.m = planet_two.m + 1e20
    planet_two.pos = planet_one.pos
    planet_two.radius = planet_two.radius + 1e-10
    #print(planet_two.m)

    r_sun = (star_in.pos - planet_two.pos) * AU
    r_sun_mag = mag(r_sun)
    r_sun_hat = norm(r_sun)

    F_sun_mag = G * (star_in.m * planet_two.m) / r_sun_mag**2
    F_sun_net = -F_sun_mag * r_sun_hat

    star_in.p = star_in.p + F_sun_net * dt
    
    if r_two_mag < star_in.radius:
        star_in.color = color.black
        planet_two.color = color.black
        display(center=star_in.pos,background=(1,1,1))
        break
        
    
    star_in.pos = star_in.pos + (star_in.p/star_in.m/AU) * dt
    #print(planet_two.m)
    t= t + dt
