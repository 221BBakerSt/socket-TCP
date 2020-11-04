from socket import *
from threading import Thread
'''
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(address)
serverSocket.listen(5)
newClientSocket, clientAddress = serverSocket.accept()
#receive()
#send()
close()
'''
class TCPserver(object):
    
    def __init__(self, address, serverSocket = None):
        
        #Create a socket
        if serverSocket is None:
            self.serverSocket = socket(AF_INET, SOCK_STREAM)
        else:
            self.serverSocket = serverSocket
        
        #Bind local info
        self.address = address
        self.serverSocket.bind(self.address)
        print('bind finished')

        #A socket is active, turn it into passive with 'listen' method so can receive connections
        self.serverSocket.listen(5)
        print('listen finished')

    def __del__(self):
        #Close the socket that serves this client
        #If this client needs service again, we can only create a new socket
        #newClientSocket.close()

        #Close the listening socket. This means the whole program can no longer receive any connections from clients
        print('close serverSocket finished')
        self.serverSocket.close()        

    def receive(self):
        #If a new client requests to build a connection, a new socket will be created to serve that client
        #newClientSocket is just for that, and serverSocket can be ready to serve other clients
        global newClientSocket, clientAddress
        newClientSocket, clientAddress = self.serverSocket.accept()
        print('accept finished')

        #Receive data (maximum 1024 bytes) from a client
        for _ in range(3):
            recvData = newClientSocket.recv(1024)
            recvData = recvData.decode('gb2312')
            print(f'{recvData} received from {str(clientAddress)}')

    def send(self, msg):
        #Encode the message
        msg = msg.encode('gb2312')
        #Send data to the client
        newClientSocket.send(msg)


if __name__ == '__main__':
    address = ('', 8894) #only visible within the same machine
    msg = 'We received your data!好的'
    server = TCPserver(address)
    task1 = Thread(target = server.receive)
    task2 = Thread(target = server.send, args = (msg,))
    task1.start()
    task1.join()
    task2.start()