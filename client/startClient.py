import socket
import sys
from socketManager import Channel


# Create a TCP/IP socket
c1 = Channel('localhost',10000)

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
        c1.open()
        c1.sendMessage(message)
        retmes = c1.recvMessage()

    finally:
        print('closing socket')
        c1.close()

#sock.close()
