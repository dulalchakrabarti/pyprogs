import math
import numpy as np
from pydap.client import open_url
dataset=open_url("https://disc2.nascom.nasa.gov/dods/TRMM_3B42_Daily_7")
r = dataset['pr']
rain=r[7071,240:379,210:489]
lat = rain.lat[:]
lon = rain.lon[:]
r_data = rain.array[:]
fl = open('/home/dulal/insat/trmm.csv','w')
count = 0
for lat_idx in range(len(lat)):
 for lon_idx in range(len(lon)):
  if not(count % 50):
   rainfall = r_data[0][lat_idx][lon_idx]
   fl.write(str(lat[lat_idx])+','+str(lon[lon_idx])+','+str(rainfall)+'\n')
  count = count + 1
fl.close()

