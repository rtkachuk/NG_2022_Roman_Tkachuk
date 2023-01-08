from flask import Flask, request, redirect, make_response
import databaseWorker

app = Flask("Lesson_9")
databaseWorker.prepareDb("chat.db")

def generateResponse(data):
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/send")
def send():
    user = request.args.get('login')
    message = request.args.get('message')
    databaseWorker.addMessage("chat.db", user, message)
    return generateResponse("")

@app.route("/messages")
def messages():
    return generateResponse(databaseWorker.generateChatHTMLTable(databaseWorker.getChat("chat.db")))

app.run(host="0.0.0.0", port=8081)