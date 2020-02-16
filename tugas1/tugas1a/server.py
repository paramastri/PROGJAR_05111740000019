import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 31000)
# server_address = ('localhost', 31001)
# server_address = ('localhost', 31002)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

# File untuk write isi dari client
isi = open('tulis_isi.txt', 'wb')
print("File yang disalin bernama tulis_isi.txt di bagian server.")

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        # print(f"received {data}")
        if data:
            isi.write(data)
            print("sending back data")
            data = connection.recv(1024)

            isi.close()
            print("File sudah disalin!")
            # connection.sendall(data)
        else:
            #print >>sys.stderr, 'no more data from', client_address
            #print(f"no more data from {client_address}")
           break
    # Clean up the connection
    connection.close()
    print("Server sudah memutus koneksi!")