from gameServer import *
from connectionManager import HostPort
from socketManager import Channel

def playSed(startPort,playerOne):
    sed = Sed(startPort,playerOne)
    admin = HostPort('localhost',sed.startPort)
    admin.start()
    while True:
        admin.getConnection()
        
