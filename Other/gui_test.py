from __future__ import division, print_function
import visual as vis
import visual.materials as vismat
import visual.graph as vig
from numpy import *

try:
	import tkinter as tk
	from tkinter.colorchooser import askcolor
except ImportError:
	import Tkinter as tk
	from tkColorChooser import askcolor

#g1 = gdisplay(x=1000, y=510, width=700, height=500)
#g2 = gdisplay(x=550, y=510, width=700, height=500)
#g3 = gdisplay(x=550, y=0, width=700, height=500)

#G = 6.7e-11  # Nm^2/kg^2
#YinS = 365. * 24. * 60. * 60  # s
#AU = 1.5e11  # m
star = vis.sphere(make_trail=True)
planet = vis.sphere(make_trail=True)

class Planetary(tk.Frame):
	global star
	scene = vis.display()
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.createWidgets(master)

	def createWidgets(self, master):
		self.star_color = tk.StringVar()
		self.plot       = tk.StringVar()
		colorlst = ["255 000 000", "000 255 255", "255 255 255", "255 165 000"]
		color = tk.Radiobutton(master, text="Red", variable=self.star_color, value=colorlst[0])
		color.grid(row=0, column=0)

		color = tk.Radiobutton(master, text="Cyan", variable=self.star_color, value=colorlst[1])
		color.grid(row=1, column=0)

		color = tk.Radiobutton(master, text="White", variable=self.star_color, value=colorlst[2])
		color.grid(row=2, column=0)

		color = tk.Radiobutton(master, text="Orange", variable=self.star_color, value=colorlst[3])
		color.grid(row=3, column=0)

		self.star_color.set(colorlst[0])

		update = tk.Button(master, text="Update", command=lambda: self.object(master, self.star_color.get()))
		update.grid(row=4, column=0)

		plot_on = tk.Radiobutton(master, text="Plot", variable=self.plot, value="on")
		plot_on.grid(row=0, column=1)

		plot_off = tk.Radiobutton(master, text="No Plot", variable=self.plot, value="off")
		plot_off.grid(row=1, column=1)


	def object(self, master, color_obj):
		G = 6.7e-11  # Nm^2/kg^2
		YinS = 365. * 24. * 60. * 60  # s
		D = 1.5e11  # m

		star.color  = vis.vector(float(color_obj[0:3])/255, float(color_obj[4:7])/255, float(color_obj[8:11])/255) #vis.vector(1, 0, 0)
		star.pos = vis.vector(0, 0, 0)
		star.radius = 0.1

		star.m = 2e30
		star.v = vis.vector(0, 0, 0)
		star.p = star.m * star.v

		planet.pos = vis.vector(0, 0, 1)
		planet.radius = 0.1
		planet.m = 0.5 * star.m

		planet.v = vis.vector(0, sqrt(G * star.m/(vis.mag(planet.pos) * D)), 0)
		planet.p = planet.m * planet.v

		if self.plot.get() == "on":
			main_plot = vig.gdisplay(x=510, y=510, width=1100, height=550, xtitle="Time in Earth Years", ytitle="Position in Y [m]")
			main = vig.gcurve(gdisplay=main_plot, color=star.color)  # Define functions to plot

		t = 0
		dt = YinS / 10000

		while True:
			vis.rate(1e50)
			r = (planet.pos - star.pos) * D
			rmag = vis.mag(r)
			rhat = vis.norm(r)

			Fmag = (G * (star.m * planet.m)/rmag**2)

			Fnet = -Fmag * rhat

			planet.p = planet.p + Fnet *dt
			planet.pos = planet.pos + (planet.p/planet.m/D) * dt

			if self.plot.get() == "on":
				main.plot(pos=(t/YinS, planet.pos.y))

			master.update()
			master.update_idletasks()

			t = t + dt

		#print(color)
		#print(star_obj.color)

if __name__ == '__main__':
	root = tk.Tk()
	Planetary(root)
	root.title("Testing")

	root.geometry("425x425")

	def quit():
		global root
		root.quit()
		root.destroy()

	root.protocol("WM_DELETE_WINDOW", quit)
	root.update()
	root.update_idletasks()

	root.mainloop()
