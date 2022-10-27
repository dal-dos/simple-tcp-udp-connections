import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1',12345))
connected = True

while connected:
    data,addr = server_socket.recvfrom(1024)
    print(str(data.decode()))
    msg = "back at you"
    server_socket.sendto(msg.encode(),addr)
    connected = False

server_socket.close()