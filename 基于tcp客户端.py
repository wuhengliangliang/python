# import socket
# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone.connect(('127.0.0.1',8080)) # 拨电话  拨 的就是服务器端的元组  也就是 ip + 端口
# phone.send('hello'.encode('utf-8')) # 客户端的发送消息的出口
# data1=phone.recv(1024)  # 这一步来接收服务端发来的消息
# data2=phone.recv(1024)
# print('收到服务端的发来的消息：',data1,data2)

            #  服务启动的目标是 永远的运行下去

from socket import *
ip_port=('127.0.0.1',8086)
back_log=5  # 发起的链接数量
buffer_size=1024
tcp_client=socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
while True:
    msg=input('>>:').strip()
    if not msg:continue
    tcp_client.send(msg.encode('utf-8'))
    print('客户端发来的消息')
    data=tcp_client.recv(buffer_size)
    print('收到服务端发来的消息',data)
tcp_client.close()
