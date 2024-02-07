import h5py
import numpy as np
fl = open('gpm.csv','w')
f = h5py.File('gpm.h5', 'r')
groups = [ x for x in f.keys() ]
#print(groups)
gridMembers = [ x for x in f['Grid'] ]
#print(gridMembers)
precip = f['Grid/precipitationCal'][0][:][:]
precip = np.transpose(precip)
latitude = f['Grid/lat'][:]
longitude = f['Grid/lon'][:]
x, y = np.float32(np.meshgrid(longitude, latitude))
lon = len(precip[0])
lat = len(precip)
#print latitude.shape,longitude.shape,precip.shape,precip[0].shape
for i in range(0,lon,5):
 for j in range(0,lat,5):
  if i > 2000 and i <2800:
   if j > 900 and j < 1300:
    print(latitude[j],longitude[i],round(precip[j][i],1))
    fl.writelines(str(latitude[j])+','+str(longitude[i])+','+str(round(precip[j][i],1))+'\n')
'''
def print_info(name, obj):
    print name 
    for name, value in obj.attrs.iteritems():
	print name+":", value
	
f = h5py.File('gpm.h5', 'r+')
f.visititems(print_info)
f.close()
'''
