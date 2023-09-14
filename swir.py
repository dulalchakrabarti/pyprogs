import pandas as pd
import numpy as np
from osgeo import osr,gdal
import struct
from osgeo.gdalconst import *
import os, sys
gl = open('cloudswir.txt', 'w')
stn = {}
lines = [line.rstrip('\n') for line in open('class.csv')]
for inp in lines:
 lst = inp.split(',')
 stn[lst[0]] = lst[1:]
#print(len(stn))
dec = {}
for key,val in stn.items():
 city = val[0]
 dec[city] = []
 lat = val[1]
 dec[city].append(lat)
 lon = val[2]
 dec[city].append(lon)
 cls = val[3]
 dec[city].append(cls)
#print(len(dec))
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
dx = 0.018360881876131
dy = 0.018360881876131
keylist = dec.keys()
sorted(keylist)
#print(len(keylist))
count=0
for key in keylist:
 #if float(dec[key][0]) < 35 and float(dec[key][1]) > 60:
 pix = latLonToPixel('/home/dc/rapidnight/swir.tif',[
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
 count+=1
 dec[key].extend(pix)
 val = ','.join(str(x) for x in dec[key][3:])
 #print(str(key)+','+str(dec[key][0])+','+str(dec[key][1])+str(dec[key][2])+','+val)
 gl.write(str(key)+','+str(dec[key][0])+','+str(dec[key][1])+','+str(dec[key][2])+','+val+'\n')
gl.close()
#print(count)
lst = list(dec.values())
#print(len(lst))
count = 0
for item in lst:
 #print(item)
 #  Initialize the Image Size
 image_size = (9,9)
 latx = float(item[1])
 laty = float(item[0])
 #  Choose some Geographic Transform (Around Lake Tahoe)
 lat = [laty+4*dy,laty-4*dy]
 lon = [latx-4*dx,latx+4*dx]
 #print(lat,lon)
 arr = [int(i) for i in item[3:]]
 pixel = np.array(arr)
 #print(pixel.shape)
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
 fname = item[0]+item[1]
 dst_ds = gdal.GetDriverByName('GTiff').Create(fname+'.tif', ny, nx, 3, gdal.GDT_Byte)
 dst_ds.SetGeoTransform(geotransform)    # specify coords
 srs = osr.SpatialReference()            # establish encoding
 srs.ImportFromEPSG(4326)                # WGS84 lat/long
 dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
 dst_ds.GetRasterBand(1).WriteArray(r_pixels)   # write r-band to the raster
 dst_ds.GetRasterBand(2).WriteArray(g_pixels)   # write g-band to the raster
 dst_ds.GetRasterBand(3).WriteArray(b_pixels)   # write b-band to the raster
 dst_ds.FlushCache()                     # write to disk
 dst_ds = None
 count+=1
 #print(fname,'created')
print(count)
