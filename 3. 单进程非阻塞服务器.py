from socket import *

TCPserver = socket(AF_INET, SOCK_STREAM)
serverAddress = ('', 8890)
TCPserver.bind(serverAddress)

# 让这个服务器socket变为非堵塞
TCPserver.setblocking(False)

TCPserver.listen(5)
clientList = []
while 1:
    # 等待新客户端到来，即完成3次握手的客户端
    try:
        # 没有客户端到来的时候会产生异常
        clientSocket, clientAddress = TCPserver.accept()
    except:
        # 如果产生异常就什么都不做，跳过else的事情去做下一步
        pass
    else:
        # 如果没产生异常就把该socket添加到list
        clientList.append((clientSocket, clientAddress))
        print(clientList)
        # 设置该客户端socket为非堵塞
        clientSocket.setblocking(False)

    # 遍历list中的socket。一旦其中某个socket收到信息就打印出来   
    for clientSocket, clientAddress in clientList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            # 如果产生异常就什么都不做且跳过else，去收下一个socket
            pass
        else:
            # 如果没产生异常就打印信息
            if recvData:
                print(recvData.decode('utf-8'))
            else:
                clientSocket.close()
                clientList.remove((clientSocket, clientAddress))
                print(f'{clientAddress} has logged off')