from socket import *
import select

# fileno() returns an int type file descriptor, for low-level I/O operations.
serverSocket = socket(AF_INET, SOCK_STREAM)
address = ('', 1027)
serverSocket.bind(address)
serverSocket.listen(5)

# create an epoll object
ep = select.epoll()
# test, to show the file descriptor of the socket
print(serverSocket.fileno())
print(select.EPOLLIN|select.EPOLLET)

# put the socket into epoll event listening
ep.register(serverSocket.fileno(), select.EPOLLIN|select.EPOLLET)

connection_list = {}
address_list = {}

# wait for clients or data from clients
while 1:
    epoll_list = ep.poll()

    for fd, event in epoll_list:
        # print(fd)
        # print(event)

        if fd == serverSocket.fileno():
            clientSocket, clientAddress = serverSocket.accept()
            print(clientAddress)

            # save clientSocket and clientAddress info
            connection_list[clientSocket.fileno()] = clientSocket
            address_list[clientAddress.fileno()] = clientAddress

            # register readable event of the clientSocket in the epoll object
            ep.register(clientSocket.fileno(), select.EPOLLIN|select.EPOLLET)

        # whether this event is the event to receive data
        elif event == select.EPOLLIN:
            # find the socket from the file descriptor because fd can't receive data
            recvData = connection_list[fd].recv(1024)

            if recvData:
                print(recvData.decode('utf-8'))

            else:
                # remove the fd connection from epoll object
                ep.unregister(fd)
                # close the fd connection
                connection_list[fd].close()
                print(f'{clientAddress} is offline')
