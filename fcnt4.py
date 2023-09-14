import urllib.request
import http
import numpy as np
import time
seconds1 = time.time()
#deltalon = 0.1
#deltalat = 0.05
def count_out(lon,lat):
    '''
    '''
    lonmin = float(lon)-0.05
    lonmax = float(lon)+0.05
    latmin = float(lat)-0.025
    latmax = float(lat)+0.025
    coord = [
    str(lonmin)+'%20'+str(latmin)+','+str(lonmax)+'%20'+str(latmin)
    ]
    for item in coord:
     txt = str(item)
     try:
      f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTransect&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&CRS=CRS:84&LINESTRING="+txt+",&TIME=2021-10-24T02:45:00&FORMAT=text/json")
      txt1 = f1.read()
      syn = txt1.split(b'\n')
      for item in syn:
       txt = item.decode('utf-8')
       buf = txt.split('{')
       dist = buf[1].split('"dist":[')
       lon = buf[1].split('"lon":[')
       lat = buf[1].split('"lat":[')
       d = dist[1].split(']')
       lo = lon[1].split(']')
       la = lat[1].split(']')
       val = buf[2].split('"unit":"","values":[')
       dst = d[0].split(',')
       cnt = val[1].split(']}}')
       vals = cnt[0].split(',')
       print(dst,lon,lat,vals)
      f1.close()
      return(vals)
     except http.client.HTTPException as e:
      print(e)
'''
coord = [
'82.705078125%2016.083984375000004,82.79296875%2016.040039062500004',
'82.705078125%2016.040039062500004,82.79296875%2016.083984375000004',
'82.749023438%2016.040039062500004,82.749023438%2016.083984375000004',
'82.705078125%2016.062011719,82.79296875%2016.062011719',
'82.705078125%2016.083984375000004,82.705078125%2016.040039062500004',
'82.705078125%2016.040039062500004,82.79296875%2016.040039062500004',
'82.705078125%2016.083984375000004,82.79296875%2016.083984375000004',
'82.705078125%2016.083984375000004,82.705078125%2016.040039062500004'
]
for item in coord:
 txt = str(item)
 try:
  f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTransect&LAYERS=3RIMG_L1B_STD4/IMG_TIR1&CRS=CRS:84&LINESTRING="+txt+",&TIME=2021-10-24T02:45:00&FORMAT=text/json")
  txt1 = f1.read()
  syn = txt1.split(b'\n')
  for item in syn:
   #print(item)
   txt = item.decode('utf-8')
   buf = txt.split('{')
   dist = buf[1].split('"dist":[')
   lon = buf[1].split('"lon":[')
   lat = buf[1].split('"lat":[')
   d = dist[1].split(']')
   lo = lon[1].split(']')
   la = lat[1].split(']')
   val = buf[2].split('"unit":"","values":[')
   dst = d[0].split(',')
   v1 = [float(x[0])-float(x[1]) for x in zip(dst[1:],dst[:-1])]
   print(v1)
   lon = lo[0].split(',')
   v2 = [float(x[0])-float(x[1]) for x in zip(lon[1:],lon[:-1])]
   print(v2)
   lat = la[0].split(',')
   v3 = [float(x[0])-float(x[1]) for x in zip(lat[1:],lat[:-1])]
   print(v3)
   cnt = val[1].split(']}}')
   vals = cnt[0].split(',')
   print(dst,lon,lat,vals)
  f1.close()
 except http.client.HTTPException as e:
  print(e)
'''
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
#print(dec)
keylist = dec.keys()
sorted(keylist)
#print(len(keylist))
count=0
for key in keylist:
 lat = dec[key][0]
 lon = dec[key][1]
 cls = dec[key][2]
 print(count_out(lat,lon))
'''
 buf = count_out(lon,lat)
 val = ','.join(str(x) for x in buf)
 print(lat, lon, cls, val[:11])
 print('.................................')
 gl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
gl.close()
'''
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)

