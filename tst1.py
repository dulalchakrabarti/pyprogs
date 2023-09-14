#Program to write 90th day forecast csv file for India
#Author: Dulal Chakrabarti
#Date:11.10.2019
# import modules
from netCDF4 import Dataset
import numpy as np
#Define grid
latu = 131
latl = 90
lonl = 250
lonr = 290
#open climate file
nc = Dataset('rain.nc')
#Determine variable dimensions
real,time,lat,lon = nc.variables['tas'].shape
#Define data values
realv,ftv,leadv,latv,timev,lonv,tmpv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],nc.variables['leadtime'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tas']
#Determine grid lengths
latlen = len(latv[latl:latu])
lonlen = len(lonv[lonl:lonr])
#Iterate over the 90th day
for day in range(time):
 #open the day file
 fl = open(str(day)+'.csv','w')
 #Initialize zero matrix
 tmp_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
 for j in range(real):
  tmp = np.matrix(tmpv[j,day,latl:latu,lonl:lonr])
  # Add 51 ensembles
  tmp_save = np.add(tmp_save,tmp)
  # Convert to degc
 degc = (tmp_save/51)-273.15
 for lat in range(latlen):
  for lon in range(lonlen):
   # Write on the day file
   fl.write(str(latv[lat+latl])+','+str(lonv[lon+lonl])+','+str(round(degc[lat,lon],1))+'\n')
   # Also print
   print day,latv[lat+latl],lonv[lon+lonl],round(degc[lat,lon],1)



