#client .py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 4000))

s.send(b"Hello, I am B19DCAT191 Client")


server_msg = s.recv(1024)

print("Nhận từ Server: " + server_msg.decode())

s.close()
