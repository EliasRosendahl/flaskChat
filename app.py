from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

from flaskChat.chatLog import ChatLog

app = Flask(__name__)
socketio = SocketIO(app)



@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connectEvent")
def handle_new_connection(json):
    emit("connectResponce", ChatLog.read())

@socketio.on("message")
def handle_event(json):
    ChatLog.append(json['msg'])
    emit("responce", json['msg'], broadcast=True)


if __name__ == "__main__":
    app.run()