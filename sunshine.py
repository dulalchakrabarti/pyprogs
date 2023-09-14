import urllib2
import re
response = urllib2.urlopen('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20190522/gfs_0p25_1hr_00z.ascii?sunsdsfc[0:120][474][308]')
html = response.read()
vals = html.split('\n')
a = []
b = []
c = []
d = []
for item in vals:
 arr = item.split(',')
 if len(arr) == 2:
  case = arr[0]
 elif len(arr)>2:
  if case == 'sunsdsfc':
   a.append(arr[1:])
  elif case == 'time':
   b.append(arr)
  elif case == 'lat':
   c.append(arr)
  elif case == 'lon':
   d.append(arr)
print len(a),len(b),len(c),len(d)
#for l,m,n,k in zip(a,b,c,d):
 #print l,m,n,k

'''
wave = {}
fl = open('wave.csv','w')
fl.write('lat'+','+'lon'+','+'height'+'\n')
for item in vals:
 if item[:3] == '0.0':
  lat = item.split(',')
 elif item[:4] == '60.0':
  lon = item.split(',')
for item in vals:
 if item[:3] == '[0]':
  ht = item.split(',')
  wv = ht[1:]
  lat_ = re.findall(r'\d+', ht[0])
  for idx in range(len(lon)):
   fl.write(lat_[1]+','+lon[idx]+','+wv[idx]+'\n')
fl.close() 
'''
