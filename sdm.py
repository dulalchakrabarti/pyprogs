from netCDF4 import Dataset
import numpy as np
import time
nc = Dataset('sdm.nc')
real,tim,lat,lon = nc.variables['tas'].shape
realv,ftv,leadv,latv,timev,lonv,tmprv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],nc.variables['leadtime'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tas']
for i in range(real):
 for j in range(tim):
  result = time.gmtime(timev[j])
  print i,result.tm_year,result.tm_mon,result.tm_mday,result.tm_hour,tmprv[i,j,70,80]
'''

for i in range(real):
 for j in range(time):
  print tmprv[real[i],timev[j],latv[70],lonv[80]]

for i in range(tot):
 grb = grbs.select(name='2 metre temperature')[i]
 data = grb.values
 lats,lons = grb.latlons()
 print i,data[70,80],lats[70,80],lons[70,80]
'''
