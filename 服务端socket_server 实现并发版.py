import socketserver
'''
    def __init__(self,request,client_address,server):
        self.request=request
        self.client_address=client_adress
        self.server=server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish    
'''

class Myserver(socketserver.BaseRequestHandler):# 处理通信 BaseRequestHandler # 来一个新的链接 产生一个实例
    def handle(self): # 通信循环
        print('conn is ：',self.request) #相当于 aceept 接收到的链接  conn
        print('addr is : ',self.client_address)  # 同理相当于 addr
        while True:
              # 收消息
            try :
                data=self.request.recv(1024)
                # if not data:break
                print('接收到的客户端消息是',data)
                  #  发消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
if __name__=='__main__':
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8050),Myserver)  # 实现多线程
    s.serve_forever() # 通信循环  #  相当于最外层的循环 完成链接循环
#  ThreadingTCPServer  链接循环  Myserver 这个是通信循环 套在链接循环里面
  # 每次来一个客户端 都会通过 Myserver 这个类 来实例化得到一个结果
    

