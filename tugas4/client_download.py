import sys
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8889

server_address = ('127.0.0.1', port)
print(f"mencoba terhubung ke {server_address} port {port}")
sock.connect(server_address)


command = input()
try:
    s = command
    filenya = s.split(" ")
    filenya = filenya[1].strip()
    command+='\n'
    sock.sendall(command.encode())

    ukuran_inbyte = sock.recv(4)
    ukuran_asli = int.from_bytes(ukuran_inbyte,byteorder='big')

    if ukuran_asli != 0:
        ukuran_diterima = 0
        recv_data=b''
        while ukuran_diterima < ukuran_asli:
            data = sock.recv(1)
            if data:
                recv_data+=data
                ukuran_diterima+=len(data)
            else:
                break
        fileclient = open('punyaclient_'+filenya,'wb+')
        fileclient.write(recv_data)
        fileclient.close()
except:
    print('err')
finally:
    response = sock.recv(1024)
    print(response.decode())
    sock.close()