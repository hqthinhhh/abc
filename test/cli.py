#client .py
import socket
import hashlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 4000))
#s.send(b"Hello, I am B19DCAT191 Client")
server_msg = s.recv(1024)

print("Nhận từ Server: " + server_msg.decode())
server_hash_msg = s.recv(1024)
key = "Hoang Quoc Thinh ok"
print("Hash từ Server" + server_hash_msg.decode())

hash_msg = hashlib.md5((server_msg.decode() + key).encode()).hexdigest()

print("Hash: " + hash_msg)

if hash_msg != server_hash_msg.decode():
    s.send(b"The received message has lost its integrity.")

s.close()
