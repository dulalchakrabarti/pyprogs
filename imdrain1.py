#from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim
#import tabula
#geolocator = GoogleV3()
geolocator = Nominatim()
#tabula.convert_into("rf.pdf", "rf.csv", output_format="csv",pages='all')
fl = open('aws.csv')
gl = open('rflatlong.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 try:
  location = geolocator.geocode(line[1])
  if location:
   print line[1],location.latitude, location.longitude,line[2]
   gl.writelines( line[1]+','+str(location.latitude)+','+str(location.longitude)+','+line[2]+'\n' )
 except:
  print 'Not found....'+line[1]
 line = fl.readline()
 line = line.strip('\n')
fl.close()

