import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', 
                        password='mysecretpassword', host='localhost')
cursor = conn.cursor()
cursor.execute("SELECT * FROM pg_catalog.pg_tables;")

for row in cursor:
    print (row)