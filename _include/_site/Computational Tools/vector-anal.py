# Spencer Riley

from __future__ import division, print_function
from visual import *
import random

run = input('Run? (0) Yes, (1) No.\n>> ')

while run == 0:

    option = input('(0) Cross Product, (1) Dot Product\n>> ')


    if option == 0:
        print('----- First Vector -----')
        u_x = input('What is the first component of the first vector?\n>> ')
        u_y = input('What is the second component of the first vector?\n>> ')
        u_z = input('What is the third component of the first vector?\n>> ')

        print('----- Second Vector -----')

        v_x = input('What is the first component of the second vector?\n>> ')
        v_y = input('What is the second component of the second vector?\n>> ')
        v_z = input('What is the third component of the second vector?\n>> ')

        u = vector(u_x, u_y, u_z)

        v = vector(v_x, v_y, v_z)

        print(cross(u,v))
        print('Your lucky numbers are {0} {1} {2} {3} {4} {5} {6}'.format(random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100)))
        run = input('Run? (0) Yes, (1) No.')
    elif option == 1:
        print('----- First Vector -----')
        u_x = input('What is the first component of the first vector?\n>> ')
        u_y = input('What is the second component of the first vector?\n>> ')
        u_z = input('What is the third component of the first vector?\n>> ')

        print('----- Second Vector -----')

        v_x = input('What is the first component of the second vector?\n>> ')
        v_y = input('What is the second component of the second vector?\n>> ')
        v_z = input('What is the third component of the second vector?\n>> ')

        u = vector(u_x, u_y, u_z)

        v = vector(v_x, v_y, v_z)

        print(dot(u,v))
        print('Your lucky numbers are {0} {1} {2} {3} {4} {5} {6}'.format(random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100)))
        run = input('Run Again? (0) Yes, (1) No.')
    else:
        print('Invalid Option')
        print('Your lucky numbers are {0} {1} {2} {3} {4} {5} {6}'.format(random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100),random.randint(0,100),
                                                                          random.randint(0,100)))
        run = input('Run Again? (0) Yes, (1) No.')

if run != 0:
    print('Your lucky numbers are {0} {1} {2} {3} {4} {5} {6}'.format(random.randint(1, 100), random.randint(1, 100),
                                                                      random.randint(1, 100), random.randint(1, 100),
                                                                      random.randint(1, 100), random.randint(1, 100),
                                                                      random.randint(1, 100)))

