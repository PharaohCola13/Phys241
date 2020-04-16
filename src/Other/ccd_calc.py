########
## Title: ccd_calc.py
## Author: Spencer Riley
## Python 3.5.2
########
from numpy import *
# Latitude
phi = 34.059
# Day of the year
<<<<<<< HEAD
Nday = 34
# Time of expected observation
h = 19 # Clock Hour
m = 0.0 # Clock Minute
=======
Nday = 329.0
# Time of expected observation
h = 19.0 # Clock Hour
m = 21.0 # Clock Minute
>>>>>>> 818ec196400f1d8963f597e60db6dbcca9eb35ef
T = ((h*60.0) + m)/60.0 # Time in units of hours
# Right Ascention from handout
RA_hm = [
    [1,33.2],[1,36.7],[1,42.4],[2,3.9],[4,3.3],[5,34.5],
    [5,52.4],[6,28.8],[7,29.2],[7,36.9],[9,55.8],[11,14.8],
    [12,30.8],[12,39.5],[12,56],[12,56.7],[13,29.9],[15,5.7],
    [16,41.7],[18,18.8],[18,44.3],[18,51.1],[20,34.8],[21,30]]
# Declination from handout
delta = [
    [60,42],[15,47],[51,34],[42,19],[36,25],[22,1],[32,33],[-7,2],
    [20,55],[65,36],[69,41],[55,1],[12,24],[-26,45],[38,19],[21,41],
    [47,12],[-55,36],[36,28],[-13,47],[39,39],[-6,16],[60,9],[12,10]
]
# Initial list for unit conversions
RA_deg      = []
delta_deg   = []
# Local Sidereal Time in degrees
LST = (((Nday - 80.0)/365.24) * 23.94 + (T - 12.0)) * 60.0 * (18.0/72.0)
# Converts RA to degrees
for i in RA_hm:
    ra  = ((i[0]*60.0) + i[1]) * (18.0/72.0)
    RA_deg.append(ra)
# Converts Declination angle to degrees
for i in delta:
    d   = i[0] + (i[1]/60.0)
    delta_deg.append(d)
# Hour Angle
H = array(RA_deg) - LST
# Altitude
gamma = arcsin((sin(deg2rad(phi))*sin(deg2rad(delta_deg))) + (cos(deg2rad(phi))*cos(deg2rad(delta_deg))*cos(deg2rad(H))))
# Filters out all objects that don't meet the 30 degrees threshold
for i in arange(0,len(gamma)):
    if rad2deg(gamma[i]) >= 30.0:
        print("{}|Altitude = {:.2f}".format(i+1, rad2deg(gamma[i])))
    else:
        continue
