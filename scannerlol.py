#!/bin/python3
#This will probably be so bad but let's try it out. 

import sys 
import socket
from datetime import datetime

#explain/define the target. 
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4

else: 
        print("Not enough arguments. Invalid.")
        print("Syntax: python3 scannerlol.py <ip>")