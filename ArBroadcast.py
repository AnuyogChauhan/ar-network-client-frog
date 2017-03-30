
import time
import socket
from lib.SimpleBroadcast import SimpleBroadcast
from ArPacket import ArPacket
from time import sleep


class ArBroadcast(SimpleBroadcast):
    def __init__(self, host2='localhost', port2=5000):
        super(ArBroadcast, self).__init__(host1=host2, port1=port2)

    def encodeValue(self, value):
        return value.asBytes()


if __name__ == "__main__":
    sb = ArBroadcast('fast.secret.equipment')
    #sb.connect()
    #sb = ArBroadcast(socket.gethostname())
    items = list()
    start = time.time()
    for i in range(0, 30):
        j = 60 - i
        ap = ArPacket(i, j)
        sb.broadcast(ap)
    print("time to send {0}".format(time.time() - start))
    sb.close()
