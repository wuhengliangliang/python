# 1：迭代器协议是指：对象必须提供一个next方法，
# 执行该方法要么返回迭代中的下一项 ，要么就引起一个StopIteratior异常，
# 以终止迭代（只能往后走不能往前退）
# 2：可迭代对象：实现了迭代器协议的对象
# （如何实现：对象内部定义一个__iter__()方法）
# 3 协议是一种约定，可迭代对象实现了迭代器协议，
# python 的内部工具（如for循环，sum,min,max函数等）使用迭代器协议访问对象
            # for循环的本质：循环所有对象，全部是使用迭代器协议。
l='hello'
for i in range(len(l)):
    print(i,l[i])
class Foo:
    def __init__(self,n):
        self.n=n
    def __iter__(self): #所有不可迭代的 加入iter 之后 都变得可迭代
        return self
    def __next__(self):
        if self.n==100:
            raise StopIteration("终止")
        self.n+=1
        return self.n #运行过后都保存在 self.n里
f1=Foo(10)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
for i in f1:
    print(i)
   #斐波那契数列
class Fib:
    def __init__(self):
        self.a=1
        self._b=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a>100:
            raise StopIteration("终止")
        self.a,self._b=self._b,self.a + self._b
        return self.a
f1=Fib()
for i in f1:    #只有字典才能 用循环中的 按照序号一一对应输出
    print(i)
print("___"*20)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
#方法二
a=0
b=1
while b<=100:
    print(b)
    a ,b= b,a+b
def fibNum(n):          #斐波那契数列
    a, b = 0, 1
    for i in range(n):
        b, a = a+b, b
    return b
n = int(input(">>:"))
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    print(fibNum(n-2))

