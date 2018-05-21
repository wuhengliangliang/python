def test(x):
    y=2*x+1
    return y #返回值 需要一个变量来接收
y=test(3)
print(y)
#调用同一个函数是  最新的那一个
#使用函数的好处：减少代码重用 保持代码一致性  易于维护， 可扩展性
#过程定义 就是没有返回值
def test2():
    msg="hello wu da lang"
    print(msg)
    return 1,2,3,4,['alex'],{'name':'alex'},None   #默认返回元组的形式
    #不加返回值  会出现none
t1=test2()
print(t1)
def calc(d,f,m):
    res=d**f**m
    return res
c=calc(3,4,2)
print(c)
def ts(x,y,z):#位置参数必须一一对应,缺一不行多一不行
    print(x)
    print(y)
    print(z)
ts(1,2,3)
def handle(x,type="mysql"):
    print(x)
    print(type)
handle('hello','sqlite')#传什么 给什么 ，不传 可以默认赋值的那个
def test1(x,*args):
    print(x)
    print(args)
test1(1,2,3,4,5,6,*['x','y','z'])#剩下的直接用元组的形式表现出来,
# 加星号  就可以全部单个表现出来
# 一个参数不能传两遍值  否则 会报错
def test(x,**kwargs):
    print(x)
    print(kwargs)
test(1,y=2,z=3)#**是以字典的形式显现出来，并且 一个参数不能传两遍值
def test(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
test(1,1,2,255,12,12,z=1,y=2,k=3)#在实参中不能与形参中出现相同的参数变量
test(1,*[1,2,3],**{'k':1,'l':3})#传入的列表可以变成元组的形式，字典还是字典
                    #局部变量与全局变量
#顶头写的  没有任何缩进  定义的变量就是全局变量
#程序中定义的变量为局部变量
name="lhf"
#定义的函数需要调用出来  才能运用全局变量
print(name)
def change_name():
    name="帅的很牛逼"
    print(name)
change_name()#在函数体内加入一个global 就是全局的意思
name='的更高'
def yangjian():
    global name
    print('我要飞',name)
def qupenfei():
    name='白痴'
    print('你是',name)
yangjian()
qupenfei()
#如果函数内部 没有global 关键字：
# 只能读取全局变量，无法重新赋值
#但是对于可变类型，可以对内部元素进行操作
#有变量的声明
#如果函数中有global 关键字，变量本质上就是全局变量的值，可读取，可赋值
name=["产品经理",'廖博士']
def qupengfei():
    global name
    name="飞"
    print("我要",name)
qupengfei()
#如果函数中有global 关键字，变量本质上就是全局变量的值，可读取，可赋值
name=["产品经理",'廖博士']
def qupengfei():
    name.append("田占龙")
    print("我要",name)
qupengfei()

#def qupengfei():错误的式例，表示不能把局部变量放在全局变量的前面
  #  name='自己'
 #   global name
   # print("我要",name)
#qupengfei()
    #    在表示全局变量的时候 一般是大写 局部变量是小写 这是规范
NAME='海峰'
def huangwei():
    name="黄伟"
    print(name)
    def liuyang():
        name="刘洋"
        print(name)
        def nulige():
            name="胡志华"
            print(name)
        print(name)
        nulige()
    liuyang()
    print(name)
huangwei()
name="杠娘"
def weihou():
    name="陈卓"
    def weiweihou():
        global name
        name='冷静'
    weiweihou()
    print(name)
print(name)
weihou()
print(name)


name="杠娘"
def weihou():
    name="陈卓"
    def weiweihou():
        nonlocal name#指定上一级的变量
        name='冷静'
    weiweihou()
    print(name)
print(name)
weihou()
print(name)


def bar():
    print('from foo')
bar()
def foo():
    print('from foo')
foo()
#函数即是变量
#只要有定义的函数 调用 无论在下面还是上面都是可以的
# def add(d,f):
#     print(f+d)
# add(3,35)
# def logger(n):
#     with open('日志记录','a') as f:
#         f.write('我是%s'%n)
# def action1(n):
#     print('wo')
#     logger(n)
# action1(10)
                       #加法器
def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(1,2,3,4,888,45,12)


def zd(*args,**kwargs):
    print(*args)
    # print('name:%s'%kwargs)
    for i in kwargs:
        print('%s:%s'%(i,kwargs[i]))
zd(job='it',hobby='lanqiu',height='100')
                           #关于不定长参数的位置
#*args(无命名)放在左边  元组，**kwargs （字典）参数放在右边
#如果有默认参数，放左边。
