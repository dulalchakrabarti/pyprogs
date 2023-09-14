#lat[360:520]lon[200:480]
import urllib2
import math
import matplotlib.pyplot as plt
import numpy as np
u850 = []
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20201204/gfs_0p25_1hr_06z.ascii?ugrdprs[0][17][360:520][200:480]')
html = response.read()
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 #print item,len(item)
 if len(item) == 282:
  u850.append([float(x) for x in item[1:]])
 elif len(item) == 161:
  lat = [float(x) for x in item]
 elif len(item) == 281:
  lon = [float(x) for x in item]
v850 = []
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20201204/gfs_0p25_1hr_06z.ascii?vgrdprs[0][17][360:520][200:480]')
html = response.read()
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 if len(item) == 282:
  v850.append([float(x) for x in item[1:]])
w850=[]
d850=[]
for idx in range(len(u850)):
 c = map(lambda x,y:(math.sqrt(x*x+y*y),((270 - (math.atan2(y,x)/3.14)*180))%360),u850[idx],v850[idx])
 w1 = []
 d1 = []
 for item in c:
  w1.append(round(float(item[0]),1))
  d1.append(round(float(item[1]),1))
 w850.append(w1)
 d850.append(d1)
fl = open('250.csv','w')
fl.write('lat'+','+'lon'+','+'ws'+','+'wd'+'\n')
for i in range(len(lat)):
 for j in range(len(lon)):
  if i%4 == 0 and j % 4 == 0:
   fl.write(str(lat[i])+','+str(lon[j])+','+str(w850[i][j] * 2)+','+str(d850[i][j])+'\n')
fl.close()
