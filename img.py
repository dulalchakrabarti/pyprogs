import requests
import json
import http
import numpy as np
import time
seconds1 = time.time()
gl = open('cloudmir.csv', 'w')
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
    out=[]
    count = 0
    for lati in np.arange(la_st_,la_end_,dy/4):
     lati_ = str(lati)
     try:
      r1 = requests.get("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTransect&LAYERS=3RIMG_L1B_STD4/IMG_MIR&CRS=CRS:84&LINESTRING="+lo_st+"%20"+lati_+","+lo_end+"%20"+lati_+",&TIME=2022-01-21T00:15:00&FORMAT=text/json")
      resp = r1.text
      data = json.loads(resp)
      lat = data['lat'][:9]
      lon = data['lon'][:9]
      vals = data['IMG_MIR']['values'][:9]
      #for l,m,n in zip(lat,lon,vals):
       #gl.write(str(l)+','+str(m)+','+str(n)+'\n')
      count+=1
      out.extend(vals)
      #print(count)
     except http.client.HTTPException as e:
      print('--------------',e)
    return out
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
 val = ','.join(str(x) for x in buf)
 print(lat, lon, cls,val[:5])
 print('.................................')
 count+=1
 #gl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
 #if count > 1:
  #seconds2 = time.time()
  #print('elapsed minutes....',(seconds2-seconds1)/60.0)
  #exit()
gl.close()
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)
