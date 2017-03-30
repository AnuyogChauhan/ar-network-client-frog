
import socket
from lib.SimpleClient import SimpleClient
from ArPacket import ArPacket


class ArClient(SimpleClient):
    def __init__(self, host2='localhost', port2=5000):
        super(ArClient, self).__init__(host2, port2)

    def decodeValue(self, value):
        return ArPacket.fromBytes(value)
    
    def useValue(self, value):
        print(value.toString())

if __name__ == "__main__":
    sc = ArClient('slow.secret.equipment')
    #sc = ArClient(socket.gethostname(),5000)
    sc.subscribe()
