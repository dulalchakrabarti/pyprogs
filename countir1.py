import urllib.request
import http
import numpy as np
import time
seconds1 = time.time()
dx = 0.0006975
dy = 0.0006975
lon = 80
lat = 20
lo_st_ = float(lon)-32*dx
lo_st = str(lo_st_)
lo_end_ = float(lon) + 32*dx
lo_end = str(lo_end_)
la_st_ = float(lat) - 32*dy
la_st = str(la_st_)
la_end_ = float(lat) + 32*dy
la_end = str(la_end_)
for lati in np.arange(la_st_,la_end_,dy):
 lati_ = str(lati)
 resp = []
 try:
  f1 = urllib.request.urlopen("https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTransect&LAYERS=3DIMG_L1B_STD4/IMG_TIR1&CRS=CRS:84&LINESTRING="+lo_st+"%20"+lati_+","+lo_end+"%20"+lati_+",&TIME=2021-10-21T13:30:00&FORMAT=text/json")
  txt1 = f1.read()
  resp.append(txt1)
  print(lati_)
  f1.close()
 except http.client.HTTPException as e:
  print(e)
seconds2 = time.time()
print((seconds2-seconds1)/60.0)

