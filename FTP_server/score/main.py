import optparse
import socketserver
from conf import settings
from score import server
class ArgvHandler():
    def __init__(self):
        self.op=optparse.OptionParser
        # self.op.add_option('-s','--s',dest='server')  #会产生一个键值对  server 对应的是ip port 对应的是端口
        # self.op.add_option('-P','--port',dest='port')
        options,args=self.op.parse_args(self)
        self.verify_args(options,args)
    def verify_args(self,options,args):
        cmd=args[0]
        if hasattr(self,cmd): # 第一个放self 调用的是属性 第二个 是cmd
            func=getattr(self,cmd)
            func()
    def start(self):
        s=socketserver.ThreadingTCPServer((settings.IP,settings.PORT),server.ServerHandler)
        s.serve_forever()
    def help(self):
        pass
