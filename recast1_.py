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
time2 = '23:45:00.000'
txt = date1+'T00:00:00.000Z'+','+date1+'T00:15:00.000Z'+','+ date1+'T00:30:00.000Z'+','+ date1+'T00:45:00.000Z'+','+\
date1+'T01:00:00.000Z'+','+date1+'T01:15:00.000Z'+','+ date1+'T01:30:00.000Z'+','+ date1+'T01:45:00.000Z'+','+\
date1+'T02:00:00.000Z'+','+date1+'T02:15:00.000Z'+','+ date1+'T02:30:00.000Z'+','+ date1+'T02:45:00.000Z'+','+\
date1+'T03:00:00.000Z'+','+date1+'T03:15:00.000Z'+','+ date1+'T03:30:00.000Z'+','+ date1+'T03:45:00.000Z'+','+\
date1+'T04:00:00.000Z'+','+date1+'T04:15:00.000Z'+','+ date1+'T04:30:00.000Z'+','+ date1+'T04:45:00.000Z'+','+\
date1+'T05:00:00.000Z'+','+date1+'T05:15:00.000Z'+','+ date1+'T05:30:00.000Z'+','+ date1+'T05:45:00.000Z'+','+\
date1+'T06:00:00.000Z'+','+date1+'T06:15:00.000Z'+','+ date1+'T06:30:00.000Z'+','+ date1+'T06:45:00.000Z'+','+\
date1+'T07:00:00.000Z'+','+date1+'T07:15:00.000Z'+','+ date1+'T07:30:00.000Z'+','+ date1+'T07:45:00.000Z'+','+\
date1+'T08:00:00.000Z'+','+date1+'T08:15:00.000Z'+','+ date1+'T08:30:00.000Z'+','+ date1+'T08:45:00.000Z'+','+\
date1+'T09:00:00.000Z'+','+date1+'T09:15:00.000Z'+','+ date1+'T09:30:00.000Z'+','+ date1+'T09:45:00.000Z'+','+\
date1+'T10:00:00.000Z'+','+date1+'T10:15:00.000Z'+','+ date1+'T10:30:00.000Z'+','+ date1+'T10:45:00.000Z'+','+\
date1+'T11:00:00.000Z'+','+date1+'T11:15:00.000Z'+','+ date1+'T11:30:00.000Z'+','+ date1+'T11:45:00.000Z'+','+\
date1+'T12:00:00.000Z'+','+date1+'T12:15:00.000Z'+','+ date1+'T12:30:00.000Z'+','+ date1+'T12:45:00.000Z'+','+\
date1+'T13:00:00.000Z'+','+date1+'T13:15:00.000Z'+','+ date1+'T13:30:00.000Z'+','+ date1+'T13:45:00.000Z'+','+\
date1+'T14:00:00.000Z'+','+date1+'T14:15:00.000Z'+','+ date1+'T14:30:00.000Z'+','+ date1+'T14:45:00.000Z'+','+\
date1+'T15:00:00.000Z'+','+date1+'T15:15:00.000Z'+','+ date1+'T15:30:00.000Z'+','+ date1+'T15:45:00.000Z'+','+\
date1+'T16:00:00.000Z'+','+date1+'T16:15:00.000Z'+','+ date1+'T16:30:00.000Z'+','+ date1+'T16:45:00.000Z'+','+\
date1+'T17:00:00.000Z'+','+date1+'T17:15:00.000Z'+','+ date1+'T17:30:00.000Z'+','+ date1+'T17:45:00.000Z'+','+\
date1+'T18:00:00.000Z'+','+date1+'T18:15:00.000Z'+','+ date1+'T18:30:00.000Z'+','+ date1+'T18:45:00.000Z'+','+\
date1+'T19:00:00.000Z'+','+date1+'T19:15:00.000Z'+','+ date1+'T19:30:00.000Z'+','+ date1+'T19:45:00.000Z'+','+\
date1+'T20:00:00.000Z'+','+date1+'T20:15:00.000Z'+','+ date1+'T20:30:00.000Z'+','+ date1+'T20:45:00.000Z'+','+\
date1+'T21:00:00.000Z'+','+date1+'T21:15:00.000Z'+','+ date1+'T21:30:00.000Z'+','+ date1+'T21:45:00.000Z'+','+\
date1+'T22:00:00.000Z'+','+date1+'T22:15:00.000Z'+','+ date1+'T22:30:00.000Z'+','+ date1+'T22:45:00.000Z'+','+\
date1+'T23:00:00.000Z'+','+date1+'T23:15:00.000Z'+','+ date1+'T23:30:00.000Z'+','+ date1+'T23:45:00.000Z'
#print(txt)
tskey = txt.split(',')
ts = {}
for item in tskey:
 ts[item] = ''
def count_out_wv(lo, la):
    '''
    '''
    ser = []
    lo = float(lo)
    la = float(la)
    dlon = 28.4326
    dlat = 7.8662
    lllo = lo - dlon
    llla = la - dlat
    urlo = lo + dlon
    urla = la + dlat
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=720&J=178&TIME="+date1+"T"+time1+"Z/"+date1+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3DIMG_L1B_STD8/IMG_WV&LAYERS=3DIMG_L1B_STD8/IMG_WV&FEATURE_COUNT=1&WIDTH=1294&HEIGHT=358"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     lo_ = str(data['domain']['axes']['x']['values'][0])
     la_ = str(data['domain']['axes']['y']['values'][0])
     sat ='D'
     dval = data['ranges']['IMG_WV']['values']
     dtime = data['domain']['axes']['t']['values']
     keyid = str(lo)+'_'+str(la)+'_'+sat
     ser.append(keyid)
     ser.append(dtime)
     ser.append(dval)
    except requests.exceptions.ConnectionError:
     print('D-Timed out!!')
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=720&J=178&TIME="+date1+"T"+time1+"Z/"+date1+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD8/IMG_WV&LAYERS=3RIMG_L1B_STD8/IMG_WV&FEATURE_COUNT=1&WIDTH=1294&HEIGHT=358"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     lo_ = str(data['domain']['axes']['x']['values'][0])
     la_ = str(data['domain']['axes']['y']['values'][0])
     sat ='R'
     rval = data['ranges']['IMG_WV']['values']
     rtime = data['domain']['axes']['t']['values']
     keyid = str(lo)+'_'+str(la)+'_'+sat
     ser.append(keyid)
     ser.append(rtime)
     ser.append(rval)
    except requests.exceptions.ConnectionError:
     print('R-Timed out!!')
    return ser
fl = open(date1_[2]+date1_[1]+date1_[0]+'rain.csv')
gl = open(date1_[2]+date1_[1]+date1_[0]+'ts_wv.csv','w')
count = 0
d = {}
lines = [line.rstrip('\n') for line in fl]
for inp in lines:
 lst = inp.split(',')
 lat = lst[0]
 lon = lst[1]
 val = lat+'_'+lon
 d[val] = lst[-1]
keylist = d.keys()
sorted(keylist)
d_ = {}
for key in d.copy():
 lst = key.split('_')
 lat = lst[0]
 lon = lst[1]
 rf = d[key]
 buf = count_out_wv(lon,lat)
 if len(buf) != 6:
   buf = count_out_wv(lon,lat)
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
  vldfnorm = [(j/vldfmx) for j in vldf]
  for num in range(len(tmd)):
   ts[tmd[num]] = vldfnorm[num]
  rts = buf[4:6]
  tmr = rts[0]
  vlr = rts[1]
  for i,j in zip(tmr,vlr):
   if j == None or j == '':
    tmr.remove(i)
    vlr.remove(j)
  vlrf = [float(x) for x in vlr]
  vlrfmx = max(vlrf)
  vlrfnorm = [(j/vlrfmx) for j in vlrf]
  for num in range(len(tmr)):
   ts[tmr[num]] = vlrfnorm[num]
  klst = ts.copy().keys()
  sorted(klst)
  for key in klst:
   if ts[key] == '' or ts[key] == None:
    ts.pop(key)
   else:
    print(lon,lat,stamp(key),ts[key],rf)
    gl.write(str(lon)+','+str(lat)+','+stamp(key)+','+str(ts[key])+','+str(rf)+'\n')
  count+=1
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0,count)
gl.close()
fl.close()
print('Starting again for mir chaannel....')
txt = date1+'T00:00:00.000Z'+','+date1+'T00:15:00.000Z'+','+ date1+'T00:30:00.000Z'+','+ date1+'T00:45:00.000Z'+','+\
date1+'T01:00:00.000Z'+','+date1+'T01:15:00.000Z'+','+ date1+'T01:30:00.000Z'+','+ date1+'T01:45:00.000Z'+','+\
date1+'T02:00:00.000Z'+','+date1+'T02:15:00.000Z'+','+ date1+'T02:30:00.000Z'+','+ date1+'T02:45:00.000Z'+','+\
date1+'T03:00:00.000Z'+','+date1+'T03:15:00.000Z'+','+ date1+'T03:30:00.000Z'+','+ date1+'T03:45:00.000Z'+','+\
date1+'T04:00:00.000Z'+','+date1+'T04:15:00.000Z'+','+ date1+'T04:30:00.000Z'+','+ date1+'T04:45:00.000Z'+','+\
date1+'T05:00:00.000Z'+','+date1+'T05:15:00.000Z'+','+ date1+'T05:30:00.000Z'+','+ date1+'T05:45:00.000Z'+','+\
date1+'T06:00:00.000Z'+','+date1+'T06:15:00.000Z'+','+ date1+'T06:30:00.000Z'+','+ date1+'T06:45:00.000Z'+','+\
date1+'T07:00:00.000Z'+','+date1+'T07:15:00.000Z'+','+ date1+'T07:30:00.000Z'+','+ date1+'T07:45:00.000Z'+','+\
date1+'T08:00:00.000Z'+','+date1+'T08:15:00.000Z'+','+ date1+'T08:30:00.000Z'+','+ date1+'T08:45:00.000Z'+','+\
date1+'T09:00:00.000Z'+','+date1+'T09:15:00.000Z'+','+ date1+'T09:30:00.000Z'+','+ date1+'T09:45:00.000Z'+','+\
date1+'T10:00:00.000Z'+','+date1+'T10:15:00.000Z'+','+ date1+'T10:30:00.000Z'+','+ date1+'T10:45:00.000Z'+','+\
date1+'T11:00:00.000Z'+','+date1+'T11:15:00.000Z'+','+ date1+'T11:30:00.000Z'+','+ date1+'T11:45:00.000Z'+','+\
date1+'T12:00:00.000Z'+','+date1+'T12:15:00.000Z'+','+ date1+'T12:30:00.000Z'+','+ date1+'T12:45:00.000Z'+','+\
date1+'T13:00:00.000Z'+','+date1+'T13:15:00.000Z'+','+ date1+'T13:30:00.000Z'+','+ date1+'T13:45:00.000Z'+','+\
date1+'T14:00:00.000Z'+','+date1+'T14:15:00.000Z'+','+ date1+'T14:30:00.000Z'+','+ date1+'T14:45:00.000Z'+','+\
date1+'T15:00:00.000Z'+','+date1+'T15:15:00.000Z'+','+ date1+'T15:30:00.000Z'+','+ date1+'T15:45:00.000Z'+','+\
date1+'T16:00:00.000Z'+','+date1+'T16:15:00.000Z'+','+ date1+'T16:30:00.000Z'+','+ date1+'T16:45:00.000Z'+','+\
date1+'T17:00:00.000Z'+','+date1+'T17:15:00.000Z'+','+ date1+'T17:30:00.000Z'+','+ date1+'T17:45:00.000Z'+','+\
date1+'T18:00:00.000Z'+','+date1+'T18:15:00.000Z'+','+ date1+'T18:30:00.000Z'+','+ date1+'T18:45:00.000Z'+','+\
date1+'T19:00:00.000Z'+','+date1+'T19:15:00.000Z'+','+ date1+'T19:30:00.000Z'+','+ date1+'T19:45:00.000Z'+','+\
date1+'T20:00:00.000Z'+','+date1+'T20:15:00.000Z'+','+ date1+'T20:30:00.000Z'+','+ date1+'T20:45:00.000Z'+','+\
date1+'T21:00:00.000Z'+','+date1+'T21:15:00.000Z'+','+ date1+'T21:30:00.000Z'+','+ date1+'T21:45:00.000Z'+','+\
date1+'T22:00:00.000Z'+','+date1+'T22:15:00.000Z'+','+ date1+'T22:30:00.000Z'+','+ date1+'T22:45:00.000Z'+','+\
date1+'T23:00:00.000Z'+','+date1+'T23:15:00.000Z'+','+ date1+'T23:30:00.000Z'+','+ date1+'T23:45:00.000Z'
tskey = txt.split(',')
ts = {}
for item in tskey:
 ts[item] = ''
def count_out_mir(lo, la):
    '''
    '''
    ser = []
    lo = float(lo)
    la = float(la)
    dlon = 28.4326
    dlat = 7.8662
    lllo = lo - dlon
    llla = la - dlat
    urlo = lo + dlon
    urla = la + dlat
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=720&J=181&TIME="+date1+"T"+time1+"Z/"+date1+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3DIMG_L1B_STD4/IMG_MIR&LAYERS=3DIMG_L1B_STD4/IMG_MIR&FEATURE_COUNT=1&WIDTH=1294&HEIGHT=358"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     lo_ = str(data['domain']['axes']['x']['values'][0])
     la_ = str(data['domain']['axes']['y']['values'][0])
     sat ='D'
     dval = data['ranges']['IMG_MIR']['values']
     dtime = data['domain']['axes']['t']['values']
     keyid = str(lo)+'_'+str(la)+'_'+sat
     ser.append(keyid)
     ser.append(dtime)
     ser.append(dval)
    except requests.exceptions.ConnectionError:
     print('D-Timed out!!')
    try:
     txt = "https://rapid.imd.gov.in/r2wms/wms?&service=WMS&request=GetTimeseries&version=1.3.0&CRS=CRS:84&BBOX="+str(lllo)+","+str(llla)+","+str(urlo)+","+str(urla)+"&I=720&J=181&TIME="+date1+"T"+time1+"Z/"+date1+"T"+time2+"Z&INFO_FORMAT=text/json&ELEVATION=0&QUERY_LAYERS=3RIMG_L1B_STD4/IMG_MIR&LAYERS=3RIMG_L1B_STD4/IMG_MIR&FEATURE_COUNT=1&WIDTH=1294&HEIGHT=358"
     #print(txt)
     r1 = requests.get(txt)
     resp = r1.text
     #print(resp)
     data = json.loads(resp)
     #['type', 'title', 'domain', 'parameters', 'ranges']
     lo_ = str(data['domain']['axes']['x']['values'][0])
     la_ = str(data['domain']['axes']['y']['values'][0])
     sat ='R'
     rval = data['ranges']['IMG_MIR']['values']
     rtime = data['domain']['axes']['t']['values']
     keyid = str(lo)+'_'+str(la)+'_'+sat
     ser.append(keyid)
     ser.append(rtime)
     ser.append(rval)
    except requests.exceptions.ConnectionError:
     print('R-Timed out!!')
    return ser
fl = open(date1_[2]+date1_[1]+date1_[0]+'rain.csv')
gl = open(date1_[2]+date1_[1]+date1_[0]+'ts_mir.csv','w')
count = 0
d = {}
lines = [line.rstrip('\n') for line in fl]
for inp in lines:
 lst = inp.split(',')
 lat = lst[0]
 lon = lst[1]
 val = lat+'_'+lon
 d[val] = lst[-1]
keylist = d.keys()
sorted(keylist)
d_ = {}
for key in d.copy():
 lst = key.split('_')
 lat = lst[0]
 lon = lst[1]
 rf = d[key]
 buf = count_out_mir(lon,lat)
 if len(buf) != 6:
   buf = count_out_mir(lon,lat)
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
  rts = buf[4:6]
  tmr = rts[0]
  vlr = rts[1]
  for i,j in zip(tmr,vlr):
   if j == None or j == '':
    tmr.remove(i)
    vlr.remove(j)
  vlrf = [float(x) for x in vlr]
  vlrfmx = max(vlrf)
  vlrfnorm = [(j/vlrfmx) for j in vlrf]
  for num in range(len(tmr)):
   ts[tmr[num]] = vlrfnorm[num]
  klst = ts.copy().keys()
  sorted(klst)
  for key in klst:
   if ts[key] == '' or ts[key] == None:
    ts.pop(key)
   else:
    print(lon,lat,stamp(key),ts[key],rf)
    gl.write(str(lon)+','+str(lat)+','+stamp(key)+','+str(ts[key])+','+str(rf)+'\n')
  count+=1
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0,count)
gl.close()
fl.close()
