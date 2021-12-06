import socket


server_address = ('127.0.0.1', 8090)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    out_msg = str(input('Message to server: '))
    client_socket.send(out_msg.encode())

    in_msg = (client_socket.recv(1024)).decode()
    print(in_msg)
