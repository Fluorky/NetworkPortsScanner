#!/bin/python3
import pyfiglet
import sys
import socket 
from datetime import datetime as dt



if len(sys.argv) == 2:
     target = socket.gethostbyname(sys.argv[1])
else:
     print("\nIncorrect output parameter : (")
     print("Syntax --> python3 (or python) NetworkPortsScanner.py <IP Address>\n")

#Banner

banner = pyfiglet.figlet_format("NETWORK SCANNER 2077")
print(banner)

print("\n"+"~" * 50)
print("Scanning host ~> {}".format(target))
print("Start time: {}".format(dt.now()))
print("~" * 50+"\n")

try:
     for port in range (8000,8002):
          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          socket.setdefaulttimeout(1)
          result = s.connect_ex((target,port))

          if result == 0:
               print("<~ Port {} is open and unfiltered ~>".format(port))

          else: 
               print("<~ Port {} is NOT open and unfiltered ~>".format(port))
          s.close

except KeyboardInterrupt:
     print("<~ Interrupt ~>")
     sys.exit()

except socket.gaierror:
     print("<~ !Incorrect host name! ~>")
     sys.exit()
except socket.error:
     print("<~Connection error")
     sys.extit()