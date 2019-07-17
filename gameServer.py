import time
from connectionManager import HostPort
from socketManager import Channel

class GameSession:
    def __init__(self,startPort,firstPlayer):
        self.start = startPort
        self.ports = []
        for x in range(10):
            self.ports.append(startPort + x)
        self.players = []
        self.players.append(firstPlayer)
        self.socks = []
        for x in range(10):
            self.socks.append(None)

#add new player to vacant spot or end of list, if list full return false
    def addPlayer(self,name):
        #check name for originality
        for elm in self.players:
            if(name == elm):
                print("name already taken")
                return False
        i = 0
        for elm in self.players:
            if(elm == None):
                self.players[i] = name
                return True
            i += 1

        if(len(self.players) >= 9):
            return False
        else:
            self.players.append(name)

    #removes player omega LUL
    def removePlayer(self,name):
        i = 0
        for elm in self.players:
            if (elm == name):
                self.players[i] == None
            i += 1

    #translate a player name to its port, and vice versa
    def playerToPort(self,name):
        i = 1
        for elm in self.players:
            if(elm == name):
                return i + self.start
            i += 1

    #safety requirement, port could be out of range of players lists
    #make sure player exist first
    def portToPlayer(self,portNum):
        i = -1
        for port in self.ports:
            if(portNum == port):
                if(i > len(self.players)):
                    print("port out of index")
                    return False
                return self.players[i]
            i += 1
        print("port not in range of host")
        return False

    #return the index of a player, useful for the adjacent ports list
    def playerIndex(name):
        i = 0
        for elm in self.players:
            if(elm == name):
                return i
            i += 1
        return -1


    def end(self):
        c1 = Channel('localhost',10000)
        c1.open()
        message = "end " + str(startPort)
        mess = message.encode()
        c1.sendMessage(mess)
        print(c1.recvMessage())
        c1.close()
        return

class Sed(GameSession):
    def startGame():
        if(len(self.players) < 2):
            print("not enough players")
            return False
        for name in players:
            if(name != None):
                port = playerToPort(name)
                tempHP = HostPort('localhost',port)
                tempHP.start()
                ind = playerIndex(name)
                self.ports[ind] = tempHP
