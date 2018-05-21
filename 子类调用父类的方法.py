#调用父类 父类名 加上.___init___
#只有实列化时候 会自动传入一个参数，对象 去调用类方法时候 会自动传self(可以不用加)
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
        Vehicle.__init__(self, '南京地铁', '100km/s', 1000000, '电')
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power
        self.line=line
    def show_info(self):
        print(self.name,self.line)
    def run(self):
        Vehicle.run(self)#子类调用父类的方法，父类名.函数名加（self）
        print("%s %s地铁，开动了"%(self.name,self.line))

line13=Subway('蚌埠地铁','10km/s',1000000,'电',13)
line13.show_info()
line13.run()