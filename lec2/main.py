import csv
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
y = abs(0.25 * x + (np.cos(x * 100)) * np.sin(0.25 * x))
pylab.plot(x, y, linewidth=2.0, label='numPy func')
pylab.title('Func')
pylab.xlabel('X')
pylab.ylabel('Y') 
pylab.legend()
plt.show()