#!/bin/python
import threading
import hashlib


class Cracker:
    def __init__(self, wordlist, password_hash):
        self.wordlist = wordlist
        self.password_hash = password_hash
        self.crack()

    def crack(self):
        with open(self.wordlist, 'r') as file:
            for password in file:
                print(password)
                h = hashlib.sha256(password.encode('utf-8')).hexdigest()
                print(h)
                if h == self.password_hash:
                    print(f'Password found: {password} : {h}')
                    break
            print('Password not found in wordlist')


if __name__ == '__main__':
    password_cracker = Cracker('wordlist.txt', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08')
