# server.py
import socket
import hashlib

host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print("Server listening on port", port)

c, addr = s.accept()
print("Connect from ", str(addr))
msg = "Hello, I am B19DCAT191"
key = "Hoang Quoc Thinh"

c.send(msg.encode())
hash_msg = hashlib.md5((msg+key).encode()).hexdigest()
c.send(hash_msg.encode())
client_msg = c.recv(1024)

if client_msg:
    print("Nhận từ Client: " + client_msg.decode())

c.close()
