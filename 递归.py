def calc(n):
    print(n)
    if int (n/2)==0:
        return n
    return calc(int(n/2))
calc(10)

import time
person_list=['alex','wupengqi','yuanhao','linhaifeng']
def ask_way(person_list):
    print('-'*60)
    if len(person_list)==0:
        return "没人知道"
    person=person_list.pop(0)
    if person =='linhaifeng':
        return '%s说：我知道'%person
    print("hi[%s],敢问路在何方"%person)
    print("%s回答道:我不知道，但是念与你有缘我帮你问问%s"%(person,person_list))
    time.sleep(1)
    res=ask_way(person_list)
    print('--')
    return res
res=ask_way(person_list)
print(">>>>>"*20)
print(res)

name='hlf'
def mo():
    global name
    name='bbb'
    print(name)
print(name)
mo()
print(name)
#函数作用区域
#函数中没有return 默认为none#
def test1():
    print("in the test")#函数中没有return默认为none
def test():
    print("int the test2")
    return test1
res=test()
print(res())
print('____'*60)
#运行test1#不加括号是内存地址
#在函数中主要看函数的先定义后使用 找他的作用域 来判定，return 是返回
# 若果没有函数 或者函数没加括号调用的是地址， 主要看函数怎么调用
print('_'*60)
def foo():
    name='alex'
    def bar():
        name='pl'
        def sb():
            name='wo'
            print(name)
        sb()
        print(name)
    bar()
    print(name)
print(name)
foo()

