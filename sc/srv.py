#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os
import time

# initialyze socket for connect creation
sock = socket.socket()

# creat server socket
host = socket.gethostbyname('localhost')
port = 5555
print("\nServer creating the bound at: %s:%d" % (host, port))
try:
    sock.bind((host, port))
except:
    os.system("fuser -kuv %s/tcp" % (port,))
    time.sleep(5)
    sock.bind((host, port))

# setup socket for maximum number of clients
sock.listen(1)

while True:
    # wait for the client 
    conn, addr = sock.accept()
    print("Server connected the client at (address:port): %s" % (addr,))

    # receive data from the client
    data = conn.recv(1024)
    if not data: break

    # send reformated message
    conn.send(data.upper())

    # close the connection
    conn.close()
