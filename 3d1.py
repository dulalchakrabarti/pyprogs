from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(8, 8))
ax = Axes3D(fig)
# Creating Dataset
zz = np.linspace(0, 15, 1000)
xx = np.sin(zz)
yy = np.cos(zz)
ax.scatter(xx,yy,zz, marker='o', s=20, c="goldenrod", alpha=0.6)
for ii in range(0,360,10):
 ax.view_init(elev=10., azim=ii)
 plt.draw()
 plt.pause(.001)
plt.show()

