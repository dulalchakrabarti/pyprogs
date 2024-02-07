import pandas as pd
from geopy.geocoders import Nominatim
import time
import tabula
import os
# convert PDF into CSV file
tabula.convert_into("rf.pdf", "rf.csv", output_format="csv", pages='all')
gl = open('dist_lat_lon.csv','w')
geolocator = Nominatim(user_agent="geoapiExercises")
df = pd.read_csv('rf.csv', delimiter=',',header=None)
lst = [list(row) for row in df.values]
count=0
for num in range(len(lst)):
 txt = lst[num]
 if str(txt[0]).isdigit():
  buf = txt[5].split()
  #print(txt[1],txt[2],buf[-2],buf[-1])
  add =txt[1]
  location = geolocator.geocode(add)
  if location != None:
   print(add,location.latitude, location.longitude,txt[2],buf[-2],buf[-1])
   gl.write(add+','+str(location.latitude)+','+str(location.longitude)+','+str(txt[2])+','+str(buf[-2])+','+str(buf[-1])+'\n')
  count+=1
  time.sleep(1.0)
print(count)