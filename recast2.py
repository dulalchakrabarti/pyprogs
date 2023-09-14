import http
import numpy as np
import time
import requests
import json
from datetime import datetime
def unquote(inp):
    '''
    '''
    return(inp[1:-1])
def str2dec(strs):
    '''
    '2022-03-22T21:30:00.000Z'
    '''
    stm = strs[1:-1]
    print(len(stm))
    dt = datetime.strptime(stm, '%Y-%m-%dT%H:%M:%S.%fZ')
    tm = datetime.timestamp(dt)
    return(tm)
def stamp(strs):
    '''
    '''
    stm = strs
    dt = stm[:-2].replace('T', ' ')
    tm = dt
    return(tm)
seconds1 = time.time()
date1 = input('Start date(2018-03-29)?')
date2 = input('End date(2018-03-29)?')
date1_ = date1.split('-')
date2_ = date2.split('-')
time1 = '00:00:00.000'
time2 = '23:45:00.000'
gl = open(date1_[2]+date1_[1]+date1_[0]+'ts.csv','w')
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
#print(txt)
fl1 = open(date1_[2]+date1_[1]+date1_[0]+'rain.csv')
fl2 = open(date1_[2]+date1_[1]+date1_[0]+'-'+date2_[2]+date2_[1]+date2_[0]+'rain.csv')
gl = open(date1_[2]+date1_[1]+date1_[0]+'ts.csv','w')
count=0
d1 = {}
d2 = {}
lines = [line.rstrip('\n') for line in fl1]
for inp in lines:
 lst = inp.split(',')
 lat = lst[0]
 lon = lst[1]
 val = lat+'_'+lon
 d1[val] = lst[-1]
l1 = list(d1.keys())
sorted(l1)
lines = [line.rstrip('\n') for line in fl2]
for inp in lines:
 buf=inp.split(',')
 #print(len(buf))
 tmd_ = []
 vld_ = []
 tmr_ = []
 vlr_ = []
 if len(buf) > 2 :
  if '_R' in buf[0]:
   lalor = buf[0]
   ptr = len(buf)//2
   ptr=ptr+1
   tmr = buf[1:ptr]
   tmr = [x.strip('[') for x in tmr]
   tmr = [x.strip(' ') for x in tmr]
   tmr = [x.strip('[') for x in tmr]
   tmr = [x.strip(']') for x in tmr]
   tmr = [unquote(x) for x in tmr]
   vlr = buf[ptr:]
   vlr = [x.strip('[') for x in vlr]
   vlr = [x.strip(' ') for x in vlr]
   vlr = [x.strip('[') for x in vlr]
   vlr = [x.strip(']') for x in vlr]
   vlr_ = [i for i in vlr if i != 'None']
   tmr_ = [j for i,j in zip(vlr,tmr) if i != 'None']
   if len(vlr_) > 0:
    vlrf = [float(x) for x in vlr_ ]
    vlrfmx = max(vlrf)
    vlrfnorm = [(j/vlrfmx) for j in vlrf]
  else:
   lalod = buf[0]
   ptr = len(buf)//2
   tmd = buf[1:ptr]
   tmd = [x.strip('[') for x in tmd]
   tmd = [x.strip(' ') for x in tmd]
   tmd = [x.strip('[') for x in tmd]
   tmd = [unquote(x) for x in tmd]
   vld = buf[ptr+1:-1]
   vld = [x.strip('[') for x in vld]
   vld = [x.strip(' ') for x in vld]
   vld = [x.strip('[') for x in vld]
   vld_ = [i for i in vld if i != 'None']
   tmd_ = [j for i,j in zip(vld,tmd) if i != 'None']
   if len(vld_) > 0:
    vldf = [float(x) for x in vld_]
    vldfmx = max(vldf)
    vldfnorm = [(j/vldfmx) for j in vldf]
   for num in range(len(tmd_)):
    lalo_ = lalod.split('_')
    lon = round(float(lalo_[1]),2)
    lat = round(float(lalo_[2]),2)
    lalo = str(lat)+'_'+str(lon)
    ts[tmd_[num]] = vldfnorm[num]
   for num in range(len(tmr_)):
    lalo_ = lalor.split('_')
    lon = round(float(lalo_[1]),2)
    lat = round(float(lalo_[2]),2)
    lalo = str(lat)+'_'+str(lon)
    ts[tmr_[num]] = vlrfnorm[num]
   keylist = ts.copy().keys()
   sorted(keylist)
   d2[lalo] = ''
   for key in keylist:
    if ts[key] == '' or ts[key] == None:
     ts.pop(key)
    else:
     lalo1 = l1[count]
     buf = lalo1.split('_')
     lat = buf[0]
     lon = buf[1]
     rf = d1[lalo1]
     print(lat,lon,key,ts[key],rf,lalo)
     gl.write(str(lon)+','+str(lat)+','+stamp(key)+','+str(ts[key])+','+str(rf)+'\n')
   count+=1     
