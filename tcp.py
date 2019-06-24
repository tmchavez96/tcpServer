import socket
import sys
from sed import Sed

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
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        # Clean up the connection
        connection.close()
