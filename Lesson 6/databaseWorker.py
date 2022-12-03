import sqlite3
from sqlite3 import Error

def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn    

def init_tables(connection):
    sql = "CREATE TABLE IF NOT EXISTS users( id integer PRIMARY KEY, login text NOT NULL, password text NOT NULL);"
    connection.execute(sql)

def getLogins(connection):
    sql = "SELECT * FROM users;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows

def registerUser(connection, login, password):
    sql = "INSERT INTO users(`login`, `password`) VALUES('{}', '{}')".format(login, password)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()