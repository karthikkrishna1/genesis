import base64
import os
from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS, cross_origin
from google.cloud import storage
from base64 import b64decode
from datetime import datetime
import time
import logging
from model import init_vertex, generate_text

app = Flask(__name__)
CORS(app, origins='*', methods=['GET', 'POST'], allow_headers=['Content-Type'])
socketio = SocketIO(app, cors_allowed_origins="*")

# email_to_sid_map = {}
# sid_to_email_map = {}

# @socketio.on('connect')
# def handle_connect():
#     print('Socket Connected', request.sid)

# @socketio.on('room:join')
# def handle_room_join(data):
#     email = data['email']
#     room = data['room']
#     email_to_sid_map[email] = request.sid
#     sid_to_email_map[request.sid] = email
#     emit('user:joined', {'email': email, 'id': request.sid}, room=room)
#     join_room(room)
#     emit('room:join', data, room=request.sid)

# @socketio.on('user:call')
# def handle_user_call(data):
#     to = data['to']
#     offer = data['offer']
#     emit('incomming:call', {'from': request.sid, 'offer': offer}, room=to)

# @socketio.on('call:accepted')
# def handle_call_accepted(data):
#     to = data['to']
#     ans = data['ans']
#     emit('call:accepted', {'from': request.sid, 'ans': ans}, room=to)

# @socketio.on('peer:nego:needed')
# def handle_peer_nego_needed(data):
#     to = data['to']
#     offer = data['offer']
#     emit('peer:nego:needed', {'from': request.sid, 'offer': offer}, room=to)

# @socketio.on('peer:nego:done')
# def handle_peer_nego_done(data):
#     to = data['to']
#     ans = data['ans']
#     emit('peer:nego:final', {'from': request.sid, 'ans': ans}, room=to)

@socketio.on("connect")
def handle_connect():
    print("Socket Connected", request.sid)
    emit("me", request.sid)

@socketio.on("disconnect")
def handle_disconnect():
    print("Socket Disconnected", request.sid)
    emit("callEnded", broadcast=True)

@socketio.on("callUser")
def handle_call_user(data):
    user_to_call = data["userToCall"]
    signal_data = data["signalData"]
    from_user = data["from"]
    name = data["name"]
    emit("callUser", {"signal": signal_data, "from": from_user, "name": name}, room=user_to_call)

@socketio.on("answerCall")
def handle_answer_call(data):
    to_user = data["to"]
    signal = data["signal"]
    emit("callAccepted", signal, room=to_user)

@app.route('/api/upload', methods=['POST'])
# @cross_origin(origin='localhost', headers=['Content- Type','Authorization'])
def upload_file():
    print('Request Received')
    try:
        image_data = request.json['body']

        image_bytes = base64.b64decode(image_data)

        client = storage.Client()

        bucket = client.get_bucket('animated-scope-418820.appspot.com')
        file_name = "Image-" + datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        blob = bucket.blob(file_name).upload_from_string(image_bytes, content_type='image/png', predefined_acl='publicRead')

        return True, bucket.blob(file_name).public_url
    except:
        logging.error("Error uploading data to GCS")
        return False
    
@app.route('/api/model', methods=['GET'])
@cross_origin()
def get_model_output():
    try:
        client = storage.Client()
        bucket = client.get_bucket('animated-scope-418820.appspot.com')
        blobs = bucket.list_blobs()
        sorted_blobs = sorted(blobs, key=lambda x: x.updated, reverse=True)
        most_recent_blob = sorted_blobs[0]
        model = init_vertex()
        start_time = time.time()
        text = generate_text(model, most_recent_blob.public_url)
        end_time = time.time()
        duration = end_time - start_time
        return {'answer': text, 'duration': duration}
    except:
        logging.error("Error getting model output")
        return False


if __name__ == '__main__':
    app.run(debug=True)