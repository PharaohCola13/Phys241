# NMT Physics 241 Lab

This tutorial page will describe how to operate VPython scripts on a Linux Desktop. The screenshots used in this example are from Pycharm, the IDE that I am using.

**Note: This will only work for Python 2.**


# Table of Contents
  - Setup
  - Executing Scripts
  - Issues


# Setup
---
There are two primary packages that are needed to operate VPython on Linux. To install them input the following commands into your terminal.

```
apt-get install python-visual libgtkglextmm-x11-1.2-dev
```

# Executing Scripts
---

Just like any other Python script, VPython scripts can be run in the terminal from the location of the file. 
To execute the script, type the following command into your terminal.
```
python [name of script file].py
```


# Issues
---
A recurring issue with running VPython via this method is the following warning:
```
/usr/lib/python2.7/dist-packages/visual/materials.py:70: FutureWarning: 
comparison to `None` will result in an elementwise object comparison in the future.
  self.__setattr__(key, value)

```
Based on my experience, I have not noticed any consequences of this warning at all.
The VPython scripts will still run in the same fashion as in VIDLE.

# VPython
---
## Objects
The objects that are pre-defined:
  - [Sphere](http://www.glowscript.org/docs/VPythonDocs/sphere.html)
  - [Box](http://www.glowscript.org/docs/VPythonDocs/box.html)
  - [Arrow](http://www.glowscript.org/docs/VPythonDocs/arrow.html)
  - [Cone](http://www.glowscript.org/docs/VPythonDocs/cone.html)
  - [Cylinder](http://www.glowscript.org/docs/VPythonDocs/cylinder.html)
  - [Pyramid](http://www.glowscript.org/docs/VPythonDocs/pyramid.html)
  - [Ellipsoid](http://www.glowscript.org/docs/VPythonDocs/ellipsoid.html)
  - [Ring](http://www.glowscript.org/docs/VPythonDocs/ring.html)

### Object attributes
```python
object           =   object_name(make_trail=True) # Creates the object
object.pos       =   vector(x, y, z) # Sets initial position
object.axis      =   vector(x, y, z) # Sets final position
object.radius    =   0.5 # Sets the radius
object.color     =   color.red # Sets the color
object.shininess =   0.6 # Sets the shininess
object.emissive  =   False 
object.opacity   =   0.8 # Sets the transparency 
```

## Color options
  - Red
  - Green
  - Blue
  - Magenta
  - Yellow
  - Orange
  - Black
  - White
  - Cyan
  - Purple
 
### Defining a color
Uses RGB color scheme. Ranges from 0 to 1.

```python
purple = vector(0.4, 0.2, 0.6)
object.color = purple
```