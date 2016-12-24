# Server side
import socket
# Address
HOST = '49.140.77.39'
PORT = 8000

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
# passively wait, 3: maximum number of connections in the queue
print "waiting for connection...."
s.listen(3)
# accept and establish connection
conn, addr = s.accept()
# receive message
print 'raspberry ip address:', addr[0]
# send message
# close connection
conn.close()
