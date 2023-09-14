import urllib.request
import http
import numpy as np
import time
import requests
import json
seconds1 = time.time()
def count_out(lon,lat):
 '''
 '''
 dx = 0.1
 dy = 0.1
 lo_st_ = float(lon)-dx
 lo_st = str(lo_st_)
 lo_end_ = float(lon) + dx
 lo_end = str(lo_end_)
 la_st_ = float(lat) - dy
 la_st = str(la_st_)
 la_end_ = float(lat) + dy
 la_end = str(la_end_)
 lati_ = str(float(lat)+dy/32)
 r1 = requests.get("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTransect&LAYERS=3DIMG_L1B_STD4/IMG_TIR1&CRS=CRS:84&LINESTRING="+lo_st+"%20"+lati_+","+lo_end+"%20"+lati_+",&TIME=2022-01-04T12:00:00&FORMAT=text/json",timeout=None)
 resp = r1.text
 data = json.loads(resp)
 print(data['lat'])
 print(data['lon'])
 print(data['IMG_TIR1']['values'])
stn = {}
lines = [line.rstrip('\n') for line in open('class.csv')]
for inp in lines:
 lst = inp.split(',')
 stn[lst[0]] = lst[1:]
dec = {}
for key,val in stn.items():
 city = key
 city1 = city+'_'
 city2 = city+'__'
 city3 = city+'___'
 if city in dec:
  city = city+'_'
 elif city1 in dec:
  city = city1+'_'
 elif city2 in dec:
  city = city2+'_'
 elif city3 in dec:
  city = city3+'_'
 dec[city] = []
 lat = val[1]
 dec[city].append(lat)
 lon = val[2]
 dec[city].append(lon)
 cls = val[3]
 dec[city].append(cls)
keylist = dec.keys()
sorted(keylist)
count=0
for key in keylist:
 lat = dec[key][0]
 lon = dec[key][1]
 cls = dec[key][2]
 buf = count_out(lon,lat)

