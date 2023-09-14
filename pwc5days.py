#Python script to download hourly forecast for five days
#Author: Dulal Chakrabarti
#Date:13.7.2022
#import modules
import requests
import math
import matplotlib.pyplot as plt
import numpy as np
import time
#note start time
seconds1 = time.time()
#input date
date = input('Input date(2018-03-29)?')
date = date.split('-')
#initialize two lists
dlst = []
dnm = []
#define a function to use retrievals
def ret(la,lo):
    '''
    input:latitude grid number(la) and longitude grid number(lo)
    output: dictionaries of parameters
    '''
    #form the url and scrape forecast values from web page
    url = 'https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/gfs'+date[0]+date[1]+date[2]+'/gfs_0p25_1hr_00z.ascii?acpcpsfc[0:120]['+str(la)+']['+str(lo)+'],tmp2m[0:120]['+str(la)+']['+str(lo)+'],rh2m[0:120]['+str(la)+']['+str(lo)+'],vissfc[0:120]['+str(la)+']['+str(lo)+'],tcdcaveclm[0:120]['+str(la)+']['+str(lo)+'],gustsfc[0:120]['+str(la)+']['+str(lo)+'],ugrd10m[0:120]['+str(la)+']['+str(lo)+'],vgrd10m[0:120]['+str(la)+']['+str(lo)+']'
    #print(url)
    html = requests.get(url).text
    vals = html.split('\n')
    for item in vals:
     item.replace(' ','')
     item.replace('[','')
     item.replace(']','')
     item = item.split(',')
     if len(item) == 2:
      if item[0][:2].isalpha():
       dname = item[0]
       dnm.append(dname)# stn name
       dname = {}
       dlst.append(dname)# stn dictionary name
      else:
       #print(item)
       key = item[0]
       key = key.split(']')
       k = key[0][1:]
       if int(k) <= 121:
        val = item[1].strip()
        #print(len(val))
        dname[k] = val #update dictionary
     elif len(item) == 121:
      if len(dname) == 0:
       dname[0] = item
     elif len(item) == 1:
      if len(dname) == 0:
       dname[0] = item[0]
    return dlst # return dictionaries
#stn names and nearest grid points
grid = [['Banda',462,321],['Varanasi',461,332],['Prayagraj',462,327],['Jhansi',462,315],['Ghazipur',462,334],['Azamgarh',464,332],['Sultanpur',465,329],['Kanpur',466,321],['Gorakhpur',467,333],['Basti',467,331],['Lucknow',467,324],['Gonda',468,328],['Agra',469,312],['Mathura',470,310],['Aligarh',471,313],['Shahjahanpur',472,319],['Bareilly',474,318],['Moradabad',475,315],['Meerut',476,311]]
#iterate grids
for g in grid:
 dval = ret(g[1],g[2])  
 for d,nm in zip(dlst,dnm):
  fl = open(g[0]+nm+'5.csv','w')
  l = list(d.values())
  for i in range(len(l)):
   fl.write(str(i)+','+str(l[i])+'\n')
  #print(g[0],nm)
  #print(list(d.values()))
 fl.close()
 print('processed...',g[0])
 time.sleep(2)# to avoid loading the server
#note the time and print number of minutes 
seconds2 = time.time()
print('elapsed minutes....',(seconds2-seconds1)/60.0)


