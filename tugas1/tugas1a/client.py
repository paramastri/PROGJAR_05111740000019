import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)


isi = open('isi.txt', 'rb')

try:
    # Send data
    message = isi.read(1024)
    print(f"sending {message}")
    # Look for the response
    # amount_received = 0
    # amount_expected = len(message)
    while message:
        # data = sock.recv(1024)
        # amount_received += len(data)
        # print(f"{data}")
        # sock.sendall(message.encode())
        print("Pesan dibawah ini diterima dari server!")
        sock.send(message)
        message = isi.read(1024)
finally:
    print("closing")
    sock.close()