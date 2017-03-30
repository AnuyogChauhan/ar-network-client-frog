
from lib.SimpleBroadcast import SimpleBroadcast
from ens import ensclient
from ArPacket import ArPacket
import sys


class ArBroadcastENS(SimpleBroadcast):
    def __init__(self, host2='localhost', port2=5000):
        super(ArBroadcastENS, self).__init__(host1=host2, port1=port2)
        self.identifier = "markmiller.ar-broadcast-frog"
        self.network = "micro-ar-network.test-network"
        self.session = None
        self.my_ens_client = None

    def encodeValue(self, value):
        return value.asBytes()

    def findEndpoints(self):
        self.my_ens_client = ensclient.ENSClient(self.identifier)
        if self.my_ens_client.init():
            self.session = self.my_ens_client.connect(self.network)
            if self.session:
                self.setConnection(self.session.conn)
                self.endpoint = ensclient.ENSEndpoint(self.session.binding["endpoint"])
                print "host {0} port {1}".format(self.endpoint.host, self.endpoint.port)
            else:
                print "failed to connect to ar-network"

        else:
            print "failed to initialize"
            sys.exit(1)

    def close(self):
        if self.my_ens_client is not None:
            self.my_ens_client.close()


if __name__ == "__main__":
    sb = ArBroadcastENS()
    sb.findEndpoints()
    sb.broadcast(ArPacket(10, 0))
    sb.close()
