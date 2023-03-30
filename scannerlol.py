#!/bin/python3
#This will probably be so bad but let's try it out. 

import pyfiglet
import sys 
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("ScannerLoL")
print(ascii_banner)

#explain/define the target. Old version
#if len(sys.argv) == 2: 
#   target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4

#explain/define the target. New Version with ability to choose
target    = input("Enter a IP host to scan: ")  
targetIP  = socket.gethostbyname(target)
sPort = int(input("Enter a start port to scan: "))
ePort = int(input("Enter end port to scan: "))

#else: 
        #print("Not enough arguments. Invalid.")
        #print("Syntax: python3 scannerlol.py <ip>")

#Add a banner
print("_" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("_" * 50)

try: 
        
        for port in range(50,85): #common ports in home routers with open DNS.
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if result == 0:
                        print(f"Port {port} is open")
                s.close()

except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
        
except socket.error:
        print("Could not connect to server.")
        sys.exit()

#run the following in the terminal to scan your network for open ports: 
# python3 scannerlol.py (your IP) 