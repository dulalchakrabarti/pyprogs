#!/usr/bin/env python
from osgeo import gdal
from osgeo import osr
import numpy as np
import os, sys

#  Initialize the Image Size
image_size = (9,9)

dx = 0.046207358
dy = 0.046207358
latx = 73.82
laty = 15.48
#  Choose some Geographic Transform (Around Lake Tahoe)
lat = [laty+4*dy,laty-4*dy]
lon = [latx-4*dx,latx+4*dx]
pixel=np.array([255,52,52,50,50,71,71,255,255,255,255,255,47,47,255,255,255,255,255,255,255,47,47,255,255,255,255,58,255,255,255,255,255,255,255,255,255,32,32,43,43,67,67,50,50,255,32,32,43,43,67,67,50,50,254,39,39,42,42,42,42,49,49,254,39,39,42,42,42,42,49,49,255,255,255,255,255,34,34,38,38])
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
dst_ds = gdal.GetDriverByName('GTiff').Create('myGeoTIFF.tif', ny, nx, 3, gdal.GDT_Byte)

dst_ds.SetGeoTransform(geotransform)    # specify coords
srs = osr.SpatialReference()            # establish encoding
srs.ImportFromEPSG(4326)                # WGS84 lat/long
dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
dst_ds.GetRasterBand(1).WriteArray(r_pixels)   # write r-band to the raster
dst_ds.GetRasterBand(2).WriteArray(g_pixels)   # write g-band to the raster
dst_ds.GetRasterBand(3).WriteArray(b_pixels)   # write b-band to the raster
dst_ds.FlushCache()                     # write to disk
dst_ds = None
