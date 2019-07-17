import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
#sock.connect(server_address)
while True:
    message = ''
    command = input("Enter 's' for start, 'j ****' to join, or 'e' to exit \n")
    if(command == 'e'):
        break
    elif(command[0] == 'j'):
        if(len(command) > 6):
            print("input too large --  should be j XXXX")
            continue
        message = command.encode()
    elif(command == 's'):
        message = command.encode()
    else:
        print("invalid input")
        continue

    try:
        sock.connect(server_address)
        # Send data
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()

#sock.close()
