import hmac
import socket

secret_key = b'egg'
sk = socket.socket()
sk.connect(('127.0.0.1',9999))
msg = sk.recv(1024)
h = hmac.new(secret_key,msg)
digest = h.digest()
sk.send(digest)

sk.close()



