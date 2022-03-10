#Threading module is used for multi-threading.
import threading
#socket module is used for connecting to the target.
import socket
#Queue is used in our module to avoid the re-appearance of the ports in portscanning.
#so the ports will not appear more than 1 time.
from queue import Queue

#change the IP to the target ip that you want to scan.
target = "IP"
#create the empty queue.
queue = Queue()
#Create the empty open_ports list for writing the open ports.
open_ports = []
#Create the thread_lists to append the thread that is created by the program.
thread_lists = []

#Function for checking if the ports is open or close.
def scan(port):
	try:
#Create the socket object.
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connecting to the target with created socket object.
		s.connect((target,port))
#The function returns true if it connects to the port.
		return True
	except:
#The function will return false if it cannot connects to the port.
		return False
		

#Function is used to create queue for ports.
def get_ports(ports):
	for p in range(ports):
#adding the ports to queue.
		queue.put(p)
		
#Function is used to perform the portscan and print the results according to that.		
def worker():
	while not queue.empty():
		port = queue.get()
		if scan(port):
			print("Port {} is open".format(port))
#If the port is open, port is added to the open_ports lists.
			open_ports.append(port)
		else:
#Else it will pass
			pass

#Main function used to call the functions that perform multiple tasks.
def run_scanner(ports):

# To get the port queue
	get_ports(ports)
	
	
#Add the threading for simultanious operations.
#Here we add 1000 threads and added to the thread_lists.
	for t in range(1000):
#Create thread object
		threads = threading.Thread(target=worker)
		thread_lists.append(threads)
	for thr in thread_lists:
		thr.start()
	for th in thread_lists:
		th.join()
		
#Print the open_ports list.
	print(open_ports)
	
	
#Calling the run_scanner function with the port range of 9000.	
run_scanner(9000)
	
