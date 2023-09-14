#from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim
import tabula
#geolocator = GoogleV3()
geolocator = Nominatim(user_agent="season.py")
#tabula.convert_into("rf.pdf", "rf.csv", output_format="csv",pages='all')
fl = open('rf.csv')
gl = open('rfseason.csv','w')
line = fl.readline()
count = 0
while line:
 line = line.split(',')
 if line[0].isdigit():
  if line[1] == '':
   try:
    location = geolocator.geocode(line[2])
    if location:
     tot = line[-1].split()[2]
     print(line[2]+','+str(location.latitude)+','+str(location.longitude)+','+tot[:-1])
     gl.writelines( line[2]+','+str(location.latitude)+','+str(location.longitude)+','+tot[:-1]+'\n' )
   except:
    print('Not found....'+line[2])
  else:
   try:
    location = geolocator.geocode(line[1])
    if location:
     tot = line[-1].split()[2]
     print(line[1]+','+str(location.latitude)+','+str(location.longitude)+','+tot[:-1])
     gl.writelines( line[1]+','+str(location.latitude)+','+str(location.longitude)+','+tot[:-1]+'\n' )
   except:
    print('Not found....'+line[1])
   count+=1
 line = fl.readline()
 line = line.strip('\n')
fl.close()
print(count)



