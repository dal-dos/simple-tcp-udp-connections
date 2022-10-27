import socket


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen()

connected = True

while connected:
    client,addr = server_socket.accept()

    data = client.recv(1024)
    print(str(data.decode()))
    msg = "back at you"
    client.send(msg.encode())
    connected = False
    
server_socket.close()