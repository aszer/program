import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    s.sendto("client",('49.140.77.39',9999))
    data,addr = s.recvfrom(1024)
    if data:
        break

s.close()
