from geopy.geocoders import Nominatim
#from geopy.geocoders import GoogleV3
geolocator = Nominatim()
#geolocator = GoogleV3()
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
ars = {}
gl = open('arslatlon_max.csv','w')
with open("arsenic.csv") as fl:
 lines = [x.strip() for x in fl.readlines()]
 for line in lines:
  line = line.split(',')
  dis = line[1]
  print dis
  try:
   location = geolocator.geocode(dis)
   lat = location.latitude
   lon = location.longitude
   val = float(line[4])
   if ars.has_key(dis):
    if ars[dis][2] < val:
     ars[dis] = [lat,lon,val]
   else:
    ars[dis] = [lat,lon,val]
  except:
   print line
keylist = ars.keys()
keylist.sort()
for key in keylist:
 print key,ars[key]
 gl.write(str(key)+','+str(ars[key][0])+','+str(ars[key][1])+','+str(ars[key][2])+'\n')
'''
from geopy.geocoders import Nominatim
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
ars = {}
geolocator = Nominatim()
gl = open('arslatlon_max.csv','w')
with open("arslatlon.csv") as fl:
 lines = [x.strip() for x in fl.readlines()]
 for line in lines:
  line = line.split(',')
  if ars.has_key(line[0]):
   print ars[line[0]],line
   if float(ars[line[0]][2]) < float(line[3]):
    ars[line[0]][2] = line[3]
  else:
    ars[line[0]] = line[1:]
'''
