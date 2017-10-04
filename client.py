import socket

host = '127.0.0.1'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#SockStream is for TCP

s.connect((host,port))

message = raw_input('ENTER MESSAGE OR WRITE Q TO QUIT\n ->')
while message != 'Q':
    s.send(message)
    data = s.recv(1024)#receive data from the server
    print 'Received from server: \n ->' +str(data)
    message = raw_input('->')

s.close()