from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        use_db_query = "use weather"
        show_table_query = "show tables"
        with connection.cursor() as cursor:
            cursor.execute(use_db_query)
            cursor.execute(show_table_query)
            for table in cursor:
             print(table)
except Error as e:
    print(e)
from pymetdecoder import synop as s

synop = "AAXX 01004 88889 12782 61506 10094 20047 30111 40197 53007 60001 81541 333 81656 86070="
output = s.SYNOP().decode(synop)
print(output)

