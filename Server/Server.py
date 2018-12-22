import os
import ssl
from socketserver import ThreadingMixIn, TCPServer, StreamRequestHandler


class SSL_TCPServer(TCPServer):
    def __init__(self,
                 server_address,
                 RequestHandlerClass,
                 certfile,
                 keyfile,
                 ssl_version=ssl.PROTOCOL_TLSv1_2,
                 bind_and_activate=True):
        TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.certfile = certfile
        self.keyfile = keyfile
        self.ssl_version = ssl_version

    def get_request(self):
        newsocket, fromaddr = self.socket.accept()
        connstream = ssl.wrap_socket(newsocket,
                                     server_side=True,
                                     certfile=self.certfile,
                                     keyfile=self.keyfile,
                                     ssl_version=self.ssl_version)
        return connstream, fromaddr


# class SSL_ThreadingTCPServer(ThreadingMixIn, SSL_TCPServer):
#     def __init__(self, host_port_tuple, streamhandler, certfile, keyfile, myparameter, mymethod):
#         SSL_TCPServer.__init__(self, host_port_tuple, streamhandler, certfile, keyfile)
#         self.myparameter = myparameter
#         self.mymethod = mymethod


class ServerHandler(StreamRequestHandler):  # instantiates for each request
    def handle(self):
        data = self.connection.recv(4096)
        print('Incoming: %s' % data)

    def filter(self, data):
        pass

    def write(self, data):
        pass


myparameter = 'I am custom server parameter available from request handler!'


def mymethod():
    print('I am custrom method using custom parameter from request hander!')
    return 'Custom method return'


def runServer():
    server_cert = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'server.crt'
    server_key = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'server.key'
    # serve2r = SSL_TCPServer.__init__(server_address=('127.0.0.1', 5151), RequestHandlerClass=IncomingHandler,
    #                                 certfile=server_cert,
    #                                 keyfile=server_key)

    server = SSL_TCPServer(('127.0.0.1', 5151), ServerHandler, certfile=server_cert, keyfile=server_key)
    try:
        server.serve_forever()
        print("Server Running on port 5151")
    except ssl.SSLError as err:
        print(err)
    finally:
        server.shutdown()
        server.server_close()
