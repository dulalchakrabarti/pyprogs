import urllib2
import math
import matplotlib.pyplot as plt
import numpy as np
u850 = []
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20190923/gfs_0p25_1hr_00z.ascii?ugrdprs[0][5][360:520][240:480]')
html = response.read()
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 if len(item) == 242:
  u850.append([float(x) for x in item[1:]])
v850 = []
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20190923/gfs_0p25_1hr_00z.ascii?vgrdprs[0][5][360:520][240:480]')
html = response.read()
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 if len(item) == 242:
  v850.append([float(x) for x in item[1:]])
u500 = []
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20190923/gfs_0p25_1hr_00z.ascii?ugrdprs[0][12][360:520][240:480]')
html = response.read()
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 if len(item) == 242:
  u500.append([float(x) for x in item[1:]])
v500 = []
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20190923/gfs_0p25_1hr_00z.ascii?vgrdprs[0][12][360:520][240:480]')
html = response.read()
vals = html.split('\n')
for item in vals:
 item = item.split(',')
 if len(item) == 242:
  v500.append([float(x) for x in item[1:]])
 elif len(item) == 161:
  lat = [float(x) for x in item]
 elif len(item) == 241:
  lon = [float(x) for x in item]
w850=[]
d850=[]
w500=[]
d500=[]
for idx in range(len(u500)):
 c = map(lambda x,y,k,l:(math.sqrt(x*x+y*y),(math.atan2(y,x)/3.14)*180,math.sqrt(k*k+l*l),(math.atan2(l,k)/3.14)*180),u850[idx],v850[idx],u500[idx],v500[idx])
 w1 = []
 d1 = []
 w2 = []
 d2 = []
 for item in c:
  w1.append(round(float(item[0]),1))
  d1.append(round(float(item[1]),1))
  w2.append(round(float(item[2]),1))
  d2.append(round(float(item[3]),1))
 w850.append(w1)
 d850.append(d1)
 w500.append(w2)
 d500.append(d2)
print w850
print d850
print w500
print d500

