from socket import *
ip_port=('127.0.0.1',8087)
buffer_size=1024
tcp_client=socket(AF_INET,SOCK_DGRAM)
tcp_client.sendto(b'hello',ip_port)   # 这种黏包 是数据量小导致黏包
tcp_client.sendto(b'pengliang',ip_port)  # 在udp 中传入的数据不用编码
tcp_client.sendto(b'egon',ip_port) # 字符串前面加b 是以字节发送