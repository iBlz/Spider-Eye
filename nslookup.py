import os

def install():
    os.system("apt install update")
    os.system("apt install upgrade")
    os.system("pkg install dnsutils")
    print(" Nslookup Installed!")
