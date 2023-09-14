#Python script to generate unique id from lat/lon
#Author: Dulal Chakrabarti
#Date:13.7.2022
# for 5 m resolution
lat = input('latitude[25.4763]:'or 25.4763)
y = int(((float(lat)+90)*40000)+1)
print(lat,y)
lon = input('longitude[80.3395]:' or 80.3395)
x = int(((float(lon))*40000))
print(lon,x)
print(float(x/40000))
uid = str(y)+str(x)
print(uid)
minlat=1
minlon=71
maxlat=41
maxlon=96
miny=int(((float(minlat)+90)*40000)+1)
minx=int((float(minlon))*40000)
print('Minimum uid:lat=1/lon=71',str(miny)+str(minx))
maxy=int(((float(maxlat)+90)*40000)+1)
maxx=int(((float(maxlon))*40000))
print('Maximum uid:lat=41,lon=96',str(maxy)+str(maxx))
# forecast grid
yy = int(float(y/40000)*4)+1
xx =int((float(x/40000))*4)
print(yy,xx)


