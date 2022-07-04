import socket
s = socket.socket()
print ("Socket uspješno spojen")
port = 80
s.bind(('', port))
print ("Socket je bindan na %s" %(port))
s.listen(5)
print ("Socket sluša")

while True:
    c, addr = s.accept()
    print ('Dobivena konekcija od', addr )
    var = "Hvala na konekciji "
    new = var.encode("ascii")
    c.send(new)
    c.close()
