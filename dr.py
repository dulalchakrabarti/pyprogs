import sqlite3

conn = sqlite3.connect('dr.db')
print "Opened  dr.db  successfully";

conn.execute('''CREATE TABLE DR
       (COUNT         INTEGER PRIMARY KEY,
       NAME           TEXT,
       LAT            REAL,
       LONG           REAL);''')
print "Table created successfully";

conn.close()
