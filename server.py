import socket

host = '127.0.0.1'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#SockStream is for TCP

s.bind((host,port))#binds socket with a port

#instruct socket to start listening for incoming TCP connections
s.listen(1)#listen to one connection

#returns a connection with a new socket and address
c,addr = s.accept()
print("Connection from ",addr)

while True:
    data = c.recv(1024)#maximum buffer size
    if not data:
        break
    print "From connected user: " +str(data)
    data = str(data)[::-1]
    print("Sending...")
    c.send(data)

c.close()#close connection


