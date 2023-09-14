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
vald = []
valr = []
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
#print(lstf1)
for item1 in lstf1:
 #print(item1[:2])
 if item1[:2] =='04':
  exit(0)  
 lines = [line.rstrip('\n') for line in open(item1)]
 lines = lines[1:]
 for num in range(len(lines)):
  if num%2 != 0:
   satvld=[]
   sattmd =[]
   satvlr=[]
   sattmr=[]
   line = lines[num].split(',')
   line = [x.strip('[') for x in line]
   line = [x.strip(']') for x in line]
   line = [x.strip(' ') for x in line]
   buf = line[0].split('_')
   lon = buf[1][:6]
   lat = buf[2][:6]
   sat = buf[3][:6]
   l = len(line[1:])
   tm = line[1:(l//2)+1]
   tm = [x.strip("'") for x in tm]
   #tm = [stamp(x) for x in tm]
   tm = [stamp1(x) for x in tm]
   tm = tm[:-1]
   vl = line[(l//2)+1:]
   vl = [x.strip('[') for x in vl]
   vl = vl[:-1]
   print(tm)
   if 'T00:30' in tm[1]:
    sat = 'D'
    print('found D...........')
   elif 'T00:45' in tm[1]:
    sat = 'R'
    print('found R..............')
'''
   if 'None' in vl:
    pass
   else:
    if len(tm) and len(vl) <= 48:
     if sat == 'D':
       sattmd.extend(tm)
       satvld.extend(vl)
       print('D',sattmd)
       print('D',satvld)
     elif sat == 'R':
       sattmr.extend(tm)
       satvlr.extend(vl)
       print('R',sattmr)
       print('R',satvlr)
   if num%2 == 0:
    mix1 = countList(sattmd[:len(sattmr)], sattmr)
    mix2 = countList(satvld[:len(satvlr)], satvlr)
    if lat+'_'+lon in satrdtm.keys():
       satrdtm[lat+'_'+lon].extend(mix1)
       satrdvl[lat+'_'+lon].extend(mix2)
    else:
       satrdtm[lat+'_'+lon]=mix1
       satrdvl[lat+'_'+lon]=mix2
keylist1 = satrdtm.keys()
print(keylist1)
keylist2 = satrdvl.keys()
for key1 in keylist1:
 if len(satrdtm[key1])>1000:
   rdvl = satrdvl[key1]
   mrdvl =max(rdvl)
   rdvl =[float(x)/float(mrdvl) for x in rdvl]
   rdtm =satrdtm[key1]
   if len(rdtm)>2000:
    latlon = key1.split('_')
    lat = latlon[0]
    lon = latlon[1]
    #for item in rdtm:
     #print(lat,lon,item)
    print(rdtm)
    
   #print(key1,rdtm,rdvl)
   #plt.xticks(rotation=15, ha='right')
   #plt.scatter(rdtm[:20],rdvl[:20])
   #plt.show()
   #a = input('Press a key to exit')
   #if a:
    #exit(0)
'''
