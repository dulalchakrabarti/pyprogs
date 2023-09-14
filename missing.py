from geopy.geocoders import Nominatim
import tabula
geolocator = Nominatim(user_agent="missing.py")
gl = open('missing_latlon.csv','w')
count = 0
lines = [line.rstrip('\n') for line in open('missing.csv')]
count=0
for line in lines:
 line = line.split(',')
 try:
  print(line[0])
  location = geolocator.geocode(line[0])
  print(line[0]+','+str(location.latitude)+','+str(location.longitude))
  gl.write( line[0]+','+str(location.latitude)+','+str(location.longitude)+'\n' )
 except:
  print('Not found....'+line[0])
 count+=1
print(count)

