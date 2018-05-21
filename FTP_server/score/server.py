import  socketserver
import json
import configparser
class ServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            data=self.request.recv(1024).strip()
            data=json.loads(data.decode("utf-8"))
            '''
            {"action":"auth",
            "usename":"yuan",
            "pwd":123
            }
            '''
            if data.get("action"): #判断 action 中是否有命令
                if hasattr(self,data.get("action")): # 只要判断有 action  便会有auth 的功能
                    func=getattr(self,data.get("action"))
                    func(**data)
                else:
                    print("Invalid cmd")
            else:
                print("Invalid cmd")
    def auth(self,**data):
        usename=data["usename"]
        password=data["password"]

        self.authenticate(usename,password)
    def authenticate(self,user,pwa):
        cfg=configparser.ConfigParser()
        cfg.read()

