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
real,time,lat,lon = nc.variables['tas'].shape
temp = nc.variables['tas']
#print("Object (temp): ", temp)
realv,latv,timev,lonv,airtemp = nc.variables['realization'],nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tas']
realv = nc.variables['realization']
latv = nc.variables['lat']
lonv = nc.variables['lon']
timev = nc.variables['time']
airtemp = nc.variables['tas']
#print("Real V: ", realv, ", Lat V: ", latv, ", Lon V: ", lonv, "Time V: ", timev, "Air Temp: ", airtemp)
#print("Real: ", realv[0], ", Lat: ", latv[0], ", Lon: ", lonv[0], ", Time: ", timev[0], ", Temp: ", airtemp[0])
#Determine grid lengths
lat_len = len(latv[latl:latu])
lon_len = len(lonv[lonl:lonr])
time_length = len(timev)
idx_time = time_length - 1
print("Time Length: ", idx_time)
i = 0
#while i < idx_time:
day_before = int((timev[i - 2] - timev[i])/24)
day_last = int((timev[i - 1]   - timev[i])/24)
for day in range(day_before+1, day_last+1):
  #open the day file
  fl = open(str(day)+"_days"+".csv","w")
  fl.write("latitude"+','+"longitude"+','+"days"+','+"Temp_K"+"\n")
  for j in range(len(realv)):
    print day,j,timev[:]-timev[0]
    a_temp = np.matrix(airtemp[day,j,latl:latu,lonl:lonr])
  for lt in range(lat_len):
    for ln in range(lon_len):
      #Write on the day file
      fl.write(str(latv[lt+90])+","+str(lonv[ln+240])+","+day+","+str(round(a_temp[lt,ln],1))+"\n")
      # Also print
      #print(latv[lt+90], lonv[ln+240], day, round(a_temp[lt,ln], 1))
   #Reset zero matrix
  a_temp = np.matrix(np.zeros(lat_len*lon_len).reshape(lat_len,lon_len))
   #i += 1
