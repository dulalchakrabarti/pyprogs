from osgeo import gdal
import struct
from gdalconst import *
d1 = {}
for idx in range(256):
 d1[idx] = 0
fname1 = raw_input('First tif file name?(ex. jpr01jan):')
# Open tif file
ds = gdal.Open('/home/dulal/ndvi/'+fname1)
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
  lat, lon = pixel2coord(col, row)
  pix = band.ReadRaster( col, row, 1,1,1, 1, band.DataType)
  val = struct.unpack('B', pix)
  count = count +1
  #print lat, lon, val[0]
  d1[val[0]] = d1[val[0]] + 1
#print count

#print d1
d2 = {}
for idx in range(256):
 d2[idx] = 0
# Open tif file
fname2 = raw_input('Second tif file name?(ex. jpr16jan):')
ds2 = gdal.Open('/home/dulal/ndvi/'+fname2)
# GDAL affine transform parameters, According to gdal documentation xoff/yoff are image left corner, a/e are pixel width/height and b/d is rotation and is zero if image is north up. 
xoff, a, b, yoff, d, e = ds2.GetGeoTransform()
colms = ds2.RasterXSize
rows = ds2.RasterYSize
bands = ds2.RasterCount
band = ds2.GetRasterBand(1)
bandtype = gdal.GetDataTypeName(band.DataType)
count = 0
for row in range(rows):
 for col in range(colms):
  lat, lon = pixel2coord(col, row)
  pix = band.ReadRaster( col, row, 1,1,1, 1, band.DataType)
  val = struct.unpack('B', pix)
  count = count +1
  #print lat, lon, val[0]
  d2[val[0]] = d2[val[0]] + 1

#print d2
ndvi1 = raw_input('Lower value of ndvi?(ex. 0.57):')
ndvi2 = raw_input('Upper value of ndvi?(ex. 0.61):')
area = 0
for idx in range(1,256):
 #print idx,idx *.005,d2[idx],d1[idx]
 if (d2[idx] - d1[idx]) > 0:
  if idx*.005 >= float(ndvi1) and idx*.005 <= float(ndvi2):
   area = area + d2[idx]
print area
 
