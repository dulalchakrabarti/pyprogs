from math import radians, cos, sin, asin, sqrt
def dist(lat1, long1, lat2, long2):
    """
Replicating the same formula as mentioned in Wiki
    """
    # convert decimal degrees to radians 
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # haversine formula 
    dlon = long2 - long1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km
#URL=
#"https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?file=gfs.t00z.pgrb2.0p25.f000&lev_10_m_above_ground=on&lev_2_m_above_ground=on&lev_entire_atmosphere=on&lev_surface=on&var_APCP=on&var_GUST=on&var_RH=on&var_TCDC=on&var_TMP=on&var_UGRD=on&var_VGRD=on&var_VIS=on&subregion=&leftlon=77&rightlon=84&toplat=32&bottomlat=25&dir=%2Fgfs.20220701%2F00%2Fatmos"
#"https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?file=gfs.t00z.pgrb2.0p25.f000&lev_10_m_above_ground=on&lev_2_m_above_ground=on&lev_entire_atmosphere=on&lev_surface=on&var_APCP=on&var_GUST=on&var_RH=on&var_TCDC=on&var_TMP=on&var_UGRD=on&var_VGRD=on&var_VIS=on&subregion=&leftlon=77&rightlon=84&toplat=32&bottomlat=25&dir=%2Fgfs.20220701%2F00%2Fatmos"
import pandas as pd
import xarray as xr
import numpy as np
df = pd.read_csv('pwc.csv')
la = df.lat.tolist()
lo = df.lon.tolist()
stn = df.name.tolist()
#pwc = [(la[i],lo[i]) for i in range(len(la))]
#print(lalo)
#print(stn)
ds = xr.open_dataset('up1.grb', engine='cfgrib')
print(ds)
lat = ds.u10.latitude.data
lon = ds.u10.longitude.data
#lalo = [(lat[i],lon[i]) for i in range(len(la))]
inp1 = [[i,j,k] for i,j,k in zip(la,lo,stn)]
inp2 = [[i,j] for i,j in zip(lat,lon)]
l1 = len(inp1)
l2 = len(inp2)
count=0
for n in range(l1):
 dt = []
 for m in range(l2):
  d = dist(inp1[n][0],inp1[n][1],inp2[m][0],inp2[m][1])
  #print(d,inp1[n][0],inp1[n][1],inp2[m][0],inp2[m][1])
  dt.append([d,inp1[n][0],inp1[n][1],inp1[n][2],inp2[m][0],inp2[m][1]])
  count+=1
 xx=[dt[i][0] for i in range(len(dt))]
 pmin = min(xx)
 ptr = xx.index(pmin)
 print(ptr,dt[ptr])
 '''  
v = ds.vis.data
v = v/1000                   #visibility
gus = ds.gust.data           #gust
temp = ds.t.data - 273.15    #air temperature
rain = ds.tp.data            #precipitation
cloud = ds.acpcp.data        #cloud cover
rh = ds.r.data               # humidity
for i in range(len(lat)):
 for j in range(len(lon)):
  print(lat[i],lon[j],v[i,j],gus[i,j],temp[i,j],rain[i,j],cloud[i,j],rh[i,j])
'''
