from __future__ import division, print_function
import visual as vis
#from visual.graph import *
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
class Planetary(tk.Frame):
	scene = vis.display()
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.createWidgets(master)

	def createWidgets(self, master):
		self.star_color = tk.StringVar()
		colorlst = ["100", "001", "010"]
		color = tk.Radiobutton(master, text="Red", variable=self.star_color, value=colorlst[0])
		color.grid(row=0, column=0)

		color = tk.Radiobutton(master, text="Blue", variable=self.star_color, value=colorlst[1])
		color.grid(row=1, column=0)

		color = tk.Radiobutton(master, text="Green", variable=self.star_color, value=colorlst[2])
		color.grid(row=1, column=0)

		self.star_color.set(colorlst[0])

		update = tk.Button(master, text="update", command=lambda: self.object(master, self.star_color.get()))
		update.grid(row=2, column=0)

	def object(self, master, color_obj):
		star_obj = vis.sphere()
		star_obj.color  = vis.vector(int(color_obj[0]), int(color_obj[1]), int(color_obj[2])) #vis.vector(1, 0, 0)

		#print(color)
		#print(star_obj.color)

if __name__ == '__main__':
	root = tk.Tk()
	Planetary(root)
	root.title("Testing")

	def quit():
		global root
		root.quit()
		root.destroy()

	root.protocol("WM_DELETE_WINDOW", quit)
	root.update()
	root.update_idletasks()

	root.mainloop()
