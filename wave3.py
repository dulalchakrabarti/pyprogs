import math
import numpy as np
from netCDF4 import Dataset
import pandas as pd
opendap_url = 'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20180424/gfs_0p25_1hr_00z'
DATAFIELD_NAME = ['gustsfc']
nc = Dataset(opendap_url)
lat2 = 444/4 - 90
lon2 = 72
for item in DATAFIELD_NAME:
 #fl = open(item+'.csv','w')
 print '---------------',item,'---------------'
 data = nc.variables[item][0:121:3,444,286]
 for item in data:
  print lat2,lon2,item
'''
wave = wh[0,78:118,48:80]
lat = wave.lat[:]
lon = wave.lon[:]
wave_data = wave.array[:]
fl = open('/home/dulal/sat/wave.csv','w')
count = 0
for lat_idx in range(len(lat)):
 for lon_idx in range(len(lon)):
  if not(count % 5):
   ht = wave_data[0][lat_idx][lon_idx]
   ht = round(ht)
   fl.write(str(lat[lat_idx])+','+str(lon[lon_idx])+','+str(ht)+'\n')
  count = count + 1
fl.close() 
'''
