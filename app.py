# backend.py
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, host='0.0.0.0', port=5000)  # IP-Adresse deiner VM und Port 5000

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg['text'])
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
