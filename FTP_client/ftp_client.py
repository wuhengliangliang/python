import socket
import optparse
import  configparser # 这个模块是做文件处理
import json
class ClientHandler():
    def __init__(self):
        self.op=optparse.OptionParser()
        self.op.add_option("-s","--server",dest="server")
        self.op.add_option("-P","--port",dest="port")
        self.op.add_option("-u","--usename",dest="usename")
        self.op.add_option("-p","--password",dest="password")

        self.options,self.args=self.op.parse_args()
        self.verify_args(options,args)
        self.make_connection()
    def verify_args(self,options,args):
        server=options.server
        port=options
        usename=options.usename
        password=options.password
        if int(port)>0 and int(port)<65535 :
            return True
        else:
            exit("the port is 0-65535")
    def make_connection(self):
        self.sock=socket.socket()
        self.sock.connect((self.options.server,self.options.port))  # 在这里面必须定义一个实例变量
    def interactive(self):
        self.authenticate()  # 这一步 直接走验证 # 么有这个方法  需要重新写一个函数 定义一个功能
    def authenticate(self):
        if self.options.usename is None or self.options.password is None:
            usename=input("usename：")
            password=input("password:")
            return self.get_auth_result(self.options.usename,self.options.password)
            # 没有的方法 需要去定义一个函数 当做方法
            # 这一步 是一个函数功能 需要 定义一个函数 来实现这个功能
    def response(self):
        data=self.sock.recv(1024).decode("utf-8")
        data=json.loads(data)
        return data

    def get_auth_result(self,user,pwd):
        data={
            "action":"auth",
            "usename":user,
            "password":pwd
        }
        self.sock.send(json.dumps(data).encode("utf-8"))
        response=self.sock.recv((1024).decode("utf-8"))
        print(response)
ch=ClientHandler()
ch.interactive()
