#Program to write 90th day forecast csv file for India
#Author: Dulal Chakrabarti
#Date:11.10.2019
# import modules
from netCDF4 import Dataset
import numpy as np
#Define grid
latu = 141
latl = 100
lonl = 250
lonr = 290
#open climate file
nc = Dataset('rain.nc')
#Determine variable dimensions
real,time,lat,lon = nc.variables['pr_amount'].shape
#Define rain rate
rain = nc.variables['pr_amount']
#Define data values
realv,ftv,latv,timev,lonv,tprv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['pr_amount']
#Determine grid lengths
latlen = len(latv[latl:latu])
lonlen = len(lonv[lonl:lonr])
#Initialize zero matrix
rain_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
#Iterate over the 90th day
for day in range(time):
 #open the day file
 fl = open(str(day)+'.csv','w')
 for j in range(real):
  rain = np.matrix(tprv[j,day,latl:latu,lonl:lonr])
  # Add 51 ensembles
  rain_save = np.add(rain_save,rain)
  # Convert to mm/hr from m/s
  mm_per_hr = (rain_save/51)#*3600000
 for lat in range(latlen):
  for lon in range(lonlen):
   # Write on the day file
   fl.write(str(latv[lat+90])+','+str(lonv[lon+240])+','+str(round(mm_per_hr[lat,lon],1))+'\n')
   # Also print
   print day,latv[lat+90],lonv[lon+240],round(mm_per_hr[lat,lon],1)
 #Reset zero matrix
 rain_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
