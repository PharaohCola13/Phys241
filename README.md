# NMT Physics 241 Lab

This tutorial page will describe how to operate VPython scripts on a Linux Desktop. The screenshots used in this example are from Pycharm, the IDE that I am using.

**Note: This will only work for Python 2.**


## Table of Contents
  - [Setup](#setup)
  - [Executing Scripts](#executing-scripts)
  - [Issues](#issues)


## Setup
There are two primary packages that are needed to operate VPython on Linux. To install them input the following commands into your terminal.

```
apt-get install python-visual libgtkglextmm-x11-1.2-dev
```

## Executing Scripts


## Issues
A recurring issue with running VPython via this method is the following warning:
```
/usr/lib/python2.7/dist-packages/visual/materials.py:70: FutureWarning: 
comparison to `None` will result in an elementwise object comparison in the future.
  self.__setattr__(key, value)

```
Based on my experience, I have not noticed any consequences of this warning at all.
The VPython scripts will still run in the same fashion as in VIDLE.
