from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask("Frontend")

@app.route('/')
def time():
    return render_template("index.html", time=str(datetime.now()))

app.run(host="0.0.0.0", port=8080)