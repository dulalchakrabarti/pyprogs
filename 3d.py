'''
In this example, we plot a spiral graph, and we will see its 360-degree view using a loop. Here, view_init(elev=, azim=)This can be used to rotate the axes programmatically.‘elev’ stores the elevation angle in the z plane. ‘azim’ stores the azimuth angle in the x,y plane.D constructor. The draw() function in pyplot module of the matplotlib library is used to redraw the current figure with a pause of 0.001-time interval.
'''

from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Creating 3D figure
fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection='3d')

# Creating Dataset
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z, 'green')

# 360 Degree view
for angle in range(0, 360):
	ax.view_init(angle, 30)
	plt.draw()
	plt.pause(.001)

plt.show()

