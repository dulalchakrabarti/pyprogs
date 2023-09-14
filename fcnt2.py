import urllib.request
import http
import numpy as np
import time
seconds1 = time.time()
gl = open('cloudir1.txt', 'w')
def count_out(lon,lat):
    '''
    '''
    dx = 0.1
    dy = 0.1
    lo_st_ = float(lon)-dx/2
    lo_st = str(lo_st_)
    lo_end_ = float(lon) + dx/2
    lo_end = str(lo_end_)
    la_st_ = float(lat) - dy/2
    la_st = str(la_st_)
    la_end_ = float(lat) + dy/2
    la_end = str(la_end_)
    out=[]
    for lati in np.arange(la_st_,la_end_,dy/4):
     lati_ = str(lati)
     try:
      f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTransect&LAYERS=3DIMG_L1B_STD4/IMG_TIR1&CRS=CRS:84&LINESTRING="+lo_st+"%20"+lati_+","+lo_end+"%20"+lati_+",&TIME=2021-11-26T12:00:00&FORMAT=text/json")
      txt1 = f1.read()
      syn = txt1.split(b'\n')
      for item in syn:
       txt = item.decode('utf-8')
       #print(txt)
       buf = txt.split('{')
       dist = buf[1].split('"dist":[')
       lon = buf[1].split('"lon":[')
       lat = buf[1].split('"lat":[')
       d = dist[1].split(']')
       lo = lon[1].split(']')
       la = lat[1].split(']')
       val = buf[2].split('"unit":"","values":[')
       dst = d[0].split(',')
       lon = lo[0].split(',')
       lat = la[0].split(',')
       cnt = val[1].split(']}}')
       vals = cnt[0].split(',')
       out.extend(vals)
     except http.client.HTTPException as e:
      print(e)
      f1.close()
    return(out)
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
 print(lat, lon, cls,len(val))
 print('.................................')
 gl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
gl.close()
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)

