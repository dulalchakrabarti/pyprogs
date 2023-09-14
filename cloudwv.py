import string
stn = {}
fl = open('india_station.csv')
gl = open('zzxxwv.csv','w')
hl = open('nchhwv.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 stn[line[0]]=line[1:]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
lines = [line.rstrip('\n') for line in open('aaxx.txt')]
for inp in lines:
 lst = inp.split()
 if len(lst)>0 and len(lst[0])==5:
  idx = lst[0]
  flag1 = True
  flag2 = True
  for word in lst[3:]:
   if word[:1] == '7': stn[idx].append(word[:5])
   if flag1:
    if word[:1] == '8':
     if len(word) > 2: stn[idx].append(word[:5])
     flag1 = False
   elif flag2:
    if word[:1] == '8' or word[:1] == '6'and stn.has_key(idx):
     if len(word) > 2: stn[idx].append(word[:5])
cld = {}
lines1 = [line.rstrip('\n') for line in open('cl.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 cld[inp1[0]] = inp1[1]
cmd = {}
lines1 = [line.rstrip('\n') for line in open('cm.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 cmd[inp1[0]] = inp1[1]
chd = {}
lines1 = [line.rstrip('\n') for line in open('ch.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 chd[inp1[0]] = inp1[1]
cd = {}
lines1 = [line.rstrip('\n') for line in open('c.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 cd[inp1[0]] = inp1[1]
hhd = {}
lines1 = [line.rstrip('\n') for line in open('hh.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 hhd[inp1[0]] = inp1[1]
wwd={}
lines1 = [line.rstrip('\n') for line in open('ww.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 wwd[inp1[0]] = inp1[1]
w1w2d={}
lines1 = [line.rstrip('\n') for line in open('w1w2.csv')]
for inp1 in lines1:
 inp1 = inp1.split(',')
 w1w2d[inp1[0]] = inp1[1]
#gl.write('city'+','+'lat'+','+'lon'+','+'ww'+','+'w1'+','+'w2'+','+'nh'+','+'cl'+','+'cm'+','+'ch'+','+'cov1'+','+'gen1'+','+'ht1'+','+'cov2'+','+'gen2'+','+'ht2'+','+'cov3'+','+'gen3'+','+'ht3'+','+'cov4'+','+'gen4'+','+'ht4'+','+'rf'+'\n')
dec = {}
for key,val in stn.items():
 if len(val) > 3:
  rf = 0.0
  city = val[0]
  dec[city] = []
  lat = val[1]
  dec[city].append(lat)
  lon = val[2]
  dec[city].append(lon)
  for idx in range(3,len(val)):
   if idx == 3:
    if val[idx][0] == '7' and '/' not in val[idx] and len(val[idx]) == 5:
     ww = wwd[val[idx][1:3]]
     w1 = w1w2d[val[idx][3]]
     w2 = w1w2d[val[idx][4]]
     text2 = ww+','+w1+','+w2
     dec[city].append('7www1w2')
     dec[city].append(text2)
     #print idx,val[0],text2
    elif val[idx][0] == '8' and '/' not in val[idx]:
     nh = val[idx][1]
     cl = cld[val[idx][2]]
     cm = cmd[val[idx][3]]
     ch = chd[val[idx][4]]
     text3 = nh+','+cl+','+cm+','+ch
     dec[city].append('8nccc')
     dec[city].append(text3)
     #print idx,val[0],text3
   elif idx == 4 and '/' not in val[idx]:
    if val[idx][0] == '6':
     rain = val[idx][1:4]
     rf = float(rain)
     if rf >= 990:
      rf = (rf-990)/10.0
     #dec[city].append(str(rf))
     #print idx,val[0],str(rf)
    elif val[idx][0] == '8' and '/' not in val[idx] and len(val[idx]) == 5:
     if '/' not in val[idx][3:5]:
      ht1 = val[idx][3:5]
      cov1 = val[idx][1]
      gen1 = cd[val[idx][2]]
      met1 = hhd[ht1]
      text4 = cov1+','+gen1+','+met1
      dec[city].append('8nchh')
      dec[city].append(text4)
      #print idx,val[0],text4
   elif idx == 5 and '/' not in val[idx]:
    if val[idx][0] == '6':
     rain = val[idx][1:4]
     rf = float(rain)
     if rf >= 990:
      rf = (rf-990)/10.0
     #dec[city].append(str(rf))
     #print val[0],str(rf)
    elif val[idx][0] == '8' and '/' not in val[idx]:
     if '/' in val[idx][3:5]:
      ht2 = val[idx][3]+'0'
     else:
      ht2 = val[idx][3:5]
      met2 = hhd[ht2]
     cov2 = val[idx][1]
     gen2 = cd[val[idx][2]]
     text5 = cov2+','+gen2+','+met2
     dec[city].append('8nchh')
     dec[city].append(text5)
     #print idx,val[0],text5
   elif idx > 5:
    if val[idx][0] == '8' and '/' not in val[idx] and len(val[idx]) == 5:
     if '/' in val[idx][3:5]:
      ht = val[idx][3]+'0'
     else:
      ht = val[idx][3:5]
     text6 = val[idx][1]+','+cd[val[idx][2]]+','+hhd[ht]
     dec[city].append('8nchh')
     dec[city].append(text6)
     #print idx,val[0],text6
  dec[city].append('6rrr/')
  dec[city].append(str(rf))
import pandas as pd
import numpy as np
from osgeo import osr,gdal
import struct
from gdalconst import *
def latLonToPixel(geotifAddr, latLonPairs):
	# Load the image dataset
	ds = gdal.Open(geotifAddr)
	# Get a geo-transform of the dataset
	gt = ds.GetGeoTransform()
	# Create a spatial reference object for the dataset
	srs = osr.SpatialReference()
	srs.ImportFromWkt(ds.GetProjection())
	# Set up the coordinate transformation object
	srsLatLong = srs.CloneGeogCS()
	ct = osr.CoordinateTransformation(srsLatLong,srs)
	# Go through all the point pairs and translate them to latitude/longitude pairings
	pixelPairs = []
	for point in latLonPairs:
		# Change the point locations into the GeoTransform space
		(point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
		# Translate the x and y coordinates into pixel values
		x = (point[1]-gt[0])/gt[1]
		y = (point[0]-gt[3])/gt[5]
		# Add the point to our return array
                band = ds.GetRasterBand(1)                   
                pix = band.ReadRaster(int(x),int(y), 1,1,1, 1, band.DataType)
                val = struct.unpack('B', pix)
		pixelPairs.append(val[0])
	return pixelPairs
dx = 0.046207358
dy = 0.046207358
keylist = dec.keys()
keylist.sort()
for key in keylist:
 #if float(dec[key][0]) < 35 and float(dec[key][1]) > 60:
 pix = latLonToPixel('/home/dulal/imgproc/insatin/wv.tif',[
[float(dec[key][0])+4*dy,float(dec[key][1])-4*dx],[float(dec[key][0])+4*dy,float(dec[key][1])-3*dx],[float(dec[key][0])+4*dy,float(dec[key][1])-2*dx],[float(dec[key][0])+4*dy,float(dec[key][1])-dx],[float(dec[key][0])+4*dy,float(dec[key][1])],[float(dec[key][0])+4*dy,float(dec[key][1])+dx],[float(dec[key][0])+4*dy,float(dec[key][1])+2*dx],[float(dec[key][0])+4*dy,float(dec[key][1])+3*dx],[float(dec[key][0])+4*dy,float(dec[key][1])+4*dx],
[float(dec[key][0])+3*dy,float(dec[key][1])-4*dx],[float(dec[key][0])+3*dy,float(dec[key][1])-3*dx],[float(dec[key][0])+3*dy,float(dec[key][1])-2*dx],[float(dec[key][0])+3*dy,float(dec[key][1])-dx],[float(dec[key][0])+3*dy,float(dec[key][1])],[float(dec[key][0])+3*dy,float(dec[key][1])+dx],[float(dec[key][0])+3*dy,float(dec[key][1])+2*dx],[float(dec[key][0])+3*dy,float(dec[key][1])+3*dx],[float(dec[key][0])+3*dy,float(dec[key][1])+4*dx],
[float(dec[key][0])+2*dy,float(dec[key][1])-4*dx],[float(dec[key][0])+2*dy,float(dec[key][1])-3*dx],[float(dec[key][0])+2*dy,float(dec[key][1])-2*dx],[float(dec[key][0])+2*dy,float(dec[key][1])-dx],[float(dec[key][0])+2*dy,float(dec[key][1])],[float(dec[key][0])+2*dy,float(dec[key][1])+dx],[float(dec[key][0])+2*dy,float(dec[key][1])+2*dx],[float(dec[key][0])+2*dy,float(dec[key][1])+3*dx],[float(dec[key][0])+2*dy,float(dec[key][1])+4*dx],
[float(dec[key][0])+dy,float(dec[key][1])-4*dx],[float(dec[key][0])+dy,float(dec[key][1])-3*dx],[float(dec[key][0])+dy,float(dec[key][1])-2*dx],[float(dec[key][0])+dy,float(dec[key][1])-dx],[float(dec[key][0])+dy,float(dec[key][1])],[float(dec[key][0])+dy,float(dec[key][1])+dx],[float(dec[key][0])+dy,float(dec[key][1])+2*dx],[float(dec[key][0])+dy,float(dec[key][1])+3*dx],[float(dec[key][0])+dy,float(dec[key][1])+4*dx],
[float(dec[key][0]),float(dec[key][1])-4*dx],[float(dec[key][0]),float(dec[key][1])-3*dx],[float(dec[key][0]),float(dec[key][1])-2*dx],[float(dec[key][0]),float(dec[key][1])-dx],[float(dec[key][0]),float(dec[key][1])],[float(dec[key][0]),float(dec[key][1])+dx],[float(dec[key][0]),float(dec[key][1])+2*dx],[float(dec[key][0]),float(dec[key][1])+3*dx],[float(dec[key][0]),float(dec[key][1])+4*dx],
[float(dec[key][0])-dy,float(dec[key][1])-4*dx],[float(dec[key][0])-dy,float(dec[key][1])-3*dx],[float(dec[key][0])-dy,float(dec[key][1])-2*dx],[float(dec[key][0])-dy,float(dec[key][1])-dx],[float(dec[key][0])-dy,float(dec[key][1])],[float(dec[key][0])-dy,float(dec[key][1])+dx],[float(dec[key][0])-dy,float(dec[key][1])+2*dx],[float(dec[key][0])-dy,float(dec[key][1])+3*dx],[float(dec[key][0])-dy,float(dec[key][1])+4*dx],
[float(dec[key][0])-2*dy,float(dec[key][1])-4*dx],[float(dec[key][0])-2*dy,float(dec[key][1])-3*dx],[float(dec[key][0])-2*dy,float(dec[key][1])-2*dx],[float(dec[key][0])-2*dy,float(dec[key][1])-dx],[float(dec[key][0])-2*dy,float(dec[key][1])],[float(dec[key][0])-2*dy,float(dec[key][1])+dx],[float(dec[key][0])-2*dy,float(dec[key][1])+2*dx],[float(dec[key][0])-2*dy,float(dec[key][1])+3*dx],[float(dec[key][0])-2*dy,float(dec[key][1])+4*dx],
[float(dec[key][0])-3*dy,float(dec[key][1])-4*dx],[float(dec[key][0])-3*dy,float(dec[key][1])-3*dx],[float(dec[key][0])-3*dy,float(dec[key][1])-2*dx],[float(dec[key][0])-3*dy,float(dec[key][1])-dx],[float(dec[key][0])-3*dy,float(dec[key][1])],[float(dec[key][0])-3*dy,float(dec[key][1])+dx],[float(dec[key][0])-3*dy,float(dec[key][1])+2*dx],[float(dec[key][0])-3*dy,float(dec[key][1])+3*dx],[float(dec[key][0])-3*dy,float(dec[key][1])+4*dx],
[float(dec[key][0])-4*dy,float(dec[key][1])-4*dx],[float(dec[key][0])-4*dy,float(dec[key][1])-3*dx],[float(dec[key][0])-4*dy,float(dec[key][1])-2*dx],[float(dec[key][0])-4*dy,float(dec[key][1])-dx],[float(dec[key][0])-4*dy,float(dec[key][1])],[float(dec[key][0])-4*dy,float(dec[key][1])+dx],[float(dec[key][0])-4*dy,float(dec[key][1])+2*dx],[float(dec[key][0])-4*dy,float(dec[key][1])+3*dx],[float(dec[key][0])-4*dy,float(dec[key][1])+4*dx]
])
  #dec[key].extend(pix)
 dec[key].append(pix)
 val = ','.join(str(x) for x in dec[key][-1])
 gl.write(str(key)+','+str(dec[key][0])+','+str(dec[key][1])+','+'['+val+']'+'\n')
 nchh = []
 idx1 = 0
 idx2 = 0
 idx3 = 0
 idx4 = 0
 if '8nchh' in dec[key]:  
  idx1 = dec[key].index('8nchh')
  nchh.append(dec[key][idx1+1])
 if '8nchh' in dec[key][idx1+1:]:  
  idx2 = dec[key][idx1+1:].index('8nchh')
  nchh.append(dec[key][idx1+1+idx2+1])
 if '8nchh' in dec[key][idx1+idx2+2:]:  
  idx3 = dec[key][idx1+idx2+2:].index('8nchh')
  nchh.append(dec[key][idx1+1+idx2+1+idx3+1])
 if '8nchh' in dec[key][idx1+idx2+idx3+3:]:  
  idx4 = dec[key][idx1+idx2+idx3+3:].index('8nchh')
  nchh.append(dec[key][idx1+1+idx2+1+idx3+1+idx4+1])
 #gl.write(key+','+(','.join(str(x) for x in dec[key])+'\n'))
 if len(nchh) > 0:
  hl.write(key+','+str(dec[key][0])+','+str(dec[key][1])+','+(','.join(str(x) for x in nchh))+'\n')
hl.close()
gl.close()

from osgeo import gdal
from osgeo import osr
import numpy as np
import os, sys

#  Initialize the Image Size
image_size = (9,9)
fl = open('zzxxwv.csv')
lines = [line.strip() for line in fl.readlines()]
for item in lines:
 idx = item.find('[')
 if idx > 0:
  lst = item[idx:]
  x = lst.split(',')
  x[0] = x[0][1:]
  x[-1] = x[-1][:-1]
  x = [int(i) for i in x]
  lst = item.split(',')
  if lst[0] != '':
   latx = float(lst[2])
   laty = float(lst[1])
   #  Choose some Geographic Transform (Around Lake Tahoe)
   lat = [laty+4*dy,laty-4*dy]
   lon = [latx-4*dx,latx+4*dx]
   pixel=np.array(x)

   #  Create Each Channel
   r_pixels = pixel.reshape(image_size)
   g_pixels = pixel.reshape(image_size)
   b_pixels = pixel.reshape(image_size)
   # set geotransform
   nx = image_size[0]
   ny = image_size[1]
   xmin, ymin, xmax, ymax = [min(lon), min(lat), max(lon), max(lat)]
   xres = (xmax - xmin) / float(nx)
   yres = (ymax - ymin) / float(ny)
   geotransform = (xmin, xres, 0, ymax, 0, -yres)

   # create the 3-band raster file
   dst_ds = gdal.GetDriverByName('GTiff').Create(lst[0][:3]+'.tif', ny, nx, 3, gdal.GDT_Byte)

   dst_ds.SetGeoTransform(geotransform)    # specify coords
   srs = osr.SpatialReference()            # establish encoding
   srs.ImportFromEPSG(4326)                # WGS84 lat/long
   dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
   dst_ds.GetRasterBand(1).WriteArray(r_pixels)   # write r-band to the raster
   dst_ds.GetRasterBand(2).WriteArray(g_pixels)   # write g-band to the raster
   dst_ds.GetRasterBand(3).WriteArray(b_pixels)   # write b-band to the raster
   dst_ds.FlushCache()                     # write to disk
   dst_ds = None

