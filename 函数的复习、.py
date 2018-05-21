# 定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可
# 特性:
# 减少重复代码
# 使程序变的可扩展
# 使程序变得易维护
def test():
    pass
    return "我是彭亮啊"#这是函数的返回值 我需要 拿一个变量 来接收返回的值
res=test()  #如果test不加括号接收到的是地址  #test()调用函数 然后 我需要接受它返回的值 如果return 没有返回任何东西 默认返回的是none
#接受过了 我需要打印出来
print(res)
def more_zhi():
    a=1
    b='abc'
    return a,b
re=more_zhi()#如果不想要元组的形式打印出来 就写成 a,b=more_zhi()
print(re)
# def more_zhi():
#     pass
#     return 1,2,3
# a,b=more_zhi()  #这是这种方法的局限性 返回 3个值 却 只有两个接收 所衣蛾会报错
# print(a,b)
def test(x,y,z):
    print(x)
    print(y)
    print(z)
    return y
a=test(1,2,3)
print(a) #主要看返回值
print(">>>>>>"*20)
def test(x,y,z):# 位置参数在形参里面叫做默认参数
    print(x)
    print(y)
    print(z)
    return y
a=test(y=1,z=2,x=3)# 象这种关键字参数无需一一对应 但是不能缺 也不能多
print(a) #主要看返回值
#位置参数必须 一一对应  而且实参会覆盖 形参的赋值
# def test(x,y,z):# 位置参数在形参里面叫做默认参数
#     print(x)
#     print(y)
#     print(z)
#     return y
# a=test(1,2,x=3)#不能传两遍 只能传一遍

#参数组 （*args列表，**kwargs字典）
# 非固定长度参数 *args是以元组的形式表达
print("---->>>"*20)
def test(x,*args):
    return args
a=test(1,[2,3,4,0])#如果没有[2,3,4,0]则为空 因为返回的是args 现在只有x被传入了值
print(a)


print("---->"*20)
def test(x,*args):
    return args
a=test(1,[2,3,4,0,{'name':'pl','age':18}])#如果没有[2,3,4,0]则为空 因为返回的是args 现在只有x被传入了值
print(a)
#如果不想要以列表的形式打印出来 那么在列表前面加入一个*
print("---->"*20)
#
def test(x,*args):
    return args
a=test(1,*[2,3,4,0,{'name':'pl','age':18}])#如果没有[2,3,4,0]则为空 因为返回的是args 现在只有x被传入了值
print(a)
#  *args 除了关键字参数（a=1,这种类型）**字典 其他都可以传
# **kwargs 只能接受关键字参数，如果接收字典的话 在字典前面加入**
def test(**kwargs):
    return kwargs
a=test(name='pl',age=18,a=1,**{'k':1})#这个字典 必须加入**
print(a)
import sys
print(sys.path)


