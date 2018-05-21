from socket import *
ip_port=('127.0.0.1',8056)
buffer_size=1024
back_log=5
tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
conn,addr=tcp_server.accept()
data1=conn.recv(3)   # 这是 tcp 中有 优化算法 如果 开始接受大于 所有的传送的数据 这会全部接收
print('第一次数据',data1)  #  但是  由于 udp 中没有 优化算法 所以不会 全部接收
data2=conn.recv(4)
print('第二次数据',data2)
