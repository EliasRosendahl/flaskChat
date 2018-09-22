from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)

socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_event(json):
    emit("responce", json['msg'], broadcast=True)


if __name__ == "__main__":
    app.run()