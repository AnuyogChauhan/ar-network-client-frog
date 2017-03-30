
import sys
import socket
from lib.SimpleClient import SimpleClient
from ens import ensclient
from ArPacket import ArPacket


class ArClientENS(SimpleClient):
    def __init__(self, host2='localhost', port2=5000):
        super(ArClientENS, self).__init__(host2, port2)
        self.identifier = "markmiller.ar-client-frog"
        self.network = "micro-ar-network.test-network"
        self.session = None
        self.my_ens_client = None

    def closestEndpoint(ensEndpoints):
        pass
        # TODO: find and return closest of ENSEndpoints

    def decodeValue(self, value):
        return ArPacket.fromBytes(value)

    def useValue(self, value):
        print(value.toString())

    def findEndpoints(self):
        self.my_ens_client = ensclient.ENSClient(self.identifier)
        if self.my_ens_client.init():
            self.session = self.my_ens_client.connect(self.network)
            if self.session:
                self.setConnection(self.session.conn)
                self.endpoint = ensclient.ENSEndpoint(self.session.binding["endpoint"])
                print("host {0} port {1}".format(self.endpoint.host, self.endpoint.port))
            else:
                print("failed to connect to ar-network")

        else:
            print("failed to initialize")
            sys.exit(1)

    def close(self):
        if self.my_ens_client is not None:
            self.my_ens_client.close()


if __name__ == "__main__":
    sc = ArClientENS()
    sc.findEndpoints()
    try:
        sc.subscribe()
    except KeyboardInterrupt:
        sc.close()

