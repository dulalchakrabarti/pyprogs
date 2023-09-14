import os
import glob
import matplotlib.pyplot as plt
from datetime import datetime
def take_second(elem):
    return elem[1]
def str2dec(strs):
    '''
    '2022-03-22T21:30:00.000Z'
    '''
    stm = strs
    dt = datetime.strptime(stm, '%Y-%m-%dT%H:%M:%S.%fZ')
    tm = datetime.timestamp(dt)
    return(tm)
def dec2str(dec):
    '''
    '2022-03-22T21:30:00.000Z'
    '''
    timestamp = dec
    dt_object = datetime.fromtimestamp(timestamp)
    return(dt_object)
three = []
four = []
five  = []
six = []    
files = glob.glob('*ts.csv')
for item in files:
 if len(item) > 16 and item[2:4] == '03':
  three.append(item)
 elif len(item) > 16 and item[2:4] == '04':
  four.append(item)
 elif len(item) > 16 and item[2:4] == '05':
  five.append(item)
three.sort()
four.sort()
five.sort()
#print(three)
#print(four)
#print(five)
ser = {}
for name in three:
 lines = [line.rstrip('\n') for line in open(name)]
 #print(lines[:10])
 lines = lines[10:]
 for line in lines:
  line=line.split(',')
  satid = line[1][17:19]
  #print(satid)
  if satid == '00':
   sat = 'D'
  elif satid =='15':
   sat = 'R'
  lat_lon = line[0].split('_')
  lat = round(float(lat_lon[1]),4)
  lon = round(float(lat_lon[2]),4)
  if str(lat)+'_'+str(lon)+'_'+sat in ser.keys():
   ser[str(lat)+'_'+str(lon)+'_'+sat].extend(line[1:])
   #print('extend...three',lat,lon,sat)
  else:
   ser[str(lat)+'_'+str(lon)+'_'+sat] = line[1:]
   #print('no extend...three',lat,lon,sat)
for name in four:
 lines = [line.rstrip('\n') for line in open(name)]
 #print(lines[:10])
 lines = lines[10:]
 for line in lines:
  line=line.split(',')
  satid = line[1][17:19]
  #print(satid)
  if satid == '00':
   sat = 'D'
  elif satid =='15':
   sat = 'R'
  lat_lon = line[0].split('_')
  lat = round(float(lat_lon[1]),4)
  lon = round(float(lat_lon[2]),4)
  if str(lat)+'_'+str(lon)+'_'+sat in ser.keys():
   ser[str(lat)+'_'+str(lon)+'_'+sat].extend(line[1:])
   #print('extend...four',lat,lon,sat)
  else:
   ser[str(lat)+'_'+str(lon)+'_'+sat] = line[1:]
   #print('no extend...four',lat,lon,sat)
for name in five:
 lines = [line.rstrip('\n') for line in open(name)]
 #print(lines[:10])
 lines = lines[10:]
 for line in lines:
  line=line.split(',')
  satid = line[1][17:19]
  #print(satid)
  if satid == '00':
   sat = 'D'
  elif satid =='15':
   sat = 'R'
  lat_lon = line[0].split('_')
  lat = round(float(lat_lon[1]),4)
  lon = round(float(lat_lon[2]),4)
  if str(lat)+'_'+str(lon)+'_'+sat in ser.keys():
   ser[str(lat)+'_'+str(lon)+'_'+sat].extend(line[1:])
   #print('extend...five',lat,lon,sat)
  else:
   ser[str(lat)+'_'+str(lon)+'_'+sat] = line[1:]
   #print('no extend...five',lat,lon,sat)
keylist = ser.keys()
sorted(keylist)
lst = []
for key in keylist:
 txt = key.split('_')
 lon = txt[0]
 lat = txt[1]
 lonlat = lon+'_'+lat
 lst.append(lonlat)
lst.sort()
frequency = {}

# iterating over the list
for item in lst:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

# printing the frequency
#print(frequency)
keylist = frequency.keys()
sorted(keylist)
gl = open('lalo.csv','w')
for key in keylist:
 latlon = key.split('_')
 print(latlon[1],latlon[0])
 gl.write(latlon[1]+','+latlon[0]+'\n')


