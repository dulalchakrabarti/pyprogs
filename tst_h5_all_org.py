import h5py
import numpy as np
from PIL import Image
import glob
import re
from time import sleep
from math import *
from osgeo import gdal
from osgeo import osr

def write_prod(data):
    '''
    '''
    print data.shape
    data = np.ma.masked_where(np.isnan(data), data)
    if np.max(data) > 255:
     img8 = map_uint16_to_uint8(data[0])
     im = Image.fromarray(img8)
     im = im.convert("L")
     return im
    else:
     im = Image.fromarray(data)
     im = im.convert("L")
     return im

def write_geotif( name ):
    '''
    '''
    f = h5py.File(name, 'r+')
    time = re.findall(r'\d+', name)
    sec = name.split('.')
    sec=sec[0].split('_')
    members = []
    f.visit(members.append)
    for i in range(len(members)):
     sub = members[i]
     if sub[:4] == 'IMG_':
      chan = '/'+sub
      data = f[chan][:]
      data = np.ma.masked_where(np.isnan(data), data)
      if len(data.shape)>2:
       chan,cols,rows = data.shape
       xmin = f.attrs['left_longitude'][0]
       xmax = f.attrs['right_longitude'][0]
       ymax = f.attrs['upper_latitude'][0]
       ymin = f.attrs['lower_latitude'][0]
       xres = (xmax - xmin)/cols
       yres = (ymax - ymin)/rows
       geotransform = (xmin, xres, 0, ymax, 0, -yres)
       dst_ds = gdal.GetDriverByName('GTiff').Create(sub+time[3]+sec[4]+'.tif', rows, cols, 1, gdal.GDT_Byte)
       dst_ds.SetGeoTransform(geotransform)    # specify coords
       srs = osr.SpatialReference()            # establish encoding
       srs.ImportFromEPSG(4326)                # WGS84 lat/long
       dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
       data = data.reshape(cols,rows)
       data = map_uint16_to_uint8(data)
       dst_ds.GetRasterBand(1).WriteArray(data)# write r-band to the raster
       dst_ds.FlushCache()                     # write to disk
       dst_ds = None
       print 'Saved.....'+sub+time[3]+sec[4]
       sleep(5)
      elif len(data.shape) == 2:
       print name,data.shape
       cols,rows = data.shape
       xmin = f.attrs['left_longitude'][0]
       xmax = f.attrs['right_longitude'][0]
       ymax = f.attrs['upper_latitude'][0]
       ymin = f.attrs['lower_latitude'][0]
       xres = (xmax - xmin)/cols
       yres = (ymax - ymin)/rows
       geotransform = (xmin, xres, 0, ymax, 0, -yres)
       dst_ds = gdal.GetDriverByName('GTiff').Create(sub+time[3]+sec[4]+'.tif', rows, cols, 1, gdal.GDT_Byte)
       dst_ds.SetGeoTransform(geotransform)    # specify coords
       srs = osr.SpatialReference()            # establish encoding
       srs.ImportFromEPSG(4326)                # WGS84 lat/long
       dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
       dat = write_prod(data)
       dst_ds.GetRasterBand(1).WriteArray(data)# write r-band to the raster
       dst_ds.FlushCache()                     # write to disk
       dst_ds = None
       print 'Saved.....'+sub+time[3]+sec[4]
       sleep(5)
     else:
      if len(sub) == 3:
       chan = '/'+sub
       data = f[chan][:]
       data = np.ma.masked_where(np.isnan(data), data)
       print sub,name,data.shape





def map_uint16_to_uint8(img, lower_bound=None, upper_bound=None):
    '''
    Map a 16-bit image trough a lookup table to convert it to 8-bit.

    Parameters
    ----------
    img: numpy.ndarray[np.uint16]
        image that should be mapped
    lower_bound: int, optional
        lower bound of the range that should be mapped to ``[0, 255]``,
        value must be in the range ``[0, 65535]`` and smaller than `upper_bound`
        (defaults to ``numpy.min(img)``)
    upper_bound: int, optional
       upper bound of the range that should be mapped to ``[0, 255]``,
       value must be in the range ``[0, 65535]`` and larger than `lower_bound`
       (defaults to ``numpy.max(img)``)

    Returns
    -------
    numpy.ndarray[uint8]
    '''
    if not(0 <= lower_bound < 2**16) and lower_bound is not None:
        raise ValueError(
            '"lower_bound" must be in the range [0, 65535]')
    if not(0 <= upper_bound < 2**16) and upper_bound is not None:
        raise ValueError(
            '"upper_bound" must be in the range [0, 65535]')
    if lower_bound is None:
        lower_bound = np.min(img)
    if upper_bound is None:
        upper_bound = np.max(img)
    if lower_bound >= upper_bound:
        raise ValueError(
            '"lower_bound" must be smaller than "upper_bound"')
    lut = np.concatenate([
        np.zeros(lower_bound, dtype=np.uint16),
        np.linspace(0, 255, upper_bound - lower_bound).astype(np.uint16),
        np.ones(2**16 - upper_bound, dtype=np.uint16) * 255
    ])
    return lut[img].astype(np.uint8)

for name in glob.glob('3DIMG*.h5'):
 write_geotif(name)


