from socket import *
ip_port=('127.0.0.1',8081)
buffer_size=1024
udp_client=socket(AF_INET,SOCK_DGRAM)  # SOCK_DGRAM 数据报
while True:
    msg=input(">>>").strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)
    data,addr=udp_client.recvfrom(buffer_size)
    print('服务端发来的消息',data.decode('utf-8'))

