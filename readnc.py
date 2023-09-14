from netCDF4 import Dataset
import numpy as np
from datetime import *
import time
import datetime
nc = Dataset('thai.nc')
for item in nc.variables.keys():
 item = item.encode('utf-8')
 temp = nc.variables[item]
 print item,temp.shape
lati = nc.variables['lat']
print lati[0],lati[1],lati[-1]
longi = nc.variables['lon']
print longi[0],longi[1],longi[-1]
tim = nc.variables['time']
print tim[1]-tim[0]
frt = nc.variables['forecast_reference_time']
print datetime.datetime.fromtimestamp(frt[0]).strftime('%Y-%m-%d')
'''
timestamp = tim[10]*24*3600
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

lati = nc.variables['lat']
print lati[95]
longi = nc.variables['lon']
print longi[41]
tim = nc.variables['time']
print tim[0],tim[1],tim[1798],tim[1799]
temp = nc.variables['pr']
print 86400*temp[1600:1615,95,41]
temp = nc.variables['tas']
real,lat,lon = temp.shape
realv,timev,latv,lonv,tmprv = nc.variables['realization'],nc.variables['time'],\
                                       nc.variables['lat'],nc.variables['lon'],nc.variables['tas']
temp = nc.variables['tas']future_date = datetime.datetime(1970, 1, 2)

past_date = datetime.datetime(1970, 1, 1)


difference = (future_date - past_date)

Calculate difference in time


total_seconds = difference.total_seconds()

Convert time difference to seconds


print(total_seconds)


real,lat,lon = temp.shape
for i in range(real):
 for j in range(lat):
  for k in range(lon):
   print temp[i,j,k]-273



rain = nc.variables['pr_amount']
real,time,lat,lon = rain.shape
for i in range(real):
 for j in range(time):
   print rain[i,j,90:130,240:301]
for i in range(real):
 for j in range(time):
   print i,j,rain[i,j,90:130,240:301]*60000
real,time,lat,lon = nc.variables['tas'].shape
realv,ftv,leadv,latv,timev,lonv,tmprv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],nc.variables['leadtime'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tas']
latlen = len(latv[90:129])
lonlen = len(lonv[240:300])
jsave = 0
isave = 0
for i in range(time):
 tmp_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
 for j in range(real):
  tmp = np.matrix(np.array(tmprv[j,i,90:129,240:300]))
  #print jsave,isave,rain_save
  tmp_save = np.add(tmp,tmp_save)
  jsave = j
  isave = i
  #print isave,tmp_save
 tmp_day = (tmp_save/51)-273
 tmp_day_5 = tmp_day.tolist()
 for k in tmp_day_5:
  xx = [round(l,1) for l in k]
  print isave, xx
'''


