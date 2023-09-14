import math
import numpy as np
from pydap.client import open_url
dataset=open_url("http://monsoondata.org:9090/dods/gfs0p25/gfs.2015102900")
ps = dataset['ps']
rh = rh2m[0,350:549,0:519]
lat = pres.lat[:]
lon = pres.lon[:]
ps_data = pres.array[:]
fl = open('/home/dulal/insat/pres.csv','w')
count = 0
for lat_idx in range(len(lat)):
 for lon_idx in range(len(lon)):
  if not(count % 50):
   pressure = ps_data[0][lat_idx][lon_idx]/100.0
   pressure = round(pressure)
   fl.write(str(lat[lat_idx])+','+str(lon[lon_idx])+','+str(pressure)+','+'\n')
  count = count + 1
fl.close() 
