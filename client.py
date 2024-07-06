import socket
import threading
from tkinter import messagebox
from signupPage import signupGui
from loginPage import loginGui
from menuPage import menuGui

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5555

client_socket = None
token = None

def connect_to_server():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    return client_socket

def send_message(sock, message):
    sock.send(message.encode())

def receive_messages():
    global token
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                handle_message(message)
        except Exception as e:
            print(f"Error receiving message: {str(e)}")
            break

def handle_message(message):
    global token
    command, *params = message.split(':')
    if command == "LOGIN_SUCCESS":
        token = params[0]
        messagebox.showinfo("Success", "Login successful!")
        menuGui.show_menu_window()
    elif command == "LOGIN_FAILURE":
        messagebox.showerror("Error", "Login failed. Please check your username and password.")
    elif command == "SIGNUP_SUCCESS":
        messagebox.showinfo("Success", "Signup successful! Please log in.")
        loginGui.show_login_window()
    elif command == "SIGNUP_FAILURE":
        messagebox.showerror("Error", "Signup failed. Username or email may already be taken.")
    elif command == "USER_LIST":
        online_users = params[0].split(',')
        menuGui.update_online_users(online_users)
    elif command == "INVITE":
        from_user = params[0]
        response = messagebox.askyesno("Game Invitation", f"You have been invited to a game by {from_user}. Do you accept?")
        if response:
            send_message(client_socket, f"INVITE_RESPONSE:{from_user}:ACCEPT")
            from gamePage import gameBoardGui  # Import locally to avoid circular import
            gameBoardGui.show_game_board_window(from_user, 'P2P')
        else:
            send_message(client_socket, f"INVITE_RESPONSE:{from_user}:REJECT")
    elif command == "INVITE_RESPONSE":
        response = params[0]
        if response == "ACCEPT":
            messagebox.showinfo("Info", "Your invitation has been accepted.")
            from gamePage import gameBoardGui  # Import locally to avoid circular import
            gameBoardGui.show_game_board_window(params[1], 'P2P')
        else:
            messagebox.showinfo("Info", "Your invitation has been rejected.")
    elif command == "MOVE":
        from_user = params[0]
        move = params[1]
        from gamePage import gameBoardGui  # Import locally to avoid circular import
        gameBoardGui.update_game_board(from_user, move)

def login(username, password):
    send_message(client_socket, f"LOGIN:{username}:{password}")

def signup(username, email, password):
    send_message(client_socket, f"SIGNUP:{username}:{email}:{password}")

def fetch_users():
    send_message(client_socket, f"FETCH_USERS:{token}")

def send_invite(to_user):
    send_message(client_socket, f"INVITE:{to_user}")

def send_invite_response(from_user, response):
    send_message(client_socket, f"INVITE_RESPONSE:{from_user}:{response}")

def send_move(to_user, move):
    send_message(client_socket, f"MOVE:{to_user}:{move}")

def start_receiving_thread():
    receiving_thread = threading.Thread(target=receive_messages)
    receiving_thread.daemon = True
    receiving_thread.start()

if __name__ == "__main__":
    connect_to_server()
    start_receiving_thread()
    loginGui.show_login_window()
    fetch_users()
