#假如父类名改变 子类调用父类的名字全部得得替换，所以可扩展性比较差
class Vehicle:
    def __init__(self,name,speed,load,power):
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power
    def run(self):
        print("开动1")
        print("开动2")
        print("开动3")
class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        super().__init__(name,speed,load,power,)#运用super 时候 不用输入self
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power
        self.line=line
    def show_info(self):
        print(self.name,self.line)
    def run(self):
        super().run()#子类调用父类的方法，父类名.函数名加（self）
        print("%s %s地铁，开动了"%(self.name,self.line))

line13=Subway('蚌埠地铁','10km/s',1000000,'电',13)
line13.show_info()
line13.run()