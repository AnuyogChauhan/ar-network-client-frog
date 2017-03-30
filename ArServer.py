
import os

from lib.SimpleServer import SimpleServer


class ArServer(SimpleServer):
    def __init__(self, port2=5000):
        super(ArServer, self).__init__(port1=port2)
        self.port = port2
        if os.getenv("USE_REDIS"):
            if os.getenv("USE_REDIS").find("TRUE") > -1:
                self.initRedis('localhost', 'ar_value')


if __name__ == "__main__":
    print("starting server")
    while True:
        server = ArServer()
        try:
            server.serve()
        except Exception:
            print("restarting server")
