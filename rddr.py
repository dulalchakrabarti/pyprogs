import sqlite3

conn = sqlite3.connect('dr.db')
print "Opened database successfully";

cursor = conn.execute("SELECT count,name, lat, long from DR")
for row in cursor:
   print "count = ", row[0]
   print "name = ", row[1]
   print "lat= ", row[2]
   print "lon = ", row[3], "\n"

print "Operation done successfully";
conn.close()
