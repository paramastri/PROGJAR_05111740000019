import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8889

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', port)
print(f"mencoba terhubung ke {server_address} port {port}")
sock.connect(server_address)

command = input()
try:
    command+="\n"
    sock.sendall(command.encode())
except:
    print('error')
finally:
    response = sock.recv(1024)
    print(response.decode())
    sock.close()