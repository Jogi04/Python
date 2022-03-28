import sys
import socket

server_address = ('10.0.1.144', 80)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    out_msg = str(input('Message to server: '))
    if out_msg == 'q':
        client_socket.close()
        sys.exit()
    client_socket.send(out_msg.encode())
