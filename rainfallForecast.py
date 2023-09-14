#Program to write 90th day forecast csv file for India
#Author: Dulal Chakrabarti
#Date:11.10.2019
# import modules
from netCDF4 import Dataset
import numpy as np
import datetime
#Define grid
latu = 40
latl = 0
lonl = 0
lonr = 40
grib_filePath='/home/dulal/prog/'
csv_filePath='/home/dulal/prog/'
#open climate file
nc = Dataset(grib_filePath+'rf.nc')
#Determine variable dimensions
real,time,lat,lon = nc.variables['tp'].shape
#Define ghi accumulated
rf = nc.variables['tp']
#Define data values
realv,ftv,latv,timev,lonv,rfv = nc.variables['realization'],\
                                       nc.variables['forecast_reference_time'],\
                                       nc.variables['lat'],nc.variables['time'],nc.variables['lon'],nc.variables['tp']
#Determine grid lengths
latlen = len(latv[latl:latu])
lonlen = len(lonv[lonl:lonr])
#Initialize zero matrix
rf_Accu = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))
#open tp file
fl = open(csv_filePath+'tp.csv', 'w')
fl.write('lat,lon,forecastDate,gmt,value\n')
for day in range(time):
 date = datetime.datetime.fromtimestamp(timev[day]).strftime('%Y-%m-%d')
 print("No. of Day:", day,"Date:", date)   
 for j in range(real):
    temp = np.matrix(rfv[j,day,latl:latu,lonl:lonr])
    #print(temp)
 for lt in range(latlen):
  for ln in range(lonlen):
   # Write on the day file
   value = temp[lt,ln]
   f_value = "{:.1f}".format(value)
   print("Temp Value:", value, "format value", f_value)
   fl.write(str(latv[lt])+','+str(lonv[ln])+','+date+','+str(0)+','+str(f_value)+'\n')
   # Also print
   print(latv[lt],lonv[ln],date,str(0),str(f_value))
 #Reset zero matrix
 ghi_temp = np.matrix(np.zeros(latlen*lonlen).reshape(latlen,lonlen))

