import os
import glob
import matplotlib.pyplot as plt
from datetime import datetime
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
three = []
four = []
five  = []
six = []    
files = glob.glob('*ts.csv')
for item in files:
 if len(item) == 14 and item[2:4] == '03':
  three.append(item)
 elif len(item) == 14 and item[2:4] == '04':
  four.append(item)
 elif len(item) == 14 and item[2:4] == '05':
  five.append(item)
 elif len(item) == 14 and item[2:4] == '06':
  six.append(item)
three.sort()
four.sort()
five.sort()
six.sort()
ser = {}
for name in three:
 lines = [line.rstrip('\n') for line in open(name)]
 for line in lines:
  txt = []
  line=line.split(',')
  val = float(line[3])
  lon = line[0]
  lat = line[1]
  time = line[2]
  val = format(val,".4f")
  rf = line[4]
  rain = rf
  lalo = lat+'_'+lon
  txt.append(time)
  txt.append(val)
  txt.append(rain)
  if lalo in ser.keys():
   ser[lalo].append(txt)
  else:
   ser[lalo] = [txt]
for name in four:
 lines = [line.rstrip('\n') for line in open(name)]
 for line in lines:
  txt = []
  line=line.split(',')
  val = float(line[3])
  lon = line[0]
  lat = line[1]
  time = line[2]
  val = format(val,".4f")
  rf = line[4]
  rain = rf
  lalo = lat+'_'+lon
  txt.append(time)
  txt.append(val)
  txt.append(rain)
  if lalo in ser.keys():
   ser[lalo].append(txt)
  else:
   ser[lalo] = [txt]
for name in five:
 lines = [line.rstrip('\n') for line in open(name)]
 for line in lines:
  txt = []
  line=line.split(',')
  val = float(line[3])
  lon = line[0]
  lat = line[1]
  time = line[2]
  val = format(val,".4f")
  rf = line[4]
  rain = rf
  lalo = lat+'_'+lon
  txt.append(time)
  txt.append(val)
  txt.append(rain)
  if lalo in ser.keys():
   ser[lalo].append(txt)
  else:
   ser[lalo] = [txt]
for name in six:
 lines = [line.rstrip('\n') for line in open(name)]
 for line in lines:
  txt = []
  line=line.split(',')
  val = float(line[3])
  lon = line[0]
  lat = line[1]
  time = line[2]
  val = format(val,".4f")
  rf = line[4]
  rain = rf
  lalo = lat+'_'+lon
  txt.append(time)
  txt.append(val)
  txt.append(rain)
  if lalo in ser.keys():
   ser[lalo].append(txt)
  else:
   ser[lalo] = [txt]
keylist = ser.keys()
sorted(keylist)
for key in keylist:
 if len(ser[key]) > 7750:
  gl = open(key+'.csv','w')
  for num in range(1,len(ser[key])):
   item1 = ser[key][num]
   item2 = ser[key][num-1]
   rfdif = float(item1[2])-float(item2[2])
   rfclass = rain_class(rfdif)
   print(key,item1[0],item1[1],rfclass)
   gl.write(str(item1[0])+','+str(item1[1])+','+str(rfclass)+'\n')
  gl.close()
