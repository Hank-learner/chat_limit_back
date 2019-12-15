#!/usr/bin/env python3.6

import socket
import sys
import threading

name=input("Enter your Username : ")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host='127.0.0.1'
port=1235
s.connect((host,port))
s.setblocking(True)


def msg_input():
    # print('waiting for input')
    while True:
        msg=input('> ')
        if len(msg)!=0:
            new_msg='@'+name+'> '+msg
            s.send(new_msg.encode('utf-8'))
        else:
            continue

def msg_read():
    # print('reading')
    while True:
            data=s.recv(1024).decode('utf-8')
            if(len(data)!=0):
                print(data)
            else: 
                continue
    
threading.Thread(target=msg_input).start()
threading.Thread(target=msg_read).start()
