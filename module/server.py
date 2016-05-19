import os
import sys
from socket import *
from socket import error as socket_error
from threading import *

status = 0
weather = 0

HOST = '192.168.43.61'
PORT = 9001

class ThreadAccept(Thread):                     
                                                
    shutdown = False
    def __init__(self, socket, socketList):     
        Thread.__init__(self)                   
        self.socket = socket
        self.socketList = socketList
        self.childThreads = []
                
    def run(self):
        self.socket.settimeout(0.1)                 
        while ThreadAccept.shutdown == False:
            try:
                                                   
                connection, address = self.socket.accept()        
            except timeout:
                continue
            else:
                self.socketList.append((connection, address))        
                print connection
                print "[connection] : ", address   
                handler = ThreadHandler(connection, address, self.socketList)
                handler.start()
                self.childThreads.append(handler)

    def joinChildThreads(self):
        for thread in self.childThreads:
            thread.join()
     
class ThreadHandler(Thread):
    shutdown = False
    
    def __init__(self, socket, addr, socketList):
        Thread.__init__(self)
        self.socket = socket
        self.addr = addr
        self.socketList = socketList
        
    def run(self):
	global status
        global weather
        self.socket.settimeout(0.1)                
        while ThreadHandler.shutdown == False:
            try:
                data = self.socket.recv(1024)        
            except timeout:
                continue
            except socket_error, e:
                print e
                break                
            else:                
                if not data:                    
                    continue                   
                if data == '/x':              
                    self.socketList.remove((self.socket, self.addr)) 
                    self.socket.close()               
                    self.socket = None
                    print addr, " disconnected"
                    break
                elif data == '00':
		    print('00')
                    status = 1
                elif data == '11':
                    status = 3
                    #print(status)
                elif data[0] == 'w':
                    print data
                    if data == 'wClear':
                        weather = 1 
                elif data == '22':
		    print(data)
                    self.sendMsgToAll(b"emer")
        self.socket.close()
        
    def sendMsgToAll(self, msg):      
        for socket, addr in self.socketList:
            #data = str(self.addr) + ' : ' + msg  
	    print(self.addr)
            socket.send(msg)                  


def serv_start():
    socketList = []                               
    serverSocket = socket(AF_INET, SOCK_STREAM)  
    serverSocket.bind((HOST, PORT))             
    serverSocket.listen(5)                     
    print "Server Start"
    acceptor = ThreadAccept(serverSocket, socketList)  
    acceptor.start()                               

def get_status():
    return status

def set_status():
    global status
    status =0 

def get_weather():
    return weather
def set_weather():
    global weather
    weather = 0

'''
while 1:                                      
    cmd = raw_input('>>')
    if cmd == 'x':                           
      
     
        ThreadHandler.shutdown = True      
        ThreadAccept.shutdown = True
        acceptor.joinChildThreads()
        acceptor.join()                   
        break
print "Server Stop"   
'''
