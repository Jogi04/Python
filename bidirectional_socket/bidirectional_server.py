import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 8090))
server_socket.listen(1)
(client_socket, address) = server_socket.accept()
print(address)

while True:
    in_msg = (client_socket.recv(1024)).decode()
    print(in_msg)
    out_msg = str(input('Message to client: '))
    client_socket.send(out_msg.encode())
