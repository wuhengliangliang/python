from socket import *
ip_port=('127.0.0.1',8050)
back_log=5
buffer_size=1024
tcp_client=socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
while True:
    msg=input('>>').strip()
    # if not msg:continue
    # if msg=='quit':break
    tcp_client.sendto(msg.encode('utf-8'), ip_port) # tcp 需要编码
    data=tcp_client.recv(buffer_size)
    print('收到服务端发来的消息',data.decode('utf-8'))
