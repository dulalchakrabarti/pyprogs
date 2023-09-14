"""
Read LAI data from h5 files with following tile details
24 05 06 07
25 05 06 07 08
26 05 06 07 08
27    06 07
"""
import os
import glob
import h5py
import numpy as np
import pandas as pd
fl = open('lai.csv','w')
dlat = 10.0/2400
dlon = 10.0/2400
def get_all(name):
   dl.append(name)
dl = []
for item in glob.glob('VNP15A2H*.h5'):
 f = h5py.File(item,'r')
 f.visit(get_all)
 name = dl[-4]
 data = f[name]
 row,col = data.shape
 word = item.split('.')
 lon = int(word[2][1:3])
 lat = int(word[2][4:])
 lonc = lon*10 - 180
 latc = 90 -lat*10
 print 'processing...',item
 for i in range(0,row,100):
  lat = latc - i*dlat
  lat = round(lat,4)
  for j in range(0,col,100):
   lon = lonc + j*dlon
   lon = round(lon,4)
   print lat, lon, round(data[i,j]*0.1,2)
   fl.write(str(lat)+','+str(lon)+','+str(round(data[i,j]*0.1,2))+'\n')
  lon = lonc
 f.close()

