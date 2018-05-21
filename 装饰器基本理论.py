#装饰器的本质 就是函数，功能是为其他函数添加附加功能
#原则：
# 不修改被修饰函数的源代码，不修改被修饰函数的调用方式
# import time
# def cal(l):
#     start_time=time.time()
#     res=0
#     for i in l:
#         time .sleep(0.1)
#         res+=i
#     stop_time=time.time()
#     print('函数的运行时间是%s'%(stop_time-start_time))
#     return res
# print(cal(range(100)))
                               #装饰器=高阶函数+函数嵌套+闭包
import time
def foo():
    time.sleep(0.2)
    print('彭亮')
#不修改源代码 不修改foo调用方式
def timer (func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print('运行时间%s'%(stop_time-start_time))
    return func
foo=timer(foo)
foo()

