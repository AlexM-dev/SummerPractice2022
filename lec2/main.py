import csv
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos
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
            
        
fig, ax = plt.subplots()
ax.plot(x1, y1, label='Offshore minerals')
ax.plot(x2, y2, label='Shipping')
ax.set_title('Value')
ax.set_xlabel('Year')
ax.set_ylabel('Value') 

x = np.linspace(2007, 2020, 1000000)
#y =  1e6 + 1e6 * np.sin(x * x)

y = 1e4 * abs(0.25 * x + 75 * (np.cos(x * 100)) * np.sin(2 * x)) - 3.3e6
ax.plot(x, y, linewidth=2.0, label='numPy func')
ax.legend()

plt.show()