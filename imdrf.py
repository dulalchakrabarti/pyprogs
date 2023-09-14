#from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim
import tabula
#geolocator = GoogleV3()
geolocator = Nominatim(user_agent="imdrf.py")
tabula.convert_into("rf.pdf", "rf.csv", output_format="csv",pages='all')
fl = open('rf.csv')
gl = open('rflatlong.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 if line[0].isdigit():
  if line[1] == '':
   try:
    location = geolocator.geocode(line[2])
    if location:
     if location.latitude > 0.0 and location.latitude < 40.0 and location.longitude > 60.0 and location.longitude < 100.0:
      print(line[2],location.latitude, location.longitude,line[5])
      gl.writelines( line[2]+','+str(location.latitude)+','+str(location.longitude)+','+line[5]+'\n' )
   except: 
    print('Not found....'+line[2])
  else:
   try:
    location = geolocator.geocode(line[1])
    if location: 
     if location.latitude > 0.0 and location.latitude < 40.0 and location.longitude > 60.0 and location.longitude < 100.0:
      print(line[1],location.latitude, location.longitude,line[2])
      gl.writelines( line[1]+','+str(location.latitude)+','+str(location.longitude)+','+line[2]+'\n' )
   except:
    print('Not found....'+line[1])
 line = fl.readline()
 line = line.strip('\n')
fl.close()



