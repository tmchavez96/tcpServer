import socket
import sys
import os
from connectionManager import HostPort
from portManager import PM

#starting port = 12000
ports = PM(100)
print(ports.span)

#hp = host port
hp = HostPort('localhost', 10000)
hp.start()


while True:
    hp.getConnection()
    try:
        print('connection from', hp.client_address)
        mssg = hp.recvMessage()
        print(mssg)
        if(mssg == 's'):
            gameAddress = ports.findFirst()
            index = ports.codeToPort(gameAddress)
            print("starting on port ",gameAddress)
            #print("pos in dict = ", index)
            retmes = gameAddress.encode()
            hp.sendMessage(retmes)
        elif(mssg == 'j'):
            retmes = 'wasnt a start'
            print(retmes)
            retmes = retmes.encode()
            hp.sendMessage(retmes)
        else:
            print('no data from', hp.client_address)
    finally:
        # Clean up the connection
        hp.close()
