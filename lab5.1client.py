import socket

s = socket.socket()

port = 8888

s.connect(('192.168.0.136', port))

data = s.recv(1024)

s.send(b'Take me to your leader...oh im here already!');

print (data)

s.close()
