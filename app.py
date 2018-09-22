from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
socketio = SocketIO(app)

chatLog = ""


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connectEvent")
def handle_new_connection(json):
    global chatLog
    emit("connectResponce", chatLog)

@socketio.on("message")
def handle_event(json):
    global chatLog
    chatLog += json['msg'] + "\n"
    emit("responce", json['msg'], broadcast=True)


if __name__ == "__main__":
    app.run()