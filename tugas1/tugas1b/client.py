import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 11000)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    # Send data
    message = 'isi.txt'
    print(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    # amount_received = 0
    # untuk menyimpan file dari server
    isi = open('tulis_isi.txt', 'wb')

    while True:

        data = sock.recv(1024)
        if data:
            # amount_received += len(data)
            isi.write(data)
            print("File diterima!")

        else:
            break

        isi.close()

finally:
    print("closing")
    sock.close()
