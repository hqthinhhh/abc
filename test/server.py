# server.py

import socket

host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print("Server listening on port", port)

c, addr = s.accept()
print("Connect from ", str(addr))

client_msg = c.recv(1024)

print("Nhận từ Client: " + client_msg.decode())

c.send(b"Hello, I am B19DCAT191 Server")

c.close()
