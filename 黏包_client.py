from socket import *
ip_port=('127.0.0.1',8056)
buffer_size=1024
back_log=5
tcp_client=socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
tcp_client.send('hello'.encode('utf-8'))   # 这种黏包 是数据量小导致黏包
tcp_client.send('pengliang'.encode('utf-8'))
tcp_client.send('egon'.encode('utf-8'))
