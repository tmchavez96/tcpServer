import socket
import sys

class Channel:
    def __init__(self,address,port):
        self.address = address
        self.port = port

    def open(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = self.sock
        server_address = (self.address, self.port)
        sock.connect(server_address)

    def sendMessage(self, message):
        sock = self.sock
        sock.sendall(message)

    def recvMessage(self):
        sock = self.sock
        rv = ''
        data = sock.recv(16)
        datas = data.decode()
        while(len(datas) > 0):
            print("yeah ight")
            print(datas)
            data = sock.recv(16)
            datas = data.decode()
            rv += datas
        return data

    def close(self):
        sock = self.sock
        sock.close()
