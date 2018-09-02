from __future__ import division, print_function
from visual import *

# 74
# Use a while loop to produce the sequence 0,4,1,5,2,6,3,7,4,8,5,9,6,10,7,11,8,12,9,13
# Divide the sequence into two starting inputs

# 0,1,2,3,4,5,6,7,8,9
x = -1 # first input (0-1)

# 4,5,6,7,8,9,10,11,12,13
y = 3 # second input (4-1)

while y < 13: # y is the largest number, and thus will act as the limiting variable
    x = x + 1 # adds one to the first input
    y = y + 1 # adds one to the second input

    print(x)
    print(y)
