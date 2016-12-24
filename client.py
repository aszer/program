import socket
import time
# Address
HOST = '49.140.77.39'
PORT = 8000
address=(HOST,PORT)
request = 'can you hear me?'

# configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send message
while True:
    s.sendto('2',address)
    print "send"
    time.sleep(1)
