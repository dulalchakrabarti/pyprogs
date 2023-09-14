#from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim
import tabula
import re
geolocator = Nominatim(user_agent='dulalchakrabarti@gmail.com')
tabula.convert_into("aq.pdf", "aq.csv", output_format="csv",pages='all')
fl = open('aq.csv')
gl = open('aqlatlong.csv','w')
line = fl.readline()
while line:
 line = line.split(',')
 if re.match('\d',line[0]):
  line1 = line
 elif re.match('\d',line[-2]):
  line1[4] = line1[4]+line[4]
  #print line1
  try:
   location = geolocator.geocode(line1[1])
   if location:
    if location.latitude > 0.0 and location.latitude < 40.0 and location.longitude > 60.0 and location.longitude < 100.0:
     print(line1[1],location.latitude, location.longitude,line1[3])
     gl.writelines( line1[1]+','+str(location.latitude)+','+str(location.longitude)+','+line1[3]+'\n' )
  except: 
   print('Not found....'+line[2])
 line = fl.readline()
 line = line.strip()
fl.close()

'''
 line = line.split(',')
 if line[0].isdigit():
  if line[1] == '':
   try:
    location = geolocator.geocode(line[2])
    if location:
     if location.latitude > 0.0 and location.latitude < 40.0 and location.longitude > 60.0 and location.longitude < 100.0:
      print line[2],location.latitude, location.longitude,line[5]
      gl.writelines( line[2]+','+str(location.latitude)+','+str(location.longitude)+','+line[5]+'\n' )
   except: 
    print 'Not found....'+line[2]
  else:
   try:
    location = geolocator.geocode(line[1])
    if location: 
     if location.latitude > 0.0 and location.latitude < 40.0 and location.longitude > 60.0 and location.longitude < 100.0:
      print line[1],location.latitude, location.longitude,line[2]
      gl.writelines( line[1]+','+str(location.latitude)+','+str(location.longitude)+','+line[2]+'\n' )
   except:
    print 'Not found....'+line[1]
 line = fl.readline()
 line = line.strip('\n')
fl.close()
'''


