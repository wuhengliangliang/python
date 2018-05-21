from socket import *
ip_port=('127.0.0.1',8081)
buffer_size=1024
udp_server=socket(AF_INET,SOCK_DGRAM)  # SOCK_DGRAM 数据报
udp_server.bind(ip_port)
while True:
    data,addr=udp_server.recvfrom(buffer_size) #这一步 加了  addr 可以实现了服务端发去客户端消息
    print('客户端发来的消息', data)
    udp_server.sendto(data.upper(),addr) # 想要实现服务端发到 客户端的消息 必须加一个 addr 双参数的模式
         #   udp 可以接收 空