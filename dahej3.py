import requests
import re,math

url = 'http://nomads.ncep.noaa.gov:80/dods/wave/gfswave/20240124/gfswave.global.0p16_00z.ascii?htsgwsfc[0:128][220][435]'
html = requests.get(url).text
vals = html.split('\n')
for item in vals:
 if len(item)>0:
  item = item.split(',')
  print(item[:5])
'''
wave = {}
fl = open('wave.csv','w')
fl.write('lat'+','+'lon'+','+'height'+'\n')
for item in vals:
 #item = item.decode('utf-8')
 #print(item)
 if item[:3] == '0.0':
  lat = item.split(',')
 elif item[:4] == '50.0':
  lon = item.split(',')
for item in vals:
 #item = item.decode('utf-8')
 if item[:3] == '[0]':
  ht = item.split(',')
  wv = ht[1:]
  #print(ht[0],wv)
  lat_=ht[0].split('[')
  lat_=lat_[3].split(']')
  lat_ = lat_[0]
  #print(lat_)
  for idx in range(len(lon)):
   fl.write(lat_+','+lon[idx]+','+str(int(math.ceil(float(wv[idx]))))+'\n')
fl.close() 
'''

