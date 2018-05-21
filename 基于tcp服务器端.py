# import socket
#
# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #AF_INET 基于网络   SOCK_STREAM  基于流式的方式 tcp 协议  这两个在一起就是 网络通信是基于tcp 协议的
# phone.bind(('127.0.0.1',8080))
# # 绑定是 IP 地址加端口的形式 要写成元组的形式  这样才能在网络中标识 唯一的程序
# phone.listen(5)  # 最大可以挂 5个链接
# print("检验上一步是否运行")
# conn,addr=phone.accept()# accept 相当于拿到一个tcp 链接  #  会拿到对方的链接  和 IP 地址
# conn.send('pl'.encode('utf-8'))
#  # 在这个位置卡住了
# msg=conn.recv(1024)  # 接收消息 客户端发来的消息
# print('客户端发来的消息',msg)
# conn.send(msg.upper())
# conn.close() # 关闭 tcp  三次的 链接
# phone.close()
#    #  socket 底层实现的 机制 ：
#    #  用 socket.socket 产生了一个对象给phone 也就是实例化的过程
#    #  然后传两个参数  ： 也就是封装的过程 一个是地址家族 一个是 tcp 协议  socket.AF_INET,socket.SOCK_STREAM
#    #  断开链接  有数据的概念  谁的数据发完了 谁就先结束
from socket import *
ip_port=('127.0.0.1',8086)
back_log=5
buffer_size=1024
tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log) # 有几个用户请求
while True:
    print(' 服务端开始运行了')
    conn,addr=tcp_server.accept() # 服务器阻塞 一旦多出了一个 终止另一个客户端 客户端这一步  如果不加抛出异常处理 则会出现异常
    print('双向链是',conn)
    print('客户端地址',addr)
    while True:
        try:
            data=conn.recv(buffer_size)
            print('客户端发来的消息是',data.decode('utf-8'))
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
tcp_server.close()
