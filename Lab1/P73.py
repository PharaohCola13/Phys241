# Spencer Riley

from __future__ import division, print_function
from visual import *
from screenshot import GetScreenShot # Required to have screenshot.py


# This creates a two boxes linked by an arrow

box_1             = box()
box_1.pos         = 2 * vector(1, 0, 0)
box_1.color       = color.orange

box_2             = box()
box_2.pos         = -2 * box_1.pos
box_2.color       = color.magenta

arrow             = arrow()
arrow.pos         = box_1.pos
arrow.axis        = 2 * box_2.pos
arrow.shaftwidth  = 0.5

GetScreenShot(1) # Triggers the GetScreenShot Function

# Note: that the screenshots displayed in the document have been cropped.