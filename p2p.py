import socket


#client


global client_socket
client_socket = None
token = None

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect_to_server(addr):

    client_socket.connect(addr)
    return client_socket

def send_message(sock, message):
    sock.send(message.encode())

def receive_messages():
        try:
            message = client_socket.recv(1024).decode()
            return message
        except Exception as e:
            print(f"Error receiving message: {str(e)}")



#server

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def server_bind(addr):
    server_socket.bind(addr)
    server_socket.listen(5)
    print("Server started on port 5555")

def server_reply(client,message):
    try:
        client.send(message.encode())
    except socket.error as e:
        str(e)
def serverDisconnect():
    server_socket .close()