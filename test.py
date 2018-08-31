from __future__ import division, print_function
from visual import *

# 69

# one             = sphere()
# one.pos         = 3 * vector(-1,-1,1)
# one.radius      = 0.5
# one.color       = color.red
#
# two             = sphere()
# two.pos         = 3 * vector(1,1,1)
# two.radius      = 0.5
# two.color       = color.cyan
#
# three           = sphere()
# three.pos       = 3 * vector(1, -1, 1)
# three.radius    = 0.5
# three.color     = color.green
#
# four            = sphere()
# four.pos        = 3 * vector(-1,1, 1)
# four.radius     = 0.5
# four.color      = color.blue
#
# five            = sphere()
# five.pos        = 3 * vector(-1, -1, -1)
# five.radius     = 0.5
# five.color      = color.yellow
#
# six             = sphere()
# six.pos         = 3 * vector(1, 1, -1)
# six.radius      = 0.5
# six.color       = color.white
#
# seven           = sphere()
# seven.pos       = 3 * vector(1, -1, -1)
# seven.radius    = 0.5
# seven.color     = color.orange
#
# eight           = sphere()
# eight.pos       = 3 * vector(-1, 1, -1)
# eight.radius    =  0.5
# eight.color     = color.magenta
#
# arrow                 = arrow()
# arrow.pos             = one.pos
# arrow.axis            = 2 * six.pos
# arrow.shaftwidth      = 0.2
# arrow.color           = color.cyan

# 70
#
# x_axis      = cylinder()
# x_axis.pos  = vector(1,0,0)
# x_axis.axis = 10 * vector(1, 0, 0)
# x_axis.color = color.red
#
# neg_x_axis      = cylinder()
# neg_x_axis.pos  = -1 * vector(1,0,0)
# neg_x_axis.axis = -10 * vector(1, 0, 0)
# neg_x_axis.color = color.red
#
# y_axis      = cylinder()
# y_axis.pos  = vector(0,1, 0)
# y_axis.axis = 10 * vector(0, 1, 0)
# y_axis.color = color.blue
#
# neg_y_axis      = cylinder()
# neg_y_axis.pos  = -1  * vector(0,1,0)
# neg_y_axis.axis = -10 * vector(0, 1, 0)
# neg_y_axis.color = color.blue
#
# z_axis      = cylinder()
# z_axis.pos  = vector(0, 0, -1)
# z_axis.axis = 10 * vector(0, 0, 1)
# z_axis.color = color.green
#
# neg_z_axis      = cylinder()
# neg_z_axis.pos  = -1  * vector(0,0,1)
# neg_z_axis.axis = -10 * vector(0, 0, 1)
# neg_z_axis.color = color.green

# 73 ***

# box_1 = box()
# box_1.pos = 10 * vector(1, 0, 0)
# box_1.color = color.orange
#
# box_2 = box()
# box_2.pos =
# box_2.color  = color.magenta
#
# arrow = arrow()
# arrow.pos = box_1.pos
# arrow.axis = box_2.pos
# arrow.shaftwidth = 0.5


# 74

# x = -1
# y = 3
#
# while y < 13 :
#     x = x + 1
#     y = y + 1
#
#     print(x)
#     print(y)

# 75

# i_hat = vector(1, 0, 0)
# j_hat = vector(0, 1, 0)
# k_hat = vector(0, 0, 1)
#
# while i_hat.x < 10:
#     x_box = box()
#     x_box.pos = i_hat
#
#     neg_x_box = box()
#     neg_x_box.pos = -1 * i_hat
#
#     i_hat.x = i_hat.x + 2
#
# while j_hat.y < 10:
#     y_box = box()
#     y_box.pos = j_hat
#
#     neg_y_box = box()
#     neg_y_box.pos = -1 * j_hat
#
#     j_hat.y = j_hat.y + 2
#
# while k_hat.z < 10:
#     z_box = box()
#     z_box.pos = k_hat
#
#     neg_z_box = box()
#     neg_z_box.pos = -1 * k_hat
#
#     k_hat.z = k_hat.z + 2


hat = vector(1,1,1)
i_hat = vector(hat.x, 0, 0)
j_hat = vector(0, hat.y, 0)
k_hat = vector(0, 0, hat.z)



while mag(hat) < 100:
    x_box = box()
    x_box.pos = i_hat
#
    neg_x_box = box()
    neg_x_box.pos = -1 * i_hat

    hat.x = hat.x + 2

    y_box = box()
    y_box.pos = j_hat

    neg_y_box = box()
    neg_y_box.pos = -1 * j_hat

    hat.y = hat.y + 2

    z_box = box()
    z_box.pos = k_hat

    neg_z_box = box()
    neg_z_box.pos = -1 * k_hat

    hat.z = hat.z + 2