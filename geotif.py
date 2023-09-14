from osgeo import gdal
import struct
from gdalconst import *

# Open tif file
ds = gdal.Open('terra.tif')
# GDAL affine transform parameters, According to gdal documentation xoff/yoff are image left corner, a/e are pixel width/height and b/d is rotation and is zero if image is north up. 
xoff, a, b, yoff, d, e = ds.GetGeoTransform()
def pixel2coord(x, y):
    """Returns global coordinates from pixel x, y coords"""
    xp = a * x + b * y + xoff
    yp = d * x + e * y + yoff
    return(xp, yp)
colms = ds.RasterXSize
rows = ds.RasterYSize
bands = ds.RasterCount
band = ds.GetRasterBand(1)
bandtype = gdal.GetDataTypeName(band.DataType)
count = 0
for row in range(rows):
 for col in range(colms):
  lon, lat = pixel2coord(col, row)
  pix = band.ReadRaster( col, row, 1,1,1, 1, band.DataType)
  val = struct.unpack('f', pix)
  count = count +1
  if val[0] > 0 and val[0] < 200:
   print lat, lon, val[0]
print count
