from __future__ import division, print_function
from visual import *

b = 1.5
c = 0.64

# Part 1

avg_velocity_a = (((b * 3) + (c * 3**3)) - ((b * 1) + (c * 1**3)))/(3 - 1)

avg_velocity_b = (((b * 2.5) + (c * 2.5**3)) - ((b * 1.5) + (c * 1.5**3)))/(2.5 - 1.5)

avg_velocity_c = (((b * 2.05) + (c * 2.05**3)) - ((b * 1.95) + (c * 1.95**3)))/(2.05 - 1.95)

print("The average velocity on the interval [1,3] is {}.".format(avg_velocity_a))
print("The average velocity on the interval [1.5, 2.5] is {}".format(avg_velocity_b))
print("The average velocity on the interval [1.95, 2.05] is {}".format(avg_velocity_c))

# Part 2

instant_velocity = b + (3 * c * 2**2)

print("The instantaneous velocity is {}".format(instant_velocity))

# Part 3

absol_error_a = avg_velocity_a - instant_velocity

absol_error_b = avg_velocity_b - instant_velocity

absol_error_c = avg_velocity_c - instant_velocity

print("The absolute error for the interval [1,3] is {}".format(absol_error_a))
print("The absolute error for the interval [1.5,2.5] is {}".format(absol_error_b))
print("The absolute error for the interval [1.95,2.05] is {}".format(absol_error_c))

# Part 4

relative_error_a = absol_error_a / instant_velocity
relative_error_b = absol_error_b / instant_velocity
relative_error_c = absol_error_c / instant_velocity

print("The relative error for the interval [1,3] is {}".format(relative_error_a))
print("The relative error for the interval [1.5,2.5] is {}".format(relative_error_b))
print("The relative error for the interval [1.95,2.05] is {}".format(relative_error_c))
