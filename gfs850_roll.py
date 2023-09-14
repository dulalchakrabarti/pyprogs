import requests
import math
import matplotlib.pyplot as plt
import numpy as np
u850 = []
#url = 'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20221022/gfs_0p25_1hr_18z.ascii?ugrdprs[0][5][360:520][160:480]'
url = 'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20221208/gfs_0p25_1hr_06z.ascii?ugrdprs[0][5][392:404][330:346]'
html = requests.get(url).text
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 #print(item,len(item))
 if len(item) == 18:
  u850.append([float(x) for x in item[1:]])
 elif len(item) == 13:
  lat = [float(x) for x in item]
 elif len(item) == 17:
  lon = [float(x) for x in item]
v850 = []
url = 'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20221208/gfs_0p25_1hr_06z.ascii?ugrdprs[0][5][392:404][330:346]'
html = requests.get(url).text
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 if len(item) == 18:
  v850.append([float(x) for x in item[1:]])
w850=[]
d850=[]
for idx in range(len(u850)):
 #print(len(u850),len(v850))
 c = map(lambda x,y:(math.sqrt(x*x+y*y),((270 - (math.atan2(y,x)/3.14)*180))%360),u850[idx],v850[idx])
 w1 = []
 d1 = []
 for item in c:
  w1.append(round(float(item[0]),1))
  d1.append(round(float(item[1]),1))
 w850.append(w1)
 d850.append(d1)
fl = open('850_roll.csv','w')
fl.write('lat'+','+'lon'+','+'ws'+','+'wd'+'\n')
for i in range(len(lat)):
 for j in range(len(lon)):
  if i%2 == 0 and j % 2 == 0:
   fl.write(str(lat[i])+','+str(lon[j])+','+str(w850[i][j] * 2)+','+str(d850[i][j])+'\n')
fl.close()
