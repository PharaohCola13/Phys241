from __future__ import division, print_function
from visual import *
from visual.graph import *
#from visual.materials import  *

from random import random

gg = gcurve(color=color.yellow)

n = 0
while n < 20:
	rate(10)
	a = random()

	print(a)

	gg.plot(pos=(n, a))
	n = n + 1

# Part A) They are not the same plots
# Part A) n -> energy state; a ->
# Part B) Max value of random() is 1.0
# Part C) Min value of random(0 is 0.0

