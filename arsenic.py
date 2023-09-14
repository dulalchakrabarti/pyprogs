from geopy.geocoders import Nominatim
geolocator = Nominatim()
gl = open('arslatlon.csv','w')
with open("arsenic.csv") as fl:
 lines = [x.strip() for x in fl.readlines()]
 for line in lines:
  line = line.split(',')
  try:
   location = geolocator.geocode(line[1])
   if location.latitude > 0.0 and location.latitude < 40.0 and location.longitude > 60.0 and location.longitude < 100.0:
     print location.latitude, location.longitude,line[4]
     gl.writelines( line[1]+','+str(location.latitude)+','+str(location.longitude)+','+line[4]+'\n' )
  except: 
   print 'Not found....'+line[1]

