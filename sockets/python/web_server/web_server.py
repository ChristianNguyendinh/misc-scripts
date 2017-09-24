'''
WIP practice web server
'''

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection Address: ', addr

while 1:
	data = conn.recv(BUFFER_SIZE)

	# ignore body, assume GET request for now
	if '\r\n\r\n' in data:
		print "Recieved Data: ", data
		break
	print "Recieved Data: ", data

conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n <h1>body</h1>')
conn.close()
