import socket
import asyncio

#target = input("[+]Enter the IP address: ")
target = "142.250.182.46"
#port = input("[+]Enter the port: ")

def portScan(port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		
		
		return True
	except:
		return False

	s.close()
for port in range(79, 1024):
	
	p = portScan(port)
	if p:
		print("The result is +ve {} open".format(port))
	else:
		print("not open")
		
	
