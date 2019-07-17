import socket
import sys
import os
from sed import Sed
from portManager import PM

#starting port = 12000
ports = PM(100)
print(ports)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)
sockCount = 10010

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        #Recieve data in chunks and send it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                dataS = data.decode()
                print("string rep of message = " + dataS)
                if(dataS == 's'):
                    gameAddress = ports.findFirst()
                    retmes = gameAddress.encode()
                    connection.sendall(retmes)
                    break
                else:
                    retmes = 'wasnt a start'
                    print(retmes)
                    connection.sendall(data)
                    break
            else:
                print('no data from', client_address)
                break
    finally:
        # Clean up the connection
        connection.close()
