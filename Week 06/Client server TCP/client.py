import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1",1234))

client_socket.send("Hello from client side!".encode())

response = client_socket.recv(1024).decode()
print("Server says: ", response)

client_socket.close()

