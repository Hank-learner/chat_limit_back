#!/usr/bin/env python3
import pymysql
import socket
import threading
import queue

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.socket(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host='127.0.0.1'
port=1235
server.bind((host,port))
server.listen()

conn=pymysql.connect("localhost","root","your_password","chat")
cursor=conn.cursor()

t=[]
users=0
print('Online:'+str(users)+'\n')

def read(connection,q):
    try:
        while True:
            data=connection.recv(1024).decode('utf-8')
            print(data)
            q.put(data)
            #print(data.split('>')[0].split('@')[1])
            #print(data[(len(data.split('>')[0])+2):])
            sql_query="INSERT INTO chats(name,msg) VALUES('{0}','{1}')".format(data.split('>')[0].split('@')[1],data[(len(data.split('>')[0])+2):])
            # print(sql_query)
            try:
                cursor.execute(sql_query)
                conn.commit()
            except Exception as e:
                print(f'Exception:{e}')
    except Exception:
        pass

def write(connection,q):
    global users
    try:
        while True:
            if(q.empty()==False):
                data=q.get()
                if len(data)!=0:
                    for a in t:
                        if a!=connection:
                            #print('Sent:{0} Sent By:{1}'.format(data,data.split('>')[0].split('@')[1]))
                            a.send(data.encode('utf-8'))
                else:
                    break
            else:
                continue
    except Exception:
        pass
    finally:
        print('client Diconnected')
        users-=1
        t.remove(connection)
        print('Online:'+str(users)+'\n')
        connection.close()
        
def client_thread(connection):
    global users
    users+=1
    print('Online:'+str(users)+'\n')
    q=queue.Queue()
    threading.Thread(target=read,args=(connection,q),daemon=True).start()
    threading.Thread(target=write,args=(connection,q),daemon=True).start()    

while True:
    try:
        connection, address=server.accept()
        t.append(connection)
        threading.Thread(target=client_thread,args=(connection,),daemon=True).start()
    except:
        break

connection.close()
server.close()

