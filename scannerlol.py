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

#Add a banner
print("_" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("_" * 50)
