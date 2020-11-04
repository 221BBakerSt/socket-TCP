from socket import *
from threading import Thread

'''
s = socket(AF_INET, SOCK_STREAM)
address = ('www.google.com', 80)
s.connect(address)
msg = 'hello'
msg = msg.encode('utf-8')
s.send(msg)
data = []
recvData = s.recv(1024)
while recvData:
    recvData.decode('utf-8')
    data.append(recvData)
s.close()
print(data)
'''

class TCPclient(object):

    def __init__(self, address, clientSocket = None):
        
        #Create a socket
        if clientSocket is None:
            self.clientSocket = socket(AF_INET, SOCK_STREAM)
        else:
            self.clientSocket = clientSocket

        #Build a connection
        self.address = address
        self.clientSocket.connect(address)
        print('connection finished')

    def __del__(self):
        self.clientSocket.close()

    def receive(self, num):
        for _ in range(num):
            recvData = self.clientSocket.recv(1024)
            recvData = recvData.decode('gb2312')
            print(recvData)

    def send(self, num):
        for _ in range(num):
            msg = input()
            print(msg + ' has been sent!')
            msg = msg.encode('gb2312')
            self.clientSocket.send(msg)
            
if __name__ == '__main__':
    address = ('', 7779)
    server = TCPclient(address) #only visible within the same machine
    taskRecv = Thread(target = server.receive, args = (4,))
    taskSend = Thread(target = server.send, args = (3,))
    taskRecv.start()
    taskSend.start()
    taskRecv.join()
    taskSend.join()