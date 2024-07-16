from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import json
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

DATABASE_DIR = 'Database'
USERS_FILE = os.path.join(DATABASE_DIR, 'users.json')
SIGNUP_LOG_FILE = os.path.join(DATABASE_DIR, 'signup_log.json')
LOGIN_LOG_FILE = os.path.join(DATABASE_DIR, 'login_log.json')

if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)


def load_users():
    if os.path.isfile(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)


def log_event(log_file, event):
    with open(log_file, 'a') as f:
        f.write(json.dumps(event) + '\n')


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = load_users()
    if any(user['username'] == username for user in users):
        return jsonify({"message": "Username already exists"}), 400

    user = {'username': username, 'password': password, 'online': False}
    users.append(user)
    save_users(users)

    log_event(SIGNUP_LOG_FILE, {'username': username, 'timestamp': str(datetime.now()), 'event': 'signup'})

    return jsonify({"message": "Signup successful"}), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            user['online'] = True
            save_users(users)
            log_event(LOGIN_LOG_FILE, {'username': username, 'timestamp': str(datetime.now()), 'event': 'login'})
            socketio.emit('user_online', {'username': username})
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    username = data.get('username')

    users = load_users()
    for user in users:
        if user['username'] == username:
            user['online'] = False
            save_users(users)
            log_event(LOGIN_LOG_FILE, {'username': username, 'timestamp': str(datetime.now()), 'event': 'logout'})
            socketio.emit('user_offline', {'username': username})
            return jsonify({"message": "Logout successful"}), 200

    return jsonify({"message": "Logout failed"}), 400


@app.route('/online_users', methods=['GET'])
def online_users():
    users = load_users()
    online_users = [user['username'] for user in users if user['online']]
    return jsonify({"online_users": online_users}), 200


@socketio.on('connect')
def handle_connect():
    pass


@socketio.on('disconnect')
def handle_disconnect():
    pass


@socketio.on('invite')
def handle_invite(data):
    inviter = data.get('inviter')
    invitee = data.get('invitee')
    invitee_sid = get_user_sid(invitee)
    if invitee_sid:
        emit('receive_invite', {'inviter': inviter}, room=invitee_sid)


user_sids = {}


@socketio.on('register')
def handle_register(data):
    username = data.get('username')
    user_sids[username] = request.sid


def get_user_sid(username):
    return user_sids.get(username)


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
