from socket import *
import hmac,os
secret_key=b'pengliang'
def conn_auth(conn):
    '''
    认证客户端链接
    :param conn:
    :return:
    '''
    print('开始验证新链接的合法性')
    msg=os.urandom(1)
    conn.sendall(msg)
    h=hmac.new(secret_key,msg)
    digest=h.digest()
    respone=conn.recv(len(digest))
    return hmac.compare_digest(respone,digest)
def data_handler(conn,buffer_size=1024): # 处理通信循环
    if not conn_auth(conn):
        print('该链接不合法，关闭')
        conn.close()
        return
    print('连接合法，开始通信')
    while True:
        data=conn.recv(buffer_size)
        if not data:break
        conn.sendall(data.upper())

def server_handler(ip_port,bufsize,backlog=5): # 处理链接循环
    '''
    只处理链接
    :param ip_port:
    :return:
    '''
    tcp_socket_server=socket(AF_INET,SOCK_STREAM)
    tcp_socket_server.bind(ip_port)
    tcp_socket_server.listen(backlog)
    while True:
        conn,addr=tcp_socket_server.accept()
        print('新连接[%s:%s]' %(addr[0],addr[1]))
        data_handler(conn,bufsize)

if __name__ == '__main__':
    ip_port=('127.0.0.1',8041)
    bufsize=1024
    server_handler(ip_port,bufsize)