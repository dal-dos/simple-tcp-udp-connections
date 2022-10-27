import socket
import time
start = time.perf_counter()

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = "hello"
client_socket.sendto(msg.encode(),('127.0.0.1',12345))
data,addr = client_socket.recvfrom(1024)
print(str(data.decode()))



client_socket.close()

print("Time:" , time.perf_counter() - start, "seconds")