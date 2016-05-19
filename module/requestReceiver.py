import SocketServer
import threading
from socket import *
#for communicate with subPi & MainPi

status = 0

def start():

    class RequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
	    global status
	    self.data = self.request.recv(1024).strip()
            if self.data == "00":
               status = 1
            elif self.data == "11":
                status = 3
            elif self.data == "22":
                self.request.sendall(b"emer")


    server = SocketServer.TCPServer(("192.168.43.61",9001), RequestHandler)

    threading._start_new_thread(server.serve_forever,())
    return 0


def get_status():
    return status

def set_status():
    global status
    status = 0

def send_data():
    appSock = socket(AF_INET, SOCK_STREAM)
    appSock.connect(('192.168.43.61',9001))
    appSock.send(b'22')
    appSock.close()
