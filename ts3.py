import os
import glob
import matplotlib.pyplot as plt
from datetime import datetime
def stamp(strs):
    '''
    '''
    stm = strs
    dt = datetime.strptime(stm, '%Y-%m-%dT%H:%M:%S.%fZ')
    tm = datetime.timestamp(dt)
    return(tm)
def stamp1(strs):
    '''
    '''
    stm = strs
    dt = stm[:-2].replace('T', ' ')
    tm = dt
    return(tm)

def countList(lst1, lst2):
    return [item for pair in zip(lst1, lst2 + [0])
                                 for item in pair]
lstf1 = []
lstf2 = []
lstf3 = []
vld = []
vlr = []
tmd = []
tmr = []
satvld=[]
sattmd =[]
satvlr=[]
sattmr=[]
satvlrd=[]
sattmrd=[]
satrdtm = {}
satrdvl = {}
files = glob.glob('*-*.csv')
for item in files:
 if item[2:4] =='03':
  lstf1.append(item)
lstf1.sort() 
for item in files:
 if item[2:4] =='04':
  lstf2.append(item)
lstf2.sort()
for item in files:
 if item[2:4] =='05':
  lstf3.append(item)
lstf3.sort()
lstf2.extend(lstf3)
lstf1.extend(lstf2) 
for item1 in lstf1:
 lines = [line.rstrip('\n') for line in open(item1)]
 for num in range(1,len(lines)):
  line = lines[num].split(',')
  loc = line[0].split('_')
  lon = loc[1]
  lat = loc[2]
  line = [x.strip('[') for x in line]
  line = [x.strip(']') for x in line]
  line = [x.strip(' ') for x in line]
  line = [x.strip('[') for x in line]
  if 'T00:30' in line[2]:
   sat = 'D'
   tmd = line[1:(len(line)//2)]
   vld = line[(len(line)//2)+1:-1]
   sattmd.extend(tmd)
   satvld.extend(vld)
   print(sat,len(sattmd),len(satvld))
  elif 'T00:45' in line[2]:
   sat = 'R'
   tmr = line[1:(len(line)//2)+1]
   vlr = line[(len(line)//2)+1:]
   sattmr.extend(tmr)
   satvlr.extend(vlr)
   print(sat,len(sattmr),len(satvlr))
'''
mix1 = countList(sattmd[:len(sattmr)], sattmr)
mix2 = countList(satvld[:len(satvlr)], satvlr)
print(len(mix1),len(mix2))
    if lat+'_'+lon in satrdtm.keys():
       satrdtm[lat+'_'+lon].extend(mix1)
       satrdvl[lat+'_'+lon].extend(mix2)
    else:
       satrdtm[lat+'_'+lon]=mix1
       satrdvl[lat+'_'+lon]=mix2
keylist1 = satrdtm.keys()
keylist2 = satrdvl.keys()
for key1 in keylist1:
 print(len(satrdtm))
 print(len(satrdtm))
 if len(satrdtm[key1])>1000:
   rdvl = satrdvl[key1]
   mrdvl =max(rdvl)
   rdvl =[float(x)/float(mrdvl) for x in rdvl]
   rdtm =satrdtm[key1]
   if len(rdtm)>1000:
    latlon = key1.split('_')
    lat = latlon[0]
    lon = latlon[1]
    #for item in rdtm:
     #print(lat,lon,item)
    print(rdtm)
   print(key1,rdtm,rdvl)
   plt.xticks(rotation=15, ha='right')
   plt.scatter(rdtm[:20],rdvl[:20])
   plt.show()
   a = input('Press a key to exit')
   if a:
    exit(0)
'''
