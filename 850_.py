from PIL import Image
import numpy as np
from rasterio.windows import Window
import rasterio

with rasterio.open('850bl.png') as src:
    b, g, r = (src.read(k) for k in (1, 2, 3))
# src.height = 718, src.width = 791
write_window = Window.from_slices((30, 269), (50, 313))
# write_window.height = 239, write_window.width = 263
with rasterio.open(
        'test.tif', 'w',
        driver='GTiff', width=500, height=300, count=3,
        dtype=r.dtype) as dst:
    for k, arr in [(1, b), (2, g), (3, r)]:
        dst.write(arr, indexes=k, window=write_window)
