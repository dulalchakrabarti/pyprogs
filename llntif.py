from osgeo import gdal
import struct
from osgeo import gdalconst

# Open tif file
ds = gdal.Open('/home/dc/codes/0_modified.tif')
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
#print bands
band1 = ds.GetRasterBand(1)
band2 = ds.GetRasterBand(2)
band3 = ds.GetRasterBand(3)
#bandtype = gdal.GetDataTypeName(band.DataType)
fl = open('lln.csv','w')
count = 0
for row in range(rows):
 for col in range(colms):
  lon, lat = pixel2coord(col, row)
  pix1 = band1.ReadRaster( col, row, 1,1,1, 1, band1.DataType)
  val1 = struct.unpack('B', pix1)
  pix2 = band2.ReadRaster( col, row, 1,1,1, 1, band2.DataType)
  val2 = struct.unpack('B', pix2)
  pix3 = band3.ReadRaster( col, row, 1,1,1, 1, band3.DataType)
  val3 = struct.unpack('B', pix3)
  #print val1[0],val2[0],val3[0]
  if val1[0] > 200 and val2[0] < 100 and val3[0] <100:
   print(val1[0],val2[0],val3[0])
   count = count +1
   if count%15 == 0:
    fl.write(str(lat)+','+str(lon)+','+str(val1[0])+'\n')
print(count)
fl.close()
