import pygrib
grbs = pygrib.open('download.grib')
tot = grbs.messages
for i in range(tot):
 grb = grbs.select(name='2 metre temperature')[i]
 data = grb.values
 lats,lons = grb.latlons()
 print i,data[70,80],lats[70,80],lons[70,80]
'''
 
grb = grbs.select(name='2 metre temperature')[0]
t = grb.values
x = t.shape
lats,lons = grb.latlons()
print lats
print lons

for grb in grbs:
 print grb
tot = grbs.messages
for i in range(tot):
 data = grbs[i+1].values
 lats,lons = grbs[i+1].latlons()
 print data[70,80],lats[70,80],lons[70,80]
'''

