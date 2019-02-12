# Spencer Riley
import numpy as np

f = open('./trig.spaghetti', 'w')
f.write("theta" + "\t" + "sin(theta)" + "\t" + "cos(theta)" + "\t" + "sin(theta)^2+cos(theta)^2" + "\n")
f.write("---"*25+"\n")


for i in np.arange(-90, 90, 2):
	theta   = i
	sin     = np.sin(np.deg2rad(i))
	cos     = np.cos(np.deg2rad(i))
	s2c2    = np.sin(np.deg2rad(i))**2 + np.cos(np.deg2rad(i))**2
	f.write("{}".format(theta) + "\t" + "{:1.4f}".format(sin) + "\t\t" + "{:1.4f}".format(cos)+ "\t\t"+ "{:1.18}".format(s2c2) + "\n")
f.close()
