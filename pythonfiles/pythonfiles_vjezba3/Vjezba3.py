import socket
#socket objekt je kreiran za komunikaciju

socket_na_klijentu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#spajanje na web server na port 80

socket_na_klijentu.connect(("www.google.com", 80))