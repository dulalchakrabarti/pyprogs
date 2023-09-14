import urllib2
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('dr.db')
print "Opened database successfully";
count=0
cursor = conn.execute("SELECT * FROM DR ORDER BY count DESC LIMIT 1;")
for row in cursor:
   count = row[0]
if count > 0:
 count = count
 name = raw_input('Name:')
 lat = raw_input('Lat:')
 lon = raw_input('Long:')
 count = count + 1
 print name+','+lat+','+lon
 params = (count,name, lat, lon)
 conn.execute("INSERT INTO DR  \
      VALUES (?,?, ?, ?)",params);
count = count
name = raw_input('Name:')
lat = raw_input('Lat:')
lon = raw_input('Long:')
count = count + 1
print name+','+lat+','+lon
params = (count,name, lat, lon)
conn.execute("INSERT INTO DR  \
      VALUES (?,?, ?, ?)",params);


conn.commit()


