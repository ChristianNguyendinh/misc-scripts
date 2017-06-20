import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection Address: ', addr

while 1:
	data = conn.recv(BUFFER_SIZE)
	if '@)' in data:
		print "Recieved Data: ", data
		break
	print "Recieved Data: ", data
	conn.send(data)

conn.send('END')
conn.close()
