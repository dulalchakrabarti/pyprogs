import math
import numpy as np
from netCDF4 import Dataset
import pandas as pd
import urllib2
from time import gmtime, strftime
import matplotlib.pyplot as plt
fl = open('marine.csv','w+')
rain = []
opendap_url2 = 'http://nomads.ncep.noaa.gov:9090/dods/gfs_0p50/gfs20190205/gfs_0p50_00z'
nc = Dataset(opendap_url2)
data = nc.variables['apcpsfc'][2:33:2,200:202,152:154]
time,lat,lon = data.shape
for idx in range(time):
 rain.append(math.ceil(data[idx,0,0]))
f = urllib2.urlopen("http://www.incois.gov.in/portal/osf/tidegraphphases.jsp?region=Cochin")
html = f.read()
lines = html.split('\n')
high_date=[]
high_val = []
low_date=[]
low_val = []
for item in lines:
 if item[0:3] == '<tr':
  item = item.split('<')
  if len(item) >= 10:
   x1 = item[3].strip().split('>')
   high_date.append(x1[1])
   x2 = item[5].strip().split('>')
   high_val.append(x2[1])
   x3 = item[7].strip().split('>')
   low_date.append(x3[1])
   x4 = item[9].strip().split('>')
   low_val.append(x4[1])
#dirpwsfc** surface none primary wave direction [deg]
#dirswsfc** surface none secondary wave direction [deg]
#htsgwsfc** surface none significant height of combined wind waves and swell [m]
#perpwsfc** surface none primary wave mean period [s]
#perswsfc** surface none secondary wave mean period [s]
#ugrdsfc** surface none u-component of wind [m/s]
#vgrdsfc** surface none v-component of wind [m/s]
#wdirsfc** surface none wind direction (from which blowing) [deg]
#windsfc** surface none wind speed [m/s]
#wvdirsfc** surface none direction of wind waves [deg]
#wvpersfc** surface none mean period of wind waves [s]          
opendap_url1 = 'http://nomads.ncep.noaa.gov:9090/dods/wave/nww3/nww320190205/nww320190205_00z'
DATAFIELD_NAME = ['wdirsfc','windsfc','htsgwsfc','dirpwsfc','perpwsfc']
pd = {'dirpwsfc':[],'htsgwsfc':[],'perpwsfc':[],'wdirsfc':[],'windsfc':[]}
nc = Dataset(opendap_url1)
for item in DATAFIELD_NAME:
 #print '---------------',item,'---------------'
 data = nc.variables[item][2:33:2,88:90,60:63]
 time,lat,lon = data.shape
 for idx in range(time):
  #print math.ceil(data[idx,0,0])
  pd[item].append(data[idx,0,0])
fl.write( 'Date/Time'+','+'Wind Dir(Deg)'+','+'Wind Speed(m/s)'+','+'Combined(swell+wind)Wave Height(m)'+','+'Swell Dir(Deg)'+','+'Swell Period(s)'+','+'6HrRain(mm)'+'\n')
for idx in range(16):
 fl.write( str(idx*6)+','+str(pd['wdirsfc'][idx])+','+str(pd['windsfc'][idx])+','+str(pd['htsgwsfc'][idx])+','+str(pd['dirpwsfc'][idx])+','+str(pd['perpwsfc'][idx])+','+str(rain[idx])+'\n')
fl.write( 'Date/Time'+','+'High Tide(m)'+','+'Date/Time'+','+'Low Tide(m)'+'\n')
for idx in range(len(high_date)):
 fl.write(high_date[idx]+','+high_val[idx]+','+low_date[idx]+','+low_val[idx]+'\n')
plt.xlabel('Forecast Hours/6')
plt.ylabel('Wave Height(m)')
plt.title('Maximum Wave Height(m)')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.plot(pd['htsgwsfc'])
plt.savefig("wave.png")

plt.xlabel('Forecast Hours/6')
plt.ylabel('Wind Dir(Deg)')
plt.title('Wind Direction')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.plot(pd['wdirsfc'])
plt.savefig("wdir.png")
plt.show()

plt.xlabel('Forecast Hours/6')
plt.ylabel('Wind Speed(m/s)')
plt.title('Wind Speed')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.plot(pd['windsfc'])
plt.savefig("ws.png")
plt.show


