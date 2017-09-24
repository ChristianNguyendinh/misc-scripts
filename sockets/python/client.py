import socket, time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = 'HELLOW WORLD THIS IS MORE THAN 20 CHARACTERS I BELIEVE!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

time.sleep(5) # Do Some Work for 5s

s.send('HERE IS SOME MORE DATA THAT IS LONGER THAN 20 CHARACTERS @)')

data = ''

while 1:
	new_data = s.recv(BUFFER_SIZE)
	if 'END' in new_data:
		data = data + new_data
		break
	data = data + new_data

print "recieved echo'd data: ", data
s.close()
