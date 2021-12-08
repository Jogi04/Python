#!/bin/python

import hashlib

password = input('Enter password to hash: ')
h = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(h)
