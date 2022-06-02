'''import csv
from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos
from matplotlib.animation import FuncAnimation
import pylab

plt.style.use('dark_background')

x1 = []
y1 = []

x2 = []
y2 = []
with open('file.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['category'] == 'Offshore minerals' and row['variable'] == 'GDP':
            y1.append(int(row['data_value']))
            x1.append(int(row['year']))
        elif row['category'] == 'Shipping' and row['variable'] == 'GDP':
            y2.append(int(row['data_value']))
            x2.append(int(row['year']))
            

pylab.subplot (1, 2, 1)
pylab.plot(x1, y1, label='Offshore minerals')
pylab.plot(x2, y2, label='Shipping')
pylab.title('GDP')
pylab.xlabel('Year')
pylab.ylabel('Value') 
pylab.legend()

pylab.subplot (1, 2, 2)
x = np.linspace(0, 100, 1000000)
i = 0.0
pylab.title('Func')
pylab.xlabel('X')
pylab.ylabel('Y') 
pylab.legend()
while True:
    y = abs(0.25 * x + (np.cos(x * 100)) * np.sin(0.25 * x)) + i
    pylab.plot(x, y, linewidth=2.0, label='numPy func')
    i+=0.1
    plt.show()'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
from math import sin, cos
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

x1 = []
y1 = []

x2 = []
y2 = []
with open('file.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['category'] == 'Offshore minerals' and row['variable'] == 'GDP':
            y1.append(int(row['data_value']))
            x1.append(int(row['year']))
        elif row['category'] == 'Shipping' and row['variable'] == 'GDP':
            y2.append(int(row['data_value']))
            x2.append(int(row['year']))

x = np.linspace(0,15,100)

fig = plt.figure()
p1 = fig.add_subplot(121)
p2 = fig.add_subplot(122)

p1.set_title('GDP')
p1.set_xlabel('Year')
p1.set_ylabel('Value') 

p2.set_title('Sin')
p2.set_xlabel('X')
p2.set_ylabel('Y') 

p2.set_xlim([0, 4])
p2.set_ylim([-1.5, 1.5])

# set up empty lines to be updates later on
l1, = p2.plot([],[],'b')

l2, = p1.plot(x1, y1, label='Offshore minerals')
l3, = p1.plot(x2, y2, label='Shipping')
p1.legend()

def init():
    l1.set_data([], [])
    l1.set_label('Sin')
    return l1,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(np.pi * (x - 0.01 * i))
    l1.set_data(x, y)
    return l1,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
plt.show()