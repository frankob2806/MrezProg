import socket
socket_na_serveru = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#povezivanje ili bindanje socketa na javni host i poznati port

socket_na_serveru.bind((socket.gethostname(), 8080))
#postani serverski socket i slusaj dolazne komunikacije

socket_na_serveru.listen(5)
