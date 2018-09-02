# Spencer Riley (***In Development***)
from __future__ import division, print_function
from visual import *
from commands import*

lab = input('What is the lab number?\n>> ')
question = input('What question is this?\n>> ')

w_default = 500 # sets default value of width to 500
# width = input('What should the scene width be?\n>> ')
#
# if width == "n/a":
#     scene.width = w_default
# else:
#     print(width)
#
h_default = 500
# height = input('What should the scene height be?\n>> ')
#
# if height == "n/a":
#     scene.height = h_default
# else:
#     print(height)

# Used to get a screenshot
def GetScreenShot(FrameNumber):
    # Uses gnome-screenshot to take screenshot
    tmp          = getoutput('/usr/bin/gnome-screenshot')

    # moves it from default directory to Lab
    tmp          = getoutput('mv ~/Pictures/Screenshot*.png'
                             ' ~/PycharmProjects/Physics/Lab{}/Figures/P{}.png'
                             .format(lab, question))

scene.height = h_default
print(scene.height)

scene.width = w_default
print(scene.width)
