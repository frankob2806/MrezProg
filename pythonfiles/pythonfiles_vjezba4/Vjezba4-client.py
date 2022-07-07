# -- coding: utf-8 --
#echo_client.py
import socket

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host,port))

client_socket.sendall('Tekst koji se salje serveru')

data = client_socket.recv(1024)

print ('data')
client_socket.close()