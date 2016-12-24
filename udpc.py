import socket
ipaddr=""#your ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    s.sendto("client",(ipaddr,9999))
    data,addr = s.recvfrom(1024)
    if data:
        break

s.close()
