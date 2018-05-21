from socket import *
import time
buffer_size=1024
ip_port=('127.0.0.1',8082)
udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)
while True:
    data,addr=udp_server.recvfrom(buffer_size)
    print(data)
    if not data:
        fmt='%Y-%m-%d %X'
    else:
        fmt=data.decode('utf-8')
    back_time=time.strftime(fmt)
    udp_server.sendto(back_time.encode('utf-8'),addr)
