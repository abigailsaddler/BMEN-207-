"""
Created on Fri May  8 06:13:12 2020

@author: john.hanks
version 1.0
"""

from matplotlib import pyplot as plt
import random as rand
import numpy as np
#import inspect

# to open an interactive plot window type %matplotlib in the console window

# here is how to close all open figures so we don't write over plts
for i in range(1,plt.gcf().number+1):
    plt.close(plt.gcf().number)

# if you just have one figure you can use plt.close()    
#plt.close() 

# linspace is good for equally spaced x increments
x_axis = np.linspace(0,10,100)
y_axis_1 = 3*np.ones(100)
y_axis_2 = np.ones(100)

# generate some random data
for i in range(0,len(x_axis)):
    y_axis_1[i] = i + rand.randint(-2,5)
    y_axis_2[i] = y_axis_2[i] + rand.randint(-2,3)
 
# This is the simplest way to plot one figure with multiple plots   
plt.plot(x_axis, y_axis_1, label="ch1")
plt.plot(x_axis, y_axis_2, label="ch2")
plt.legend(loc='upper left')
plt.ylabel('volts')
plt.xlabel('time(ms)')
plt.title('Signals with Noise')
plt.show()


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# This plots the histogram of the data in a second figure
fig2 = plt.figure()
new_plot = fig2.add_subplot(111)
n, bins, patches = new_plot.hist(x, 50, density=True, facecolor='g', alpha=0.75)

new_plot.set_xlabel('Smarts')
new_plot.set_ylabel('Probability')
new_plot.set_title('Histogram of IQ')

# some advanced excape codes for mu and sigma
new_plot.text(60, .025, '\u03BC=100, \u03C3=15')

# set the x and y limits
new_plot.set_xlim(40, 160)
new_plot.set_ylim(0, 0.03)

# turn on a grid
new_plot.grid(True)
plt.show()

# Show vertical plots in a 3rd figure
# Here is how to have multiple plots in one figure, use subplot(s)  (with an s)
fig3, (ax1,ax2) = plt.subplots(2)
ax1.plot(x_axis,y_axis_1)
ax1.plot(x_axis,y_axis_2)
ax1.set_xlabel('time')
ax1.set_ylabel('Volts')
ax1.set_title('Signal with Noise ')
ax1.plot(x_axis, y_axis_1, label="ch1")
ax1.plot(x_axis, y_axis_2, label="ch2")

# the second sub plot
n, bins, patches = ax2.hist(x, 50, density=True, facecolor='b', alpha=0.75)
ax2.set_xlabel('Smarts')
ax2.set_ylabel('Probability')
ax2.set_title('Histogram of IQ')

# some advanced excape codes for mu and sigma
ax2.text(60, .025, '\u03BC=100, \u03C3=15')
ax2.set_xlim(40, 160)
ax2.set_ylim(0, 0.03)
ax2.grid(True)

# remove white spacing from border
plt.tight_layout()
plt.show()

