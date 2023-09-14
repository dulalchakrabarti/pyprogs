import numpy as np
import math
from pydap.client import open_url
#Define lat/lon
lat = raw_input('Latitude(ex, 28.89):')
lon = raw_input('Longitude(ex, 76.68):')
date = raw_input('Date (ex, 20171112):')
time = raw_input('Time (ex, 00):')
la = int(round((float(lat)+90)/.25))
lo = int(round(float(lon)/.25))
print la,lo
#create dictionary to store parameters hourly
db = {}
for idx in range(385):
 db[idx] = []
#open ncep dods sever for 5 days
dataset=open_url("http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs"+date+"/gfs_0p25_1hr_"+time+"z")
#Download presssure data
pres = dataset['pressfc']
#Filter data for lat/lon site
presf=pres[:,la,lo]
presf_data = presf.array[:]
#Download temperature data
temp = dataset['tmpsfc']
#Filter data for lat/lon site
tempf=temp[:,la,lo]
tempf_data = tempf.array[:]
#Download humidity data
hum = dataset['rh2m']
#Filter data for lat/lon site
humf=hum[:,la,lo]
humf_data = humf.array[:]
#Download surface wind data
gust = dataset['gustsfc']
#Filter data for lat/lon site
gustf=gust[:,la,lo]
gustf_data = gustf.array[:]
#Download u10m data
ugrd = dataset['ugrd10m']
#Filter data for lat/lon site
ugrdf=ugrd[:,la,lo]
ugrdf_data = ugrdf.array[:]
#Download v10m data
vgrd = dataset['vgrd10m']
#Filter data for lat/lon site
vgrdf=vgrd[:,la,lo]
vgrdf_data = vgrdf.array[:]
#Iterate over time array
hr=pres.time[:]
for hr_idx in range(len(hr)):
 presval = round(presf_data[hr_idx,0,0],1)
 db[hr_idx].append(presval)
 tempval = round(tempf_data[hr_idx,0,0],1)
 db[hr_idx].append(tempval)
 humval = round(humf_data[hr_idx,0,0],1)
 db[hr_idx].append(humval)
 gustval = round(gustf_data[hr_idx,0,0],1)
 db[hr_idx].append(gustval)
 ugrdval = ugrdf_data[hr_idx,0,0]
 vgrdval = vgrdf_data[hr_idx,0,0]
 wind_speed = 2*math.sqrt(ugrdval*ugrdval+ vgrdval*vgrdval)
 wind_speed = round(wind_speed,1)
 db[hr_idx].append(wind_speed)
 wind_dir = (180/3.142)*math.atan2(ugrdval,vgrdval)+180
 wind_dir = round(wind_dir,1)
 db[hr_idx].append(wind_dir)
fl = open('maruti.csv','w')
fl.writelines(','+'Location'+','+'Forecast'+','+'Dated'+','\
+date[6:8]+'.'+date[4:6]+'.'+date[:4]+','+'Lat:28.892695'+','+'Long:76.681341'+','+'\n')
fl.writelines('Day'+','+'Hour(UTC)'+','+'Surface Pressure(Pa)'+','+'Surface Temperature(K)'+','+'Relative Humidity(%)'\
+','+'Surface Wind Speed Gust(m/s)'+','+'10m Wind Speed(m/s)'+','+'10m Wind Direction(deg)'+'\n')
#Iterate over time array
def flatten(xx):
    for i in xx:
     print i,
hr=len(db)
for hr_idx in range(hr):
 if len(db[hr_idx]) > 0:
  print hr_idx/24,hr_idx,
  flatten(db[hr_idx])
  print
  fl.writelines(str(hr_idx/24)+','+str(hr_idx)+',')
  for i in db[hr_idx]:
   fl.writelines(str(i)+',')
  fl.writelines('\n')
fl.close()

