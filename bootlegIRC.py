"""
SERVER SIDE
"""

HOST = ""
PORT = 1337

import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind ((HOST , PORT))
s.listen(1) *LISTENS FOR 1 CONNECTION
conn , addr = s.accept()
conn.recv(1024) *RECEIVES 1024 BITS WORTH OF DATA ONCE

"""
CLIENT SIDE
"""
HOST = "127.0.0.1" *LOOPBACK ADDRESS
PORT = 1337

import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((HOST , PORT))
s.send(b'test')