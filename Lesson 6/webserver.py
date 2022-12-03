from databaseWorker import *
from flask import Flask, render_template, redirect, request

app = Flask("DatabaseExample")
conn = init_conn("users.db")
init_tables(conn)
conn.close()

@app.route('/')
def index():
    conn = init_conn("users.db")
    rows = getLogins(conn)
    conn.close()
    usersTable = "<table border='1'>"
    for row in rows:
        usersTable += "<tr>"
        for cell in row:
            usersTable += "<td>" + str(cell) + "</td>"
        usersTable += "</tr>"
    usersTable += "</table>"
    return render_template("index.html", users=usersTable)

@app.route('/register')
def register():
    login = request.args.get('login')
    password = request.args.get('password')
    conn = init_conn("users.db")
    registerUser(conn, login, password)
    conn.close()
    return redirect('/')

app.run(host='0.0.0.0', port=8081)