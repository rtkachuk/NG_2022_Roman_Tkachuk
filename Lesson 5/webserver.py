from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask("TEST")

@app.route('/')
def index():
    tableToPlace = "<table border=\"1\">"
    temp = open("users.txt", "r")
    counter = 1
    for line in temp.readlines():
        tableToPlace += "<tr><td>" + str(counter) + "</td><td>" + line + "</td></tr>"
        counter += 1
    tableToPlace += "</table>"
    temp.close()
    return render_template("index.html", contents=tableToPlace)

@app.route('/process')
def process():
    temp = open("users.txt", "a")
    temp.write(request.args.get('data') + "\n")
    return redirect('/')

app.run(host="0.0.0.0", port=8081)