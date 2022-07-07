import socket
import datetime

print(datetime.datetime.now())

from pythonfiles_vjezba6.localMachineInfo import print_machine_info

print_machine_info()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inputHost = input("Unesite adresu hosta: ")
print("Skeniranje porta za: ", inputHost)

print("Unesite start port i end port:")

startPort = input("Start port=> ")
endPort = input("End port => ")

startPort = int(startPort)
endPort = int(endPort)

def scanner(port):
    try:
        sock.connect((inputHost,port))
        return True
    except:
        return False

for portNumber in range(startPort,endPort):
    print("Skeniranje porta: ", portNumber)
    if scanner(portNumber):
        print('Port: ',portNumber,'/tcp',' je otvoren!')