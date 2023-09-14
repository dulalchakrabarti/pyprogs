import http
import numpy as np
import time
import requests
import json
seconds1 = time.time()
date = input('Input date(2018-03-29)?')
dat = date.split('-')
fl = open(dat[2]+dat[1]+dat[0]+'rain.csv')
gl = open('areair1.csv', 'a+')
def count_out(lon,lat,tm,dr):
    '''
    '''
    print(tm,dr,lon,lat)
    dx = 0.5
    dy = 0.5
    lo_st = float(lon)-1
    lo_end = float(lon)+1
    la_st = float(lat)-1
    la_end = float(lat)+1
    for lati in np.arange(la_st,la_end,dy):
     for longi in np.arange(lo_st,lo_end,dx):
      try:
       txt = "https://rapid.imd.gov.in/r2wms/wms?LAYERS=3"+dr+"IMG_L1B_STD4/IMG_TIR1&REQUEST=GetPolyStats&TIME="+date+"T"+tm[2:4]+":"+tm[4:]+":00&polygon="+str(longi)+","+str(lati)+";"+str(longi+dx)+","+str(lati)+";"+str(longi+dx)+","+str(lati+dy)+";"+str(longi)+","+str(lati+dy)+";"+str(longi)+","+str(lati)+"&FORMAT=text/json"
       print(txt)
       r1 = requests.get(txt)
       resp = r1.text
       print(resp)
       data = json.loads(resp)
       print(data)
      except requests.exceptions.ConnectionError:
       print('Timed out!!')
count = 0
lines = [line.rstrip('\n') for line in fl]
for inp in lines:
 lst = inp.split(',')
 lat = lst[0]
 lon = lst[1]
 tm = lst[2]
 dr = tm[4:]
 if dr == '15' or dr == '45':
  dr = 'R'
 else:
  dr = 'D'
 buf = count_out(lon,lat,tm,dr)
 print('.................................')
 count+=1
 #gl.write(str(lat)+','+str(lon)+','+str(cls)+','+val+'\n')
 #if count > 0:
  #seconds2 = time.time()
  #print('elapsed minutes....',(seconds2-seconds1)/60.0)
  #exit()
#gl.close()
print(count)
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)
