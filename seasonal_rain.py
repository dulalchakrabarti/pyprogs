#Program to write 90th day forecast csv file for India
#Author: Dulal Chakrabarti
#Date:11.10.2019
# import modules
from netCDF4 import Dataset
import numpy as np
import datetime
grib_filePath='/home/dulal/prog/'
csv_filePath='/home/dulal/prog/'
#open climate file
nc = Dataset('thai.nc')
#Determine variable dimensions
real,time,lat,lon = nc.variables['tp'].shape
#print real, time, lat, lon
#Define rain
rain = nc.variables['tp']
#Define data values
realv,ftv,latv,timev,lonv,tpv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tp']
#Determine grid lengths
latlen = len(latv[:])
lonlen = len(lonv[:])
#print latlen,lonlen
#Initialize zero matrix
rain_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
#open tp file
#fl = open(csv_filePath+'tp.csv', 'w')
reftime = datetime.datetime.fromtimestamp(ftv[0]).strftime('%Y-%m-%d')
#fl.write('forecastDate,lat,lon,rainfall(mm) since '+reftime+'\n')
store = {}
for day in range(time):
 store[day] = []
 date = datetime.datetime.fromtimestamp(timev[day]).strftime('%Y-%m-%d')
 #print("No. of Day:", day,"Date:", date)   
 for j in range(real):
  rain = np.matrix(tpv[j,day,:,:])
  # Add 51 ensembles
  rain_save = np.add(rain_save,rain)
  # Convert to mm/hr from m/s
 m = (rain_save/51)
 for lat in range(latlen):
  for lon in range(lonlen):
   # Write on the day file
   #fl.write(str(date)+','+str(latv[lat])+','+str(lonv[lon])+','+str(round(m[lat,lon],1)*1000)+'\n')
   # Also print
   print date,latv[lat],lonv[lon],round(m[lat,lon],1)*1000
   store[day].append((latv[lat],lonv[lon],round(m[lat,lon],1)*1000))
 #Reset zero matrix
 rain_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
keys = store.keys()
keys.sort()
gl = open(csv_filePath+'tp_24.csv', 'w')
for key in keys:
  if key > 0:
   u = store[key]
   v = store[key-1]
   c = map(lambda x,y:(x[0],x[1],(x[2]-y[2])),u,v)
   date = datetime.datetime.fromtimestamp(timev[key]).strftime('%Y-%m-%d')
   for i in c:
    gl.write(str(date)+','+str(i[0])+','+str(i[1])+','+str(i[2])+'\n')

