from socket import *
ip_port=('127.0.0.1',8087)
buffer_size=1024
udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)
data1=udp_server.recvfrom(1024)
print('第一次收到的客户端发来的信息',data1)
data2=udp_server.recvfrom(26)
print("第二次发来的消息",data2)