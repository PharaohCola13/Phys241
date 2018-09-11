from __future__ import division, print_function
from visual import *

b = 1.5 # constant defined in the problem

c = 0.64 # Other constant defined by the problem

# Part 1

# Position function provided by the problem.
# r = bt + ct^3

avg_velocity_a = (((b * 3) + (c * 3**3)) - ((b * 1) + (c * 1**3)))/(3 - 1) # Average velocity for the time interval of [1,3]
avg_velocity_b = (((b * 2.5) + (c * 2.5**3)) - ((b * 1.5) + (c * 1.5**3)))/(2.5 - 1.5) # Average velocity for the time interval of [1.5, 2.5]
avg_velocity_c = (((b * 2.05) + (c * 2.05**3)) - ((b * 1.95) + (c * 1.95**3)))/(2.05 - 1.95) # Average velocity for the time interval [1.95, 2.05]

print("The average velocity on the interval [1,3] is {}.".format(avg_velocity_a))
print("The average velocity on the interval [1.5, 2.5] is {}".format(avg_velocity_b))
print("The average velocity on the interval [1.95, 2.05] is {}".format(avg_velocity_c))

# Part 2

# Derivative of the position function
# v = b + 2t^2

instant_velocity = b + (3 * c * 2**2) # instantaneous velocity function

print("The instantaneous velocity is {}".format(instant_velocity))

# Part 3

absol_error_a = avg_velocity_a - instant_velocity # absolute error for the time interval [1,3]
absol_error_b = avg_velocity_b - instant_velocity # absolute error for the time interval [1.5,2.5]
absol_error_c = avg_velocity_c - instant_velocity # absolute error for the time interval [1.95,2.05]

print("The absolute error for the interval [1,3] is {}".format(absol_error_a))
print("The absolute error for the interval [1.5,2.5] is {}".format(absol_error_b))
print("The absolute error for the interval [1.95,2.05] is {}".format(absol_error_c))

# Part 4

relative_error_a = absol_error_a / instant_velocity # relative error for the time interval [1,3]
relative_error_b = absol_error_b / instant_velocity # relative error for the time interval [1.5,2.5]
relative_error_c = absol_error_c / instant_velocity # relative error for the time interval [1.95,2.05]

print("The relative error for the interval [1,3] is {}".format(relative_error_a))
print("The relative error for the interval [1.5,2.5] is {}".format(relative_error_b))
print("The relative error for the interval [1.95,2.05] is {}".format(relative_error_c))
