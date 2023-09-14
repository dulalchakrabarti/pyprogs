import os
import glob
import http
import numpy as np
import time
import requests
import json
def stamp(strs):
    '''
    '''
    stm = strs
    dt = stm[:-2].replace('T', ' ')
    tm = dt
    return(tm)
seconds1 = time.time()
date1 = input('Start date(2018-03-29)?')
date1_ = date1.split('-')
time1 = '00:00:00.000'
time2 = '23:30:00.000'
txt = date1+'T00:00:00.000Z'+','+ date1+'T00:30:00.000Z'+','+\
date1+'T01:00:00.000Z'+','+ date1+'T01:30:00.000Z'+','+\
date1+'T02:00:00.000Z'+','+ date1+'T02:30:00.000Z'+','+\
date1+'T03:00:00.000Z'+','+ date1+'T03:30:00.000Z'+','+\
date1+'T04:00:00.000Z'+','+ date1+'T04:30:00.000Z'+','+\
date1+'T05:00:00.000Z'+','+ date1+'T05:30:00.000Z'+','+\
date1+'T06:00:00.000Z'+','+ date1+'T06:30:00.000Z'+','+\
date1+'T07:00:00.000Z'+','+ date1+'T07:30:00.000Z'+','+\
date1+'T08:00:00.000Z'+','+ date1+'T08:30:00.000Z'+','+\
date1+'T09:00:00.000Z'+','+ date1+'T09:30:00.000Z'+','+\
date1+'T10:00:00.000Z'+','+ date1+'T10:30:00.000Z'+','+\
date1+'T11:00:00.000Z'+','+ date1+'T11:30:00.000Z'+','+\
date1+'T12:00:00.000Z'+','+ date1+'T12:30:00.000Z'+','+\
date1+'T13:00:00.000Z'+','+ date1+'T13:30:00.000Z'+','+\
date1+'T14:00:00.000Z'+','+ date1+'T14:30:00.000Z'+','+\
date1+'T15:00:00.000Z'+','+ date1+'T15:30:00.000Z'+','+\
date1+'T16:00:00.000Z'+','+ date1+'T16:30:00.000Z'+','+\
date1+'T17:00:00.000Z'+','+ date1+'T17:30:00.000Z'+','+\
date1+'T18:00:00.000Z'+','+ date1+'T18:30:00.000Z'+','+\
date1+'T19:00:00.000Z'+','+ date1+'T19:30:00.000Z'+','+\
date1+'T20:00:00.000Z'+','+ date1+'T20:30:00.000Z'+','+\
date1+'T21:00:00.000Z'+','+ date1+'T21:30:00.000Z'+','+\
date1+'T22:00:00.000Z'+','+ date1+'T22:30:00.000Z'+','+\
date1+'T23:00:00.000Z'+','+ date1+'T23:30:00.000Z'
tskey = txt.split(',')
ts = {}
for item in tskey:
 ts[item] = ''
def count_out_ir1(lo, la):
    '''
    '''
    ser = []
    lo = float(lo)
    la = float(la)
    dlon = 15.908203125
    dlat = 12.919921875
    lllo = lo - dlon
    llla = la - dlat
    urlo = lo + dlon
    urla = la + dlat
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=362&J=294&TIME="+date1+"T"+time1+"Z/"+date1+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3DIMG_L1B_STD4/IMG_TIR1&LAYERS=3DIMG_L1B_STD4/IMG_TIR1&FEATURE_COUNT=1&WIDTH=724&HEIGHT=588"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     lo_ = str(data['domain']['axes']['x']['values'][0])
     la_ = str(data['domain']['axes']['y']['values'][0])
     sat ='D'
     dval = data['ranges']['IMG_TIR1']['values']
     dtime = data['domain']['axes']['t']['values']
     keyid = str(lo)+'_'+str(la)+'_'+sat
     ser.append(keyid)
     ser.append(dtime)
     ser.append(dval)
    except requests.exceptions.ConnectionError:
     print('D-Timed out!!')
    return ser
gl = open(date1_[2]+date1_[1]+date1_[0]+'ts_ir1.csv','w')
files = glob.glob('*V*.csv')
loc = {}
count = 0
for item in files:
 if len(item) > 20 and item[9:13] == '2022':
  lst = item.split('-')
  lat = lst[2]
  lon = lst[3].split('.')
  lon =lon[0]+'.'+lon[1]
  loc[lst[0]] = lat+','+lon
keylist =loc.keys()
sorted(keylist)
for key in keylist:
  rad = loc[key].split(',')
  #print(key,rad)
  lat = rad[0]
  lon = rad[1]
  buf = count_out_ir1(lon,lat)
  if len(buf) != 6:
   buf = count_out_ir1(lon,lat)
  else:
   dts = buf[1:3]
   tmd = dts[0]
   vld = dts[1]
   for i,j in zip(tmd,vld):
    if j == None or j == '':
     tmd.remove(i)
     vld.remove(j)
   vldf = [float(x) for x in vld]
   vldfmx = max(vldf)
   vldfmn = min(vldf)
   vldfnorm = [(j-vldfmn)/(vldfmx-vldfmn) for j in vldf]
   for num in range(len(tmd)):
    ts[tmd[num]] = vldfnorm[num]
  klst = ts.copy().keys()
  sorted(klst)
  for key in klst:
   if ts[key] == '' or ts[key] == None:
    ts.pop(key)
   else:
    print(lon,lat,stamp(key),ts[key],rf)
    gl.write(str(lon)+','+str(lat)+','+stamp(key)+','+str(ts[key])+','+str(rf)+'\n')
  count+=1
print(klst)
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0,count)
gl.close()
