import http
import numpy as np
import time
import requests
import json
seconds1 = time.time()
gl = open('testir1.csv', 'a+')
def count_out(lon,lat):
    '''
    '''
    dx = 0.1
    dy = 0.1
    lo_st_ = float(lon)-dx/2
    lo_st = str(lo_st_)
    lo_end_ = float(lon) + dx/2
    lo_end = str(lo_end_)
    la_st_ = float(lat) - dy/4
    la_st = str(la_st_)
    la_end_ = float(lat) + dy/4
    la_end = str(la_end_)
    out=[]
    count = 0
    for lati in np.arange(la_st_,la_end_,dy/64):
     lati_ = str(lati)
     try:
      r1 = requests.get("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTransect&LAYERS=3DIMG_L1B_STD4/IMG_TIR1&CRS=CRS:84&LINESTRING="+lo_st+"%20"+lati_+","+lo_end+"%20"+lati_+",&TIME=2022-02-06T12:00:00&FORMAT=text/json")
      resp = r1.text
      data = json.loads(resp)
      lat = data['lat'][19:47]
      lon = data['lon'][19:47]
      vals = data['IMG_TIR1']['values'][19:47]
      #for l,m,n in zip(lat,lon,vals):
       #gl.write(str(l)+','+str(m)+','+str(n)+'\n')
      out.extend(vals)
      count+=1
      if count > 27:
       return out
      #print(count)
     except requests.exceptions.ConnectionError:
      print('Timed out!!')
      
stn = {}
lines = [line.rstrip('\n') for line in open('obs_train_class.csv')]
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
 print(count)
 buf = count_out(lon,lat)
 print(lat, lon, cls, len(buf))
 val = ','.join(str(x) for x in buf)
 print('.................................')
 count+=1
 gl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
 #if count > 100:
  #seconds2 = time.time()
  #print('elapsed minutes....',(seconds2-seconds1)/60.0)
  #exit()
gl.close()
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)

