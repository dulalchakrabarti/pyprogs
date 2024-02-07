import math
import numpy as np
from netCDF4 import Dataset
import pandas as pd
import urllib2
import matplotlib.pyplot as plt
from ast import literal_eval
import collections
import datetime,time
dt = raw_input("Input date(ex.20190208???? ):")
tm = raw_input("Input time(ex.18???? ):")
def date_time(hr):
    '''
    '''
    out = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out = out.split()
    out = out[0].split('-')
    out = int(out[-1])
    if hr == 0:
     out = str(out)+'/'+'0600'
    elif hr == 6:
     out = str(out)+'/'+'1200'
    elif hr == 12:
     out = str(out)+'/'+'1800'
    elif hr == 18:
     out = out + 1
     out = str(out)+'/'+'0000'
    elif hr == 24:
     out = out + 1
     out = str(out)+'/'+'0600'
    elif hr == 30:
     out = out + 1
     out = str(out)+'/'+'1200'
    elif hr == 36:
     out = out + 1
     out = str(out)+'/'+'1800'
    elif hr == 42:
     out = out + 2
     out = str(out)+'/'+'0000'
    elif hr == 48:
     out = out + 2
     out = str(out)+'/'+'0600'
    elif hr == 54:
     out = out + 2
     out = str(out)+'/'+'1200'
    elif hr == 60:
     out = out + 2
     out = str(out)+'/'+'1800'
    elif hr == 66:
     out = out + 3
     out = str(out)+'/'+'0000'
    elif hr == 72:
     out = out + 3
     out = str(out)+'/'+'0600'
    elif hr == 78:
     out = out + 3
     out = str(out)+'/'+'1200'
    elif hr == 84:
     out = out + 3
     out = str(out)+'/'+'1800'
    elif hr == 90:
     out = out + 4
     out = str(out)+'/'+'0000'
    elif hr == 96:
     out = out + 4
     out = str(out)+'/'+'0600'
    elif hr == 102:
     out = out + 4
     out = str(out)+'/'+'1200'
    elif hr == 108:
     out = out + 4
     out = str(out)+'/'+'1800'
    elif hr == 114:
     out = out + 5
     out = str(out)+'/'+'0000'
    return out

def per(deg):
    '''
    '''
    global out
    out='-'
    if deg == '--':
     out = '--'
    elif deg < 100:
     out = int(deg)
    return out

def deg2comp(deg):
    '''
    '''
    global out
    out='-'
    if deg == '--':
     out = '--'
    elif deg >= 0 and deg < 22.5:
     out = 'N'
    elif deg >= 22.5 and deg < 45:
     out = 'NNE'
    elif deg >= 45 and deg < 67.5:
     out = 'NE'
    elif deg >= 67.5 and deg < 90:
     out = 'ENE'
    elif deg >= 90 and deg < 112.5:
     out = 'E'
    elif deg >= 112.5 and deg < 135:
     out = 'ESE'
    elif deg >= 135 and deg < 157.5:
     out = 'SE'
    elif deg >= 157.5 and deg < 180:
     out = 'SSE'
    elif deg >= 180 and deg < 202.5:
     out = 'S'
    elif deg >= 202.5 and deg < 225:
     out = 'SSW'
    elif deg >= 225 and deg < 247.5:
     out = 'SW'
    elif deg >= 247.5 and deg < 270:
     out = 'WSW'
    elif deg >=270 and deg < 292.5:
     out = 'W'
    elif deg >= 292.5 and deg < 315:
     out = 'WNW'
    elif deg >= 315 and deg < 337.5:
     out = 'NW'
    elif deg >= 337.5 and deg < 360:
     out = 'NNW'
    return out


df  = pd.DataFrame(index = range(31),columns=['00','01','02','03','04','05','06','07','08','09','10','11','12',
'13','14','15','16','17','18','19','20','21','22','23'])
timed = collections.OrderedDict()
f = urllib2.urlopen("http://www.incois.gov.in/portal/osf/tidegraphphases.jsp?region=Cochin")
html = f.read()
start=html.index('[[')
end = html.index(']]')
tide = html[start:end+2]
tide = literal_eval(tide)
date = ''
timed = collections.OrderedDict()
for idx in range(len(tide)):
 timestamp = int(tide[idx][0])/1000
 time = datetime.datetime.fromtimestamp(timestamp).strftime('%c')
 tim = time.split()
 hh = tim[3].split(':')
 if tim[2] != date:
  if len(timed)>0:
   for k,v in timed.items():
    df.loc[df.index[int(date)], k] = v
   timed = collections.OrderedDict()
   date = tim[2]
   timed[hh[0]]=tide[idx][1]
  else:
   date = tim[2]
   timed[hh[0]]=tide[idx][1]
 else:
  timed[hh[0]] = tide[idx][1]
for k,v in timed.items():
 df.loc[df.index[int(date)], k] = v
df.dropna().to_csv('tide.csv')
#rain
fl = open('marine.csv','w+')
rain = []
gust = []
opendap_url2 = 'https://nomads.ncep.noaa.gov:9090/dods/gfs_0p25/gfs'+dt+'/gfs_0p25_'+tm+'z'
nc = Dataset(opendap_url2)
data = nc.variables['apcpsfc'][4:43:2,200:201,152:153]
time,lat,lon = data.shape
for idx in range(time):
 rain.append(math.ceil(data[idx,0,0]))
data = nc.variables['gustsfc'][4:43:2,200:201,152:153]
time,lat,lon = data.shape
for idx in range(time):
 gust.append(math.ceil(data[idx,0,0]))
opendap_url1 = 'https://nomads.ncep.noaa.gov:9090/dods/wave/nww3/nww3'+dt+'/nww3'+dt+'_'+tm+'z'
DATAFIELD_NAME = ['wdirsfc','windsfc','htsgwsfc','dirpwsfc','perpwsfc','dirswsfc','perswsfc']
dd = {'dirpwsfc':[],'htsgwsfc':[],'perpwsfc':[],'wdirsfc':[],'windsfc':[],'dirswsfc':[],'perswsfc':[]}
nc = Dataset(opendap_url1)
for item in DATAFIELD_NAME:
 data = nc.variables[item][4:43:2,88:89,60:61]
 time,lat,lon = data.shape
 for idx in range(time):
  dd[item].append(data[idx,0,0])
fl.write( 'Date/Time'+','+'Surface Wind Dir'+','+'Surface Wind Spd [m/s]'+','+'Surface wind Gust [m/s]'+','+'Combined(swell+wind)Wave Height(m)'+','+'Swell Dir(Deg)'+','+'Swell Period(s)'+','+'Swell2 Dir(Deg)'+','+'Swell2 Period(s)'+','+'6HrRain(mm)'+'\n')
for idx in range(20):
 fl.write( str(date_time(idx*6))+','+str(deg2comp(int(dd['wdirsfc'][idx])))+','+str(int(dd['windsfc'][idx]))+','+str(gust[idx])+','+str(round(dd['htsgwsfc'][idx],1))+','+str(deg2comp(int(dd['dirpwsfc'][idx])))+','+str(int(dd['perpwsfc'][idx]))+','+str(deg2comp(dd['dirswsfc'][idx]))+','+str(per(dd['perswsfc'][idx]))+','+str(rain[idx])+'\n')
fl.close()
fr = pd.read_csv('marine.csv')

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(fr['Date/Time'], fr['Surface Wind Spd [m/s]'],'bo-')
ax1.set_xticklabels(fr['Date/Time'],rotation = 90)

ax1.set_xlim(0, 20)
ax1.set_xlabel("Date/Time")
ax1.set_ylabel("Wind Speed(blue)(m/s)/Gust(red)(m/s)")

ax2 = ax1.twiny()
ax2.set_xlabel("Wind Direction(Deg)")
ax2.set_xlim(0, len(fr['Surface Wind Dir']))
ax2.plot(range(len(fr['Surface Wind Dir'])),fr['Surface wind Gust [m/s]'],'ro-')
ax2.set_xticks(range(len(fr['Surface Wind Dir'])))
ax2.set_xticklabels(fr['Surface Wind Dir'],rotation = 90)
plt.tight_layout()
plt.savefig('wind.png')
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(fr['Date/Time'], fr['Combined(swell+wind)Wave Height(m)'],'ro-')
ax1.set_xticklabels(fr['Date/Time'],rotation = 90)

ax1.set_xlim(0, 20)
ax1.set_xlabel("Date/Time")
ax1.set_ylabel("Combined(swell+wind)Wave Height(m)")

ax2 = ax1.twiny()
ax2.set_xlabel("Primary Swell Direction(Deg)")
ax2.set_xlim(0, len(fr['Combined(swell+wind)Wave Height(m)']))
ax2.set_xticks(range(len(fr['Swell Dir(Deg)'])))
ax2.set_xticklabels(fr['Swell Dir(Deg)'],rotation = 90)
plt.tight_layout()
plt.savefig('wave.png')
plt.show()


