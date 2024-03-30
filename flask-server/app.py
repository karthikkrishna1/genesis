import os
from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

email_to_sid_map = {}
sid_to_email_map = {}

@socketio.on('connect')
def handle_connect():
    print('Socket Connected', request.sid)

@socketio.on('room:join')
def handle_room_join(data):
    email = data['email']
    room = data['room']
    email_to_sid_map[email] = request.sid
    sid_to_email_map[request.sid] = email
    emit('user:joined', {'email': email, 'id': request.sid}, room=room)
    join_room(room)
    emit('room:join', data, room=request.sid)

@socketio.on('user:call')
def handle_user_call(data):
    to = data['to']
    offer = data['offer']
    emit('incomming:call', {'from': request.sid, 'offer': offer}, room=to)

@socketio.on('call:accepted')
def handle_call_accepted(data):
    to = data['to']
    ans = data['ans']
    emit('call:accepted', {'from': request.sid, 'ans': ans}, room=to)

@socketio.on('peer:nego:needed')
def handle_peer_nego_needed(data):
    to = data['to']
    offer = data['offer']
    emit('peer:nego:needed', {'from': request.sid, 'offer': offer}, room=to)

@socketio.on('peer:nego:done')
def handle_peer_nego_done(data):
    to = data['to']
    ans = data['ans']
    emit('peer:nego:final', {'from': request.sid, 'ans': ans}, room=to)

if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()
    app.run(debug=True)