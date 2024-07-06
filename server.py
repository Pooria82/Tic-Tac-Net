import socket
import threading
from Database import db_helper
import jwt
import os
import dotenv

dotenv.load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
clients = {}
users = {}


def handle_client(client_socket, addr):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message from {addr}: {message}")
                handle_message(client_socket, addr, message)
        except Exception as e:
            print(f"Error handling message from {addr}: {str(e)}")
            remove_client(client_socket, addr)
            break


def handle_message(client_socket, addr, message):
    command, *params = message.split(':')

    if command == "LOGIN":
        username, password = params
        if db_helper.validate_login(username, password):
            token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
            users[token] = username
            clients[client_socket] = token
            client_socket.send(f"LOGIN_SUCCESS:{token}".encode())
        else:
            client_socket.send("LOGIN_FAILURE".encode())

    elif command == "SIGNUP":
        username, email, password = params
        if db_helper.is_unique_username(username) and db_helper.is_unique_email(email):
            db_helper.save_user_to_db(username, email, password)
            client_socket.send("SIGNUP_SUCCESS".encode())
        else:
            client_socket.send("SIGNUP_FAILURE".encode())

    elif command == "FETCH_USERS":
        token = clients.get(client_socket)
        if token:
            online_users = [users[client_token] for client_token in clients.values() if client_token != token]
            client_socket.send(f"USER_LIST:{','.join(online_users)}".encode())

    elif command == "INVITE":
        from_user = users.get(clients.get(client_socket))
        to_user = params[0]
        to_user_socket = get_socket_by_username(to_user)
        if to_user_socket:
            to_user_socket.send(f"INVITE:{from_user}".encode())

    elif command == "INVITE_RESPONSE":
        from_user = params[0]
        response = params[1]
        from_user_socket = get_socket_by_username(from_user)
        if from_user_socket:
            from_user_socket.send(f"INVITE_RESPONSE:{response}".encode())

    elif command == "MOVE":
        from_user = users.get(clients.get(client_socket))
        to_user = params[0]
        move = params[1]
        to_user_socket = get_socket_by_username(to_user)
        if to_user_socket:
            to_user_socket.send(f"MOVE:{from_user}:{move}".encode())


def get_socket_by_username(username):
    for client_socket, token in clients.items():
        if users.get(token) == username:
            return client_socket
    return None


def remove_client(client_socket, addr):
    token = clients.pop(client_socket, None)
    if token:
        users.pop(token, None)
    client_socket.close()
    print(f"Connection from {addr} closed")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen(5)
    print("Server started on port 5555")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()


if __name__ == "__main__":
    start_server()
