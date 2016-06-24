#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

# check arguments
if len(sys.argv) == 1:
    print("Usage: %s <any string>" % (sys.argv[0]))
    exit(1)

# initialyze the socket for connection
sock = socket.socket()

# try socket to connect to the host:port server
host = socket.gethostbyname('localhost')
port = 5555
print("Client searching for server at: %s:%d" % (host, port))
sock.connect((host, port))

# send server the message
smsg = sys.argv[1]
print("Client sending message: %s" % (smsg,))
sock.send(smsg)

# receive message from server
data = sock.recv(1024)
print("Client received updated message: %s" % (data,))

# close connection socket
sock.close()

