#多态的概念 ：一类事物有多种形态
#不同对象可以调用相同方法
#多态的概念指出了对象如何通过他们共同的属性和动作来操作及访问，而不需考虑他们具体的类
class H2O:
    def __init__(self,name,temperature):
        self.name=name
        self.temperature=temperature
    def turn_ice(self):
        if self.temperature<0:
            print("[%s][%s]温度太低结冰"%(self.name,self.temperature))
        elif self.temperature>0 and self.temperature<100:
            print('[%s]液化成水'%self.name)
        elif self.temperature>100:
            print('[%s]温度太高变成了水蒸气'%self.name)
class Water(H2O):
    pass
class Ice(H2O):
    pass
class Steam(H2O):
    pass
w1=Water('水',25)# w1和i1和s1分别是不同的对象
i1=Ice('冰',-10)
s1=Steam('水蒸气',3000)
w1.turn_ice()
i1.turn_ice()
s1.turn_ice()
#接口就是函数
print("___"*100)
def func(obj): #obj为对象  多态反映执行时候的状态
    obj.turn_ice()  #    不同的对象 去调用相同的方法 就是多态的体现、
func(w1)            #    一种方式多种实现  采用一个接口来实现多种功能
func(i1)            #  继承 可以改变和扩展

