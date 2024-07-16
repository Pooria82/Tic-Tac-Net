import requests
import json
import asyncio
import websockets
import socketio

base_url = 'http://127.0.0.1:5000'
ws_url = 'http://127.0.0.1:5000'  # Use http for Socket.IO connection

sio = socketio.Client()


@sio.event
def connect():
    print('Connection established')
    sio.emit('register', {'username': current_user})


@sio.event
def disconnect():
    print('Disconnected from server')


@sio.event
def receive_invite(data):
    inviter = data.get('inviter')
    print(f"Received invite from {inviter}")
    response = input(f"Do you want to accept the invite from {inviter}? (yes/no): ")
    if response.lower() == 'yes':
        print("Invite accepted.")
    else:
        print("Invite rejected.")


current_user = None


def main():
    global current_user
    while True:
        print_menu()
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            username, password = login()
            if username:
                current_user = username
                sio.connect(ws_url)
                user_info = {'username': username, 'password': password}
                user_menu(base_url, user_info)
        elif choice == '2':
            signup()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def print_menu():
    print("\n1. Login")
    print("2. Signup")
    print("3. Exit")


def login():
    print("\nLogin:")
    username = input("Enter username: ")
    password = input("Enter password: ")

    login_data = {'username': username, 'password': password}
    response = requests.post(f"{base_url}/login", json=login_data)

    if response.status_code == 200:
        print("Login successful.")
        return username, password
    else:
        print("Login failed. Please check your credentials.")
        return None, None


def signup():
    print("\nSignup:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    signup_data = {'username': username, 'password': password}
    response = requests.post(f"{base_url}/signup", json=signup_data)

    if response.status_code == 200:
        print("Signup successful.")
    else:
        print("Signup failed. Username may already exist.")


def user_menu(base_url, user_info):
    while True:
        print("\nUser Menu:")
        print("1. Match")
        print("2. View Match History")
        print("3. Profile")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            online_users = get_online_users(base_url)
            if online_users:
                print("Online users:", online_users)
                invite_user = input("Enter username to invite for a match: ")
                invite(base_url, user_info['username'], invite_user)
        elif choice == '2':
            view_history(user_info['username'])
        elif choice == '3':
            view_profile(user_info['username'])
        elif choice == '4':
            logout(user_info['username'])
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def get_online_users(base_url):
    response = requests.get(f"{base_url}/online_users")
    if response.status_code == 200:
        return response.json().get('online_users', [])
    else:
        print("Failed to get online users.")
        return []


def invite(base_url, inviter_username, invited_username):
    sio.emit('invite', {'inviter': inviter_username, 'invitee': invited_username})


def view_history(username):
    view_data = {'username': username}
    response = requests.post(f"{base_url}/view", json=view_data)

    if response.status_code == 200:
        print(response.json()['message'])
    else:
        print("Failed to view match history.")


def view_profile(username):
    profile_data = {'username': username}
    response = requests.post(f"{base_url}/profile", json=profile_data)

    if response.status_code == 200:
        print("Profile:", response.json())
    else:
        print("Failed to view profile.")


def logout(username):
    logout_data = {'username': username}
    response = requests.post(f"{base_url}/logout", json=logout_data)

    if response.status_code == 200:
        print("Logout successful.")
    else:
        print("Failed to logout.")


if __name__ == '__main__':
    main()
