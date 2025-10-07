import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",1234))
server_socket.listen(1) 
print("Server is waiting for connection..")
conn, addr =server_socket.accept()
print(f"Connected with {addr}")

data = conn.recv(1024).decode()
print("Client says: ", data)
conn.send("hello from server ! ".encode())

conn.close()
