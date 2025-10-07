import socket

s = socket.socket()

s.bind(('localhost',9999))
s.listen(3)
print("Listening..")
s.accept()
