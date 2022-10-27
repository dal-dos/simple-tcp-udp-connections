import socket
import time
start = time.perf_counter()

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))

msg = "hello"
client_socket.send(msg.encode())
data = client_socket.recv(1024)
print(str(data.decode()))

client_socket.close()

print("Time:" , time.perf_counter() - start, "seconds")