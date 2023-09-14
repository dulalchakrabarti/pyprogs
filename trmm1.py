from pytrmm import TRMM3B42RTFile
trmm_file = TRMM3B42RTFile("3B42RT.2018101106.7.bin.gz")
#print(trmm_file.header())
precip = trmm_file.precip()
y,x = precip.shape
fl = open('trmm.csv','w')
for idy in range(80,340):
 for idx in range(160,800):
  lon = idx*.25
  lat = 60 - idy*.25
  fl.write(str(lat)+','+str(lon)+','+str(precip[idy,idx])+'\n')
  #print lon,lat,precip[idy,idx]

