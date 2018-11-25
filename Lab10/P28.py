# Spencer Riley
# Code copied from the book verbatim cause the question told me too
from __future__ import division, print_function
from visual import *
from visual.graph import *
from random import random

gg = gcurve(color=color.yellow)

n = 0
while n < 20:
	rate(10)
	a = random()

	print(a)

	gg.plot(pos=(n, a))
	n = n + 1
