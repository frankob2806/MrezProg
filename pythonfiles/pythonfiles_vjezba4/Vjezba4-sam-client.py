# -- coding: utf-8 --
#echo_client.py
from ast import Expression
import socket

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host,port))

client_socket.sendall(b'Tekst koji se salje serveru')

data = client_socket.recv(1024)

print (data)
client_socket.close()



print("Unesite vas input:")
input_korisnika = input()

if(input_korisnika == 'franko biliskov'):
    print('Molim odaberite drugi input')
if(input_korisnika == 'Franko Biliskov'):
    print('Molim odaberite drugi input')
if(input_korisnika == 'franko_biliskov'):
    print('Molim odaberite drugi input')
if(input_korisnika == 'Franko_Biliskov'):
    print('Molim odaberite drugi input')



# py desktop/pythonfiles/pythonfiles_vjezba4/vjezba4-sam-server.py
# Pokusa san napravit raw_input umisto input ali mi izbacuje gresku da ne postoji ta opcija
# Koliko san skuzia raw_input je koristen u python 2, a samo input u python 3.
#try: 
 #   if input_korisnika : ('franko biliskov')
  #  print ("Molim unesite drugi input")

#except:
#    print (input_korisnika)