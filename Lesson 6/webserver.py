from databaseWorker import *
from flask import Flask, render_template, redirect, request

app = Flask("DatabaseExample")
prepareDb("users.db")

@app.route('/')
def index():
    rows = getLogins("users.db")
    return render_template("index.html", users=generateUsersHTMLTable(rows))

@app.route('/register')
def register():
    login = request.args.get('login')
    password = request.args.get('password')
    registerUser("users.db", login, password)
    return redirect('/')

app.run(host='0.0.0.0', port=8081)