"""
Copyright (C) 2017 The HDF Group

This example code illustrates how to access and visualize a SMAP L4 HDF5 file 
in Python.

If you have any questions, suggestions, or comments on this example, please use
the HDF-EOS Forum (http://hdfeos.org/forums).  If you would like to see an
example of any other NASA HDF/HDF-EOS data product that is not listed in the
HDF-EOS Comprehensive Examples page (http://hdfeos.org/zoo), feel free to
contact us at eoshelp@hdfgroup.org or post it at the HDF-EOS Forum
(http://hdfeos.org/forums).

Usage:  save this script and run

    python SMAP_L4_SM_gph_20170803T193000_Vv3030_001.h5.py

The HDF5 file must be in your current working directory.

Tested under: Python 2.7.13 :: Anaconda custom (x86_64)
Last updated: 2017-08-08
"""

import os

import h5py
import numpy as np

FILE_NAME = '3DIMG_01NOV2018_0600_L1C_ASIA_MER.h5'
fl = open('insat.csv','w')    
with h5py.File(FILE_NAME, mode='r') as f:
    
    name = '/IMG_TIR1'
    data = f[name][:]
    units = f[name].attrs['radiance_units']
    longname = f[name].attrs['long_name']
    _FillValue = f[name].attrs['_FillValue']
    data = np.ma.masked_where(np.isnan(data), data)
    
    # Get the geolocation data
    lat = f['/Y'][:]
    lon = f['/X'][:]
    name1 = '/Projection_Information'
    datap = f[name1][:]
    ul = f[name1].attrs['upper_left_lat_lon(degrees)']
    lr = f[name1].attrs['lower_right_lat_lon(degrees)']
i,j,k = data.shape
for x in range(i):
 for y in range(j):
  for z in range(k):
   print lat[y],lon[z],data[x][y][z]
'''
for i in range(len(data[0][0])):
 for j in range(len(data[0])):
   print latitude[i],longitude[j],data[i][j]
   fl.writelines(str(latitude[i])+','+str(longitude[j])+','+str(data[i][j])+'\n')
'''

