import os
import glob
import matplotlib.pyplot as plt
from datetime import datetime
import time
def rain_class(rfdif):
    if rfdif>0.0:
     print(rfdif)
    if float(rfdif) <= 0.0:
     cat = 0
    elif float(rfdif) > 0.0 and float(rfdif) <= 60.0:
     cat = 1
    elif float(rain) > 60.0:
     cat = 2
    return cat
six = []    
files = glob.glob('*6*ts_*.csv')
for item in files:
 if len(item) > 16 and item[2:4] == '06':
  six.append(item)
six.sort()
seven = []    
files = glob.glob('*7*ts_*.csv')
for item in files:
 if len(item) > 16 and item[2:4] == '07':
  seven.append(item)
eight = []    
files = glob.glob('*8*ts_*.csv')
for item in files:
 if len(item) > 16 and item[2:4] == '08':
  eight.append(item)
nine = []    
files = glob.glob('*9*ts_*.csv')
for item in files:
 if len(item) > 16 and item[2:4] == '09':
  nine.append(item)
ten = []    
files = glob.glob('*10*ts_*.csv')
for item in files:
 if len(item) > 16 and item[2:4] == '10':
  ten.append(item)
eleven = []    
files = glob.glob('*11*ts_*.csv')
for item in files:
 if len(item) > 16 and item[2:4] == '11':
  eleven.append(item)
six.sort()
seven.sort()
eight.sort()
nine.sort()
ten.sort()
eleven.sort()
six.extend(seven)
six.extend(eight)
six.extend(nine)
six.extend(ten)
six.extend(eleven)
d4 = {}
for num in range(0,len(six),4):
 #print('processing file.....'+six[num],'processing file.....'+six[num+1],'processing file.....'+six[num+2],'processing file.....'+six[num+3])
 ir1lines = [line.rstrip('\n') for line in open(six[num])]
 lir1 = len(ir1lines)
 for n in range(lir1):
  ir1line = ir1lines[n].split(',')
  kir1 = ir1line[0]+'_'+ir1line[1]
  ir1 = ir1line[2:]
  ir1.append('ir1')
  if kir1 in d4.keys():
   d4[kir1].append(ir1)
  else:
   d4[kir1] = [ir1]
 ir2lines = [line.rstrip('\n') for line in open(six[num+1])]
 lir2 = len(ir2lines)
 for n in range(lir2):
  ir2line = ir2lines[n].split(',')
  kir2 = ir2line[0]+'_'+ir2line[1]
  ir2 = ir2line[2:]
  ir2.append('ir2')
  if kir2 in d4.keys():
   d4[kir2].append(ir2)
  else:
   d4[kir2] = [ir2]
 mirlines = [line.rstrip('\n') for line in open(six[num+2])]
 lmir = len(mirlines)
 for n in range(lmir):
  mirline = mirlines[n].split(',')
  kmir = mirline[0]+'_'+mirline[1]
  mir = mirline[2:]
  mir.append('mir')
  if kmir in d4.keys():
   d4[kmir].append(mir)
  else:
   d4[kmir] = [mir]
 if (num+3) < len(six):
  wvlines = [line.rstrip('\n') for line in open(six[num+3])]
  lwv = len(wvlines)
  for n in range(lwv):
   wvline = wvlines[n].split(',')
   kwv = wvline[0]+'_'+wvline[1]
   wv = wvline[2:]
   wv.append('wv')
   if kwv in d4.keys():
    d4[kwv].append(wv)
   else:
    d4[kwv] = [wv]
klst = d4.keys()
sorted(klst)
#print(klst)
for k in klst:
 n = len(d4[k])
 if n > 35000:
  lst = d4[k]
  k = k.strip()
  fl = open(k+'.csv','w')
  print(k+'.csv'+' opened for........',n,' bytes')
  for item in lst:
   #print(item[0],item[1],item[2],item[-1])
   fl.write(item[0]+','+item[1]+','+item[2]+','+item[-1]+'\n')
  fl.close()
 time.sleep(1)
