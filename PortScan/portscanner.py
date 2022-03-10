import threading
import socket
from queue import Queue

target = "192.168.0.18"
queue = Queue()
open_ports = []
thread_lists = []

def scan(port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,port))
		return True
	except:
		return False
		


def get_ports(ports):
	for p in range(ports):
		queue.put(p)
		
		
def worker():
	while not queue.empty():
		port = queue.get()
		if scan(port):
			print("Port {} is open".format(port))
			open_ports.append(port)
		else:
			pass

def run_scanner(ports):
	get_ports(ports)
	
	for t in range(1000):
		threads = threading.Thread(target=worker)
		thread_lists.append(threads)
	for thr in thread_lists:
		thr.start()
	for th in thread_lists:
		th.join()
	print(open_ports)
	
run_scanner(9000)
	
