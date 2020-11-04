from socket import *
from select import *
# select is supported by almost all platforms
# but select can listen to only 2048 sockets and use polling to scan each socket, which is inefficient

server_socket = socket(AF_INET, SOCK_STREAM)
address = ('', 1028)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(address)
server_socket.listen(5)
print('listening...')

inputs = [server_socket,]
# running = True

while 1:
    # Call select function, block to wait
    readable, writable, exceptional = select(inputs, [], [])

    for sock in readable:
        # if there is a new client connection
        if sock == server_socket:
            newSocket, newAddress = sock.accept()
            print('accepting...')
            # let select listen to this client socket
            inputs.append(newSocket)

        else:
            # receive the data from the client
            data = sock.recv(1024)
            print(data.decode('utf-8'))
            if data:
                # send double the data we just received
                sock.send(data + b' received!')
            else:
                # remove the socket listened by select
                inputs.remove(sock)
                sock.close()
