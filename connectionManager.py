import socket
import sys

class HostPort:
    def __init__(self,addy,port):
        self.address = addy
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = None
        self.client_address = None

    def start(self):
        sock = self.sock
        server_address = (self.address, self.port)
        sock.bind(server_address)
        sockCount = 10010
        sock.listen(1)

    def getConnection(self):
        sock = self.sock
        self.connection,self.client_address = sock.accept()


    def recvMessage(self):
        sock = self.sock
        rv = ''
        data = self.connection.recv(16)
        datas = data.decode()
        rv = datas
        print("recv ended")
        return rv

    def sendMessage(self, message):
        self.connection.sendall(message)

    def close(self):
        self.connection.close()
