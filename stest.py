#!/bin/python3
#Learning about sockets #Connect two nodes togheter.

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, 
#sock_stream is a port
s.connect((HOST,PORT))

#Important to connect to yourself. 
 