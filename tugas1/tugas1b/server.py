import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 11000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    minta = connection.recv(1024)
    isi = open(minta.decode(), 'rb')
    print("Permintaan diterima!")
    while True:
        data = isi.read(1024)
        print(f"received {data}")
        if data:
            connection.sendall(data)
            print("Sedang mengirimkan..")
        else:
           break
    isi.close()
    # Clean up the connection
    connection.close()
    print("Server sudah memutus koneksi!")