import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



def gen_arrow_head_marker(rot):
    """generate a marker to plot with matplotlib scatter, plot, ...
    """
    arr = np.array([[.1, .3], [.1, -.3], [1, 0], [.1, .3]])  # arrow shape
    angle = rot / 180 * np.pi
    rot_mat = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)]
        ])
    arr = np.matmul(arr, rot_mat)  # rotates the arrow

    # scale
    x0 = np.amin(arr[:, 0])
    x1 = np.amax(arr[:, 0])
    y0 = np.amin(arr[:, 1])
    y1 = np.amax(arr[:, 1])
    scale = np.amax(np.abs([x0, x1, y0, y1]))
    codes = [mpl.path.Path.MOVETO, mpl.path.Path.LINETO,mpl.path.Path.LINETO, mpl.path.Path.CLOSEPOLY]
    arrow_head_marker = mpl.path.Path(arr, codes)
    return arrow_head_marker, scale

fig, ax = plt.subplots()
for rot in [0, 15, 30, 45, 60, 90, 110, 180, 210, 315, 360]:

    marker, scale = gen_arrow_head_marker(rot)
    markersize = 20
    ax.scatter(rot, 0, marker=marker, s=(markersize*scale)**2)

ax.set_xlabel('Rotation in degree')
plt.show()
