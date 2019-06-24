#Sed = seven eleven doubles
class Sed:
    def __init__(self,start,size):
        self.start = start
        self.size = size
        self.players = []
        self.openSockets = []

    def addPlayer(playerName):
        self.players.append(playerName)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ("localhost",self.start+len(self.player))
        sock.bind(server_address)
        sock.listen(1)
