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
    os.system("fuser -kuv %s/tcp >/dev/null 2>&1" % (port,))
    print("Server tring to recreate the bound - please wait 5 secs !!!")
    time.sleep(5)
    sock.bind((host, port))
    print("Server successfully recreated the bound")

# setup socket for maximum number of clients
sock.listen(1)

while True:
    # wait for the client 
    conn, addr = sock.accept()
    print("Server connected the client at (address:port): %s" % (addr,))

    # receive data from the client
    rmsg = conn.recv(1024)
    if not rmsg: break
    print("Server received from the client the message: %s" % (rmsg,))

    # send reformated message
    if rmsg.isdigit():
        smsg = str(int(rmsg) * 100)
    else:
        smsg = rmsg.upper()
    print("Server sendig the client the new message: %s" % (rmsg,))
    conn.send(smsg)

    # close the connection
    conn.close()
