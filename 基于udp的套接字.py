#  在 udp 中没有 链接这一说法 所以 没有 listen
#
# udp 服务端
# ss=socket() # 创建一个服务器的套接字
# ss.bind()
# inf_loop:
#     cs = ss.recvfrom()/ss.sendto() # 对话（接收与发送）
# ss.close()  # 关闭服务器套接字
#
# udp 客户端
#
# cs=socket() # 创建客户套接字
# comm_loop:  # 通讯循环
#     cs.sendto()/cs.recvfrom()  # 对话（发送/接收）
# cs.close()   # 关闭客户端套接字

