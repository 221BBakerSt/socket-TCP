import ssl
import socket

# s = socket(AF_INET, SOCK_STREAM)
s = ssl.wrap_socket(socket.socket())

# Connect to Sina server
address = ('www.baidu.com', 443)
s.connect(address)

# Send message to the server
msg = 'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n'
msg = msg.encode('utf-8')
s.send(msg)

# Receive the response from Sina server
buffer = []
while 1:
    data = s.recv(1024)
    if data:
        # data.decode('utf-8')
        buffer.append(data)
    else:
        break
response = b''.join(buffer).decode('utf-8')

s.close()
header, html = response.split('\r\n\r\n', 1)
print(header)
# 把接收的数据写入文件:
f = open('/Users/allen/Desktop/sina.html', 'w')
f.write(html)
f.close
