from netCDF4 import Dataset
import numpy as np
nc = Dataset('TOT_PREC_2020.nc')
t,y,x = nc.variables['TOT_PREC'].shape
print t,y,x
print nc.variables['lon'][0,0],nc.variables['lon'][0,208],nc.variables['lon'][145,0],nc.variables['lon'][145,208]
print nc.variables['lat'][0,0],nc.variables['lat'][0,208],nc.variables['lat'][145,0],nc.variables['lat'][145,208]
'''
for i in range(y):
 for j in range(x):
  print nc.variables['lat'][i,j]
print nc.variables['tprate']
for i in range(real):
 for j in range(time):
   print rain[i,j,90:130,240:301]*60000
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
'''


