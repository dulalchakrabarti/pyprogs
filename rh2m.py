import math
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
#start = datetime(1,1,1,0,0,0)
#timedelta_hrs = timedelta(days=738273.0+0.041666668)
#print(start+timedelta_hrs)
date = input('date[ex.20220427]?')
URL = "https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/gfs"+date+"/gfs_0p25_1hr_00z.ascii?rh2m[24:48][436][292],tmp2m[0:24][436][292]"
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html.parser' )#'html5lib','lxml'
data = soup.prettify()
data = data.split('\n\n')
rh = []
for item in data:
 item = item.split(',')
 if len(item) == 3:
  rh.append(item[2].strip(' '))
 elif len(item) == 2:
  rh.append(item[1].strip(' '))
 elif len(item) == 30:
  rh.append(item[-1].strip(' '))
  #print(item[:123])
  #print(item[123:-1])
 elif len(item) == 28:
  pass
  #print(item[:-2])
  #print(item[-2:])
hum = rh[:25]
hum = hum[:-1]
hum = [round(float(x),1) for x in hum]
#print(hum)
temp = rh[25:]
temp = temp[:-1]
temp = [round(float(x)-273.15,1) for x in temp]
#print(temp)
x = range(24,48)
hrs = []
for item in x:
 hrs.append(item)
#print(hrs)
fl = open(date+'.csv','w')
for k,l,m in zip(hrs,temp,hum):
 print(k,l,m)
 fl.write(str(k)+','+str(l)+','+str(m)+'\n')
fl.close()

