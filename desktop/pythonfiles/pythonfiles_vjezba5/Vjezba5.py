#local_machine_info
#datetime library

from ipaddress import ip_address
import socket
import datetime
import sys

print("Vrijeme pokretanja ovog programa:")
print (datetime.datetime.now())

print("Program se izvodi na ovom racunalu:")

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

print("----------------------------------------------------")

print("Molim vas unesite adresu hosta koju zelite testirati:")
input_adrese = input()
print("Skeniram host %s" %input_adrese,"IP adresu: %s")



# py desktop/pythonfiles/pythonfiles_vjezba5/Vjezba5.py