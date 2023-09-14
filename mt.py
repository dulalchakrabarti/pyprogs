from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="season.py")
line = 'AHMEDABAD,RAJGARH,PENDRA ROAD,JHARSUGUDA,BALASORE'
line = line.split(',')
line = [x.strip() for x in line]
fl = open('mt.csv','w')
for i in line:
 try:
  location = geolocator.geocode(i)
  print(i,location.latitude, location.longitude)
  fl.writelines( i +','+str(location.latitude)+','+str(location.longitude)+'\n' )
 except:
  print('Not found....',i)
fl.close()
