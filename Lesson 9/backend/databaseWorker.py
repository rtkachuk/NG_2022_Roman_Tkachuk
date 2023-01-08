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
    sql = "CREATE TABLE IF NOT EXISTS chat( id integer PRIMARY KEY, login text NOT NULL, message text NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getChat(name):
    connection = init_conn(name)
    sql = "SELECT * FROM chat;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()

    return rows

def generateChatHTMLTable(rows):
    chatTable = "<table border='1'>"
    for row in rows:
        chatTable += "<tr>"
        for cell in row:
            chatTable += "<td>" + str(cell) + "</td>"
        chatTable += "</tr>"
    chatTable += "</table>"
    return chatTable

def addMessage(db, login, message):
    connection = init_conn(db)
    sql = "INSERT INTO chat(`login`, `message`) VALUES('{}', '{}')".format(login, message)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()