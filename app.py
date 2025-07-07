from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__, template_folder='templates1')  # <-- specify the new folder
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # still the same file name

@socketio.on('message')
def handle_message(data):
    print(f"{data['username']}: {data['message']}")
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
