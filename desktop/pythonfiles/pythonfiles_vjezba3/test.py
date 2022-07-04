import socket
import sys
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket uspješno ostvaren")
except socket.error as err:
    print("Stvaranje socketa neuspješno %s" % (err))
port = 80
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("Došlo je do errora postavljanje hosta")
    sys.exit()
s.connect((host_ip,port))
print ("Socket je uspješno povezan na google")