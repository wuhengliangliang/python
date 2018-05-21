#类型：1不可变：不用变量保存状态，不修改变量
def bar():
    print("from foo")
def foo():
    print("from bar")
    return bar()
n=foo()
print(n)
print("-"*20)
def hanle():
    print("from foo")
    return hanle
h=hanle()
h()
#高阶函数：函数接收的参数是一个函数名，或者返回值中包含函数
#递归的缺点  效率低，而调用栈 就可以解决这个问题
                                #  尾调用优化
#尾调用  在函数的最后一步调用另外一个函数（最后一行不一定是函数的最后一步）
#举例说明：
def test(x):
    if x > 1:
        return True
    elif x==1:
        return False
    else:
        return True
res=test(1)
print(res)
#斐波那契数列
print(">>>>>>>"*20)
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(5))
num_l=[1,2,10,5,3,7]
# ret=[]
# for i in num_l:
#     ret.append(i**2)
# print(ret)
#map函数：
num_l=[1,2,10,5,3,7]
def add_one(x):
    return x+1
def reduce_one(x):
    return x-1
def map_test(func,array):
    ret=[]
    for i in array:
        res=func(i)
        ret.append(res)
    return ret
print(map_test(add_one,num_l))
print(map_test(lambda x:x**2,num_l))#匿名函数的功能的简便
#内置函数
res=map(lambda x:x+1,num_l)
print(res)#只能看见有地址 因为是可迭代对象所以看不到 ，需要用for 循环来看出结果
for i in res:
    print(i)

print(list(res)) #map函数是一个迭代器，只能得到一次
print("传的是列表的形式",list(map(reduce_one,num_l)))
mag='aadsfdfds'
print(list(map(lambda x:x.upper(),mag)))

#map函数filter函数
movie_people=['alex_sb','sb_wupeiqi','linhaifeng','yuanhao']
def sb_show(n):
    return n.endswith('sb')
def filter_test(func,array):
    ret=[]
    for p in array:
        if not func(p):
               ret.append(p)
    return ret
res=filter_test(sb_show,movie_people)
print(res)
                             #终极版本：
res=filter_test(lambda n:not n.startswith('sb'),movie_people)
print(res)#可以使匿名的函数也可以是自定义的函数
#reduce在python 3中被放入模块当中
# num_1=[1,2,5,6,45]
# def reduce_test(func,array):
#     res=1
#     for pl in array:
#         res=func(res,pl)
#     return res
# print(list(map(lambda x,y:x*y,num_1)))#对于map函数不能对应两个参数想x,y
#map处理其中的每一个元素跟原列表的顺序一样
#filter 把列表中的值筛选一遍
#用户指定一个初始的值，最后的一个列表出来
num_1=[1,2,5,6,45]
def reduce_test(func,array,it=None):
    if it is None:
        res=array.pop(0)
    else:
        res=it
    for pl in array:
        res=func(res,pl)
    return res
print(reduce_test(lambda x,y:x*y,num_1,100))
#reduce的功能：把两个完整的压缩到一块得到一个值
#合并一个序列 整体压缩到一处得到一个最终的结果
from functools import reduce
num_o=[1,2,3,4]
print(reduce(lambda x,y:x+y,num_o,2))
