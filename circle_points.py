import math
from math import pi


def points_on_circumference(center=(0, 0), r=50, n=100):
    return [
        (
            center[0]+(math.cos(2 * pi / n * x) * r),  # x
            center[1] + (math.sin(2 * pi / n * x) * r)  # y

        ) for x in xrange(0, n + 1)]


pts = points_on_circumference(center=(-10,-10),r=50)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
l =[k[0] for k in pts]
y =[x[1] for x in pts]
z1 = [40 for x in range(len(pts))]
z2 = [20 for x in range(len(pts))]

ax.plot3D(l, y, z1, 'gray')
ax.plot3D(l, y, z2, 'gray')
plt.show()

