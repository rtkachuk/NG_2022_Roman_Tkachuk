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

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getLogins(db):
    connection = init_conn()
    sql = "SELECT * FROM users;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()

    return rows

def generateUsersHTMLTable(rows):
    usersTable = "<table border='1'>"
    for row in rows:
        usersTable += "<tr>"
        for cell in row:
            usersTable += "<td>" + str(cell) + "</td>"
        usersTable += "</tr>"
    usersTable += "</table>"
    return usersTable

def registerUser(db, login, password):
    connection = init_conn(db)
    sql = "INSERT INTO users(`login`, `password`) VALUES('{}', '{}')".format(login, password)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()