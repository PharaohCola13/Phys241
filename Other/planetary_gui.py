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

dim = "#303030"  #   Background
dimf = "#00C0FF"  #   Font Color
disa = "#d400ff" #   Disabled Text

scene = vis.display()
star = vis.sphere(make_trail=True)
planet = vis.sphere(make_trail=True)
main_plot = vig.gdisplay(x=510, y=510, width=1100, height=550, xtitle="Time in Earth Years",
						 ytitle="Position in Y [m]")
planetlabel = vis.label()
starlabel = vis.label()

class Planetary(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		master.bind("<Return>", self.planetary_system)
		self.createWidgets(master)


	def createWidgets(self, master):
		self.star_color = tk.StringVar()
		self.plot       = tk.StringVar()
		self.star_name	= tk.StringVar()
		self.planet_name = tk.StringVar()

		self.colordict = {"Red" 		: "(255,000,000)",
						  "Cyan" 		: "(000,255,255)",
						  "White"		: "(255,255,255)",
						  "Orange"		: "(255,165,000)",
						  "Yellow"		: "(255,255,000)",
						  "Yellow-White": "(255,255,224)",
						  "Purple"		: "(255,000,255)",
					}


		self.plot_on = tk.Radiobutton(master, text="Plot", variable=self.plot, value="on")
		self.plot_on.grid(row=0, column=0, sticky='nsw')

		self.plot_off = tk.Radiobutton(master, text="No Plot", variable=self.plot, value="off")
		self.plot_off.grid(row=1, column=0, sticky='nsw')

		self.plot.set("off")


		self.time = tk.Label(master, text="0.0e-00 Earth Years")
		self.time.grid(row=13, column=0, columnspan=2, sticky='nsew')
		n = 4
		# Mass of Star

		self.star_label = tk.Label(master, text="--- Main Star ---")
		self.star_label.grid(row=n-1, column=0, columnspan=10, sticky='nsew')

		self.starname_label = tk.Label(master, text="Star Name:")
		self.starname_label.grid(row=0, column=1, sticky='nsew')
		self.starname = tk.Entry(master, textvariable=self.star_name, width=10)
		self.starname.grid(row=0, column=2, columnspan=2,  sticky='nsew')
		self.star_name.set("Sol")

		self.mass_label = tk.Label(master, text="Mass (kg) = ")
		self.mass_label.grid(row=n, column=0, sticky='new', pady=20)
		self.masscoeff = tk.Scale(master, from_=-10, to=50, resolution=0.25, orient=tk.HORIZONTAL)
		self.masscoeff.grid(row=n, column=1, sticky='new')
		self.masscoeff.set(1)

		self.mass_label2 = tk.Label(master, text="X 10^")
		self.mass_label2.grid(row=n, column=2, sticky='new', pady=20)

		self.massexp = tk.Scale(master, from_=-10, to=50, resolution=0.25, orient=tk.HORIZONTAL)
		self.massexp.grid(row=n, column=3, sticky='new')
		self.massexp.set(1)

		self.label = str(self.masscoeff.get()) + "X10^(" + str(self.massexp.get()) + ")"

		self.mass = tk.Message(master, text=self.label, relief=tk.GROOVE)
		self.mass.config(width=150, fg=dimf, bg=dim)
		self.mass.grid(row=n, column=4, columnspan=6, sticky='nsew', pady=18)

		# Mass of Planet
		self.planet_label = tk.Label(master, text="--- Planet(s) ---")
		self.planet_label.grid(row=n+1, column=0, columnspan=10, sticky='nsew')

		self.planetname_label = tk.Label(master, text="Planet Name:")
		self.planetname_label.grid(row=1, column=1, sticky='nsew')
		self.planetname = tk.Entry(master, textvariable=self.planet_name, width=10)
		self.planetname.grid(row=1, column=2, columnspan=2,  sticky='nsew')
		self.planet_name.set("Terra")

		self.mass_label1 = tk.Label(master, text="Mass (kg) = ")
		self.mass_label1.grid(row=n+2, column=0, sticky='new', pady=20)
		self.masscoeff1 = tk.Scale(master, from_=-10, to=50, resolution=0.25, orient=tk.HORIZONTAL)
		self.masscoeff1.grid(row=n+2, column=1, sticky='new')
		self.masscoeff1.set(1)

		self.mass_label21 = tk.Label(master, text="X 10^")
		self.mass_label21.grid(row=n+2, column=2, sticky='new', pady=20)

		self.massexp1 = tk.Scale(master, from_=-10, to=50, resolution=0.25, orient=tk.HORIZONTAL)
		self.massexp1.grid(row=n+2, column=3, sticky='new')
		self.massexp1.set(1)

		self.label1 =str(self.masscoeff1.get()) + "X10^(" + str(self.massexp1.get()) + ")"

		self.mass1 = tk.Message(master, text=self.label1, relief=tk.GROOVE)
		self.mass1.config(width=150, fg=dimf, bg=dim)
		self.mass1.grid(row=n+2, column=4, columnspan=5, sticky='nsew', pady=18)

# #		# Update
		self.update = tk.Button(master, text="Update", command=lambda: self.planetary_system(master))
		self.update.grid(row=10, column=0, columnspan=2, rowspan=3, sticky='nsew')

		def dark(self):
			self.scales = [self.massexp1, self.masscoeff1, self.massexp, self.masscoeff]
			self.button = [self.update]
			self.radio  = [self.plot_on, self.plot_off]
			self.labels = [self.mass_label, self.mass_label2, 
						   self.mass_label1, self.mass_label21, self.planet_label, self.star_label, self.starname_label, self.planetname_label, self.time]
			master.config(background=dim)
			for m in self.scales:
				m.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimf)
			for n in self.labels:
				n.config(bg=dim, fg=dimf, activebackground=dim)
			for o in self.radio:
				o.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
						 selectcolor=dim)
			for p in self.button:
				p.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)
		return dark(self)

	def unbound(self):
		top = tk.Toplevel(self)
		top.config(background=dim)
		top.maxsize(170, 170)
		top.minsize(170, 170)
		top.title("Unbound System")
		top.focus_set()
		top.grab_set()

		pop = tk.Button(top, text="POP!", command=top.destroy)
		pop.grid(row=0, column=0, columnspan=5, sticky='nsew')
		pop.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

		elvis = tk.Message(top, text="Elvis has left the building!")
		elvis.grid(row=1, column=0, columnspan=5, rowspan=5, sticky='nsew')
		elvis.config(fg=dimf, bg=dim, width=175)

	def RGB(self, red,green,blue): 
		return '#%02x%02x%02x' % (red,green,blue)
	def planetary_system(self, master):
		global star, planet, main_plot, planetlabel, starlabel
		solarmass = 1.989e30 # in kg
		#self.unbound()
		self.label 	=str(self.masscoeff.get()) + "X10^(" + str(self.massexp.get()) + ")"
		self.label1 =str(self.masscoeff1.get()) + "X10^(" + str(self.massexp1.get()) + ")"
		#tk_color = self.RGB(int(self.star_color.get()[1:4]),int(self.star_color.get()[5:8]), int(self.star_color.get()[9:12]))
		self.mass.config(text=self.label)
		self.mass1.config(text=self.label1)

		starm = self.masscoeff.get()* 10**self.massexp.get()
		starcolor = self.colordict["Purple"]
		if starm <= 50 * solarmass: # Class O
			starcolor = self.colordict["Cyan"]
			tk_color = self.RGB(int(starcolor[1:4]),int(starcolor[5:8]), int(starcolor[9:12]))
			self.massexp.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
			self.masscoeff.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
			if starm <= 1 * solarmass: # Class G
				starcolor = self.colordict["Yellow"]
				tk_color = self.RGB(int(starcolor[1:4]),int(starcolor[5:8]), int(starcolor[9:12]))
				self.massexp.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
				self.masscoeff.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
				if starm <= 0.7 * solarmass: # Class K
					starcolor = self.colordict["Orange"]
					tk_color = self.RGB(int(starcolor[1:4]),int(starcolor[5:8]), int(starcolor[9:12]))
					self.massexp.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
					self.masscoeff.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
					if starm <= 0.2 * solarmass: # Class M
						starcolor = self.colordict["Red"]
						tk_color = self.RGB(int(starcolor[1:4]),int(starcolor[5:8]), int(starcolor[9:12]))
						self.massexp.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
						self.masscoeff.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
						if starm <= 0.1 * solarmass: # Class D
							starcolor = self.colordict["White"]
							tk_color = self.RGB(int(starcolor[1:4]),int(starcolor[5:8]), int(starcolor[9:12]))
							self.massexp.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
							self.masscoeff.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
							if starm <= 0: # Negative Mass
								starcolor = self.colordict["Purple"]
								tk_color = self.RGB(int(starcolor[1:4]),int(starcolor[5:8]), int(starcolor[9:12]))
								self.massexp.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
								self.masscoeff.config(troughcolor=tk_color, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
		else:
			print(starm)
			self.massexp.config(troughcolor=dimf, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)
			self.masscoeff.config(troughcolor=dimf, activebackground=dim, fg=dimf, bg=dim, highlightthickness=0)

		G = 6.7e-11  # Nm^2/kg^2
		YinS = 365. * 24. * 60. * 60  # s
		D = 1.5e11  # m

		star.color  = vis.vector(float(starcolor[1:4])/255, float(starcolor[5:8])/255, float(starcolor[9:12])/255) #vis.vector(1, 0, 0)
		star.pos = vis.vector(0, 0, 0)
		star.radius = 0.1

		star.m = self.masscoeff.get()* 10**self.massexp.get()
		print(star.m)
		star.v = vis.vector(0, 0, 0)
		star.p = star.m * star.v

		planet.pos = vis.vector(0, 0, 1)
		planet.radius = 0.1
		planet.m = self.masscoeff1.get()* 10**self.massexp1.get()

		planet.v = vis.vector(0, sqrt(G * star.m/(vis.mag(planet.pos) * D)), 0)
		planet.p = planet.m * planet.v

	#	if self.plot.get() == "on":
		main = vig.gcurve(gdisplay=main_plot, color=star.color)  # Define functions to plot

		t = 0
		dt = YinS/10000
		starlabel.pos=pos=vis.vector(0, 0.25, 0)
		starlabel.text=self.starname.get()
		while True:
			#print(planet.m)
			vis.rate(100000000000)
			r = (planet.pos - star.pos) * D
			rmag = vis.mag(r)
			rhat = vis.norm(r)
			Fmag = (G * (star.m * planet.m)/rmag**2)

			Fnet = -Fmag * rhat

			planet.p = planet.p + Fnet *dt
			planet.pos = planet.pos + (planet.p/planet.m/D) * dt

			if self.plot.get() == "on":
				main.plot(pos=(t/YinS, planet.pos.y))
			if rmag >= 100 * D:
				break
				self.unbound()

			master.update()
			master.update_idletasks()

			planetlabel.pos=planet.pos+ vis.vector(0, 0.25, 0)
			planetlabel.text=text=self.planet_name.get()

			self.time.config(text=str(t/YinS)+" Earth Years")
			t = t + dt

if __name__ == '__main__':
	root = tk.Tk()
	Planetary(root)
	root.title("Planetary Motion")

	#root.geometry("425x425")
	root.maxsize(455, 455)
	root.minsize(455, 455)

	#root.maxsize(425, 425)
	#root.minsize(425, 425)

	def quit():
		global root
		root.quit()
		root.destroy()

	root.protocol("WM_DELETE_WINDOW", quit)
	root.update()
	root.update_idletasks()
	def quit(self):
		global root
		root.quit()
		root.destroy()

	root.bind("<Escape>", quit)


	root.mainloop()
