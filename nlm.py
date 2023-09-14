from geopy.geocoders import Nominatim
fl = open('nlm.csv','w')
txt1 = 'sn'+','+'lat'+','+'lon'+','+'name'
fl.write(txt1+'\n')
txt2 = ['Kakinada', 'Ramagundam', 'Buldhana', 'Dahanu']
geolocator = Nominatim(user_agent="season.py")
count = 0
for item in txt2:
 location = geolocator.geocode(item)
 if location:
  count +=1
  print(str(count)+','+str(location.latitude)+','+str(location.longitude)+','+item)
  fl.write(str(count)+','+str(location.latitude)+','+str(location.longitude)+','+item+'\n')
#7.0°N, 94.5°E, Kakinada, Ramagundam, Buldana,Dahanu, Long. 71.0° E/Lat. 19.5° N
