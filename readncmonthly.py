from netCDF4 import Dataset
import numpy as np
nc = Dataset('mrain.nc')
real,time,lat,lon = nc.variables['tprate'].shape
rain = nc.variables['tprate']
realv,ftv,leadv,latv,timev,lonv,tprv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],nc.variables['leadtime'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tprate']
latlen = len(latv[90:130])
lonlen = len(lonv[240:301])
rain_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
jsave = 0
isave = 0
for i in range(time):
 for j in range(real):
  rain = np.matrix(np.array(tprv[j,i,90:130,240:301]))
  #print j,i,rain,jsave,isave,rain_save
  rain_save = np.add(rain,rain_save)
  jsave = j
  isave = i
 print jsave,isave,(rain_save/51)*3600000
'''
for item in nc.variables.keys():
 item = item.encode('utf-8')
 print item
print nc.variables['tprate']
for i in range(real):
 for j in range(time):
   print rain[i,j,90:130,240:301]*60000
for i in range(real):
 for j in range(time):
   print i,j,rain[i,j,90:130,240:301]*60000


real,time,lat,lon = nc.variables['tprate'].shape
rain = nc.variables['tprate']
realv,ftv,leadv,latv,timev,lonv,tprv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],nc.variables['leadtime'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tprate']
latlen = len(latv[90:130])
lonlen = len(lonv[240:301])
rain_save = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
jsave = 0
isave = 0
for i in range(time):
 for j in range(real):
  rain = np.matrix(np.array(tprv[j,i,90:130,240:301]))
  print j,i,rain,jsave,isave,rain_save
  rain_save = np.add(rain,rain_save)
  jsave = j
  isave = i
print jsave,isave,(rain_save/51)*60000
'''


