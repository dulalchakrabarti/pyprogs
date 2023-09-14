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
date2 = input('End date(2018-03-29)?')
date1_ = date1.split('-')
date2_ = date2.split('-')
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
fl1 = open(date1_[2]+date1_[1]+date1_[0]+'rain.csv')
fl2 = open(date1_[2]+date1_[1]+date1_[0]+'-'+date2_[2]+date2_[1]+date2_[0]+'rain.csv')
gl = open(date1_[2]+date1_[1]+date1_[0]+'ts.csv','w')
count1=0
count2=0
d1 = {}
d2 = {}
lines = [line.rstrip('\n') for line in fl1]
for inp in lines:
 lst = inp.split(',')
 lat = lst[0]
 lon = lst[1]
 val = lat+'_'+lon
 d1[val] = lst[-1]
 count1+=1
keylist = d1.keys()
sorted(keylist)
l1 = list(d1.keys())
l2 = list(d1.values())
from itertools import repeat
new_list1=[]
new_list2=[]
for x,y in zip(l1,l2):
 given_value1 = x
 new_list1.extend(repeat(given_value1,2))
 given_value2 = y
 new_list2.extend(repeat(given_value2,2))
lines = [line.rstrip('\n') for line in fl2]
for inp in lines:
 lst = inp.split(',')
 if len(lst) > 2:
  lst_ = lst[0].split('_')
  lat = lst_[1]
  lon = lst_[2]
  sat = lst_[3]
  val = lat+'_'+lon+'_'+sat
  d2[val] = lst[1:-1]
keylist = d2.keys()
sorted(keylist)
for key in keylist:
 line = d2[key]
 line = [x.strip('"[') for x in line]
 line = [x.strip(']"') for x in line]
 line = [x.strip(' ') for x in line]
 line = [x.strip('[') for x in line]
 if '_D' in key:
  l1 = len(line)//2
 else:
  l1 = (len(line)//2)+1
 buf = line[:l1]
 vl = line[l1:]
 print(key)
 print(buf)
 print(vl)
 count2+=1
print(new_list1)
print(new_list2)
print(count1,count2)
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0,count)
