from geopy.geocoders import Nominatim
fl = open('pwc.csv','w')
txt1 = 'sn'+','+'lat'+','+'lon'+','+'name'
fl.write(txt1+'\n')
txt2 = city = ['Agra','Aligarh','Banda','Jhansi','Kanpur','Mathura','Prayagraj','Azamgarh','Basti','Ghazipur','Gorakhpur','Varanasi','Shahjahanpur','Sultanpur','Lucknow', 'Gonda','Bareilly','Meerut','Moradabad']
geolocator = Nominatim(user_agent="up_ref.py")
count = 0
for item in txt2:
 location = geolocator.geocode(item)
 if location:
  count +=1
  print(str(count)+','+str(location.latitude)+','+str(location.longitude)+','+item)
  fl.write(str(count)+','+str(location.latitude)+','+str(location.longitude)+','+item+'\n')


