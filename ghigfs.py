import numpy as np
from pydap.client import open_url
#Define lat/lon
lat = 416
lon = 309
#open ncep dods sever
dataset=open_url("http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20190522/gfs_0p25_1hr_00z")
#Download ghi data
rad = dataset['dswrfsfc']
#Filter data for lat/lon site
ghi=rad[0:120,lat,lon]
rad_data = ghi.array[:]
#Open output file and variable lists
daylist =[]
hrlist =[]
ghilist=[]
fl = open('emagfs.csv','w')
#Iterate over time array
hr=ghi.time[:]
for hr_idx in range(len(hr)):
 ghival = rad_data[hr_idx,0,0]
 if ghival > 9999: ghival = 0.0
 ghilist.append(ghival)
#interpolate ghi over 15 min
n = 4
x = np.arange(0, n * len(ghilist), n)       # 0, 4, ..
xx = np.arange((len(ghilist) - 1) * n + 1)  # 0, 1, ..
ghi15 = np.interp(xx, x, ghilist)
for i in range(len(ghi15)):
 print i%96, ghi15[i]
 fl.writelines(str(i%96)+','+str(ghi15[i])+'\n')
fl.close()
 
