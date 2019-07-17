import random

#object for managing the available ports to start new games on

def makeKey():
    k = 0
    retStr = ''
    while(k < 4):
        rn = random.randint(97,122)
        retStr = retStr + chr(rn)
        k = k + 1
    return retStr

class PM:
    #initialize a dictionary, the keys are random ascii values (see makeKey above)
    #the values are boolean, true for open and false for taken
    def __init__(self,length):
        self.span = {}
        x = 0
        while(x < length):
            key = makeKey()
            y = self.span.get(key)
            #print("x = " + str(x) + " key = " + str(key))
            if(y == None):
                #print("added key/port")
                self.span[key] = True
                x = x + 1

    #find the first open port and return the key, key is set to taken
    def findFirst(self):
        for key in self.span:
            if(self.span[key] != False):
                self.span[key] = False
                return key
        print("no open ports")
        return None

    #parse dictionary in order to find the designated port num
    def codeToPort(self,code):
        i = 0
        for key in self.span:
            if(key == code):
                return i
            i += 1
        print("code didnt exist")
        return False

    #set the key equal to zero
    def reOpen(self,key):
        self.span[key] = True
