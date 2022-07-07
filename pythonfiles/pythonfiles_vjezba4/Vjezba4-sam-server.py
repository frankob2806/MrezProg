# -- coding: utf-8 --
#echo_server.py
from ipaddress import ip_address
import socket
import datetime
import sys

print (datetime.datetime.now())

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)

if __name__ == '__main__':
    print_machine_info()

host = socket.gethostname()
port = 12345

echo_server = socket.socket()
echo_server.bind ((host, port))
echo_server.listen(5)


print ("Cekam klijenta...")
conn, addr = echo_server.accept()
print ("Spojen: ", addr)


while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)

conn.close()

# py desktop/pythonfiles/pythonfiles_vjezba4/vjezba4-sam-server.py
# Nisan skuzia kako napravit da server saceka sljedeci input, nisam siguran treba li vremenski ili postoji nekakva naredba