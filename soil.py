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

FILE_NAME = 'SMAP_L3_SM_P_E_20181106_R16010_001.h5'
fl = open('smap.csv','w')    
with h5py.File(FILE_NAME, mode='r') as f:
    
    name = '/Soil_Moisture_Retrieval_Data_AM/soil_moisture'
    data = f[name][:]
    units = f[name].attrs['units']
    longname = f[name].attrs['long_name']
    _FillValue = f[name].attrs['_FillValue']
    valid_max = f[name].attrs['valid_max']
    valid_min = f[name].attrs['valid_min']        
    invalid = np.logical_or(data > valid_max,
                            data < valid_min)
    invalid = np.logical_or(invalid, data == _FillValue)
    data[invalid] = np.nan
    data = np.ma.masked_where(np.isnan(data), data)
    
    # Get the geolocation data
    latitude = f['/Soil_Moisture_Retrieval_Data_AM/latitude'][:]
    longitude = f['/Soil_Moisture_Retrieval_Data_AM/longitude'][:]
for i in range(len(data)):
 for j in range(len(data[0])):
  if latitude[i][j]>=0 and latitude[i][j]<=40 and longitude[i][j]>=60 and longitude[i][j]<=100 and data[i][j]!='--':
   print latitude[i][j],longitude[i][j],data[i][j]
   fl.writelines(str(latitude[i][j])+','+str(longitude[i][j])+','+str(data[i][j])+'\n')

