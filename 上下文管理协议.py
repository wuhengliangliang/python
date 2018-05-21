class Open:
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
        # return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
#相当于实例化的过程 f=Open()
# init 会在with 这一行之前触发
with Open('a.txt') as f:#with 里面 执行异常时候回直接触发exit 代码块
    print('=====>执行代码块')
    # print(asdsad)#不存在的变量
    print("=====>>>")
print("00000000")# exit 在文件中执行完后去运行


# 我们知道在操作文件对象的时候可以这么写
# with open('a.txt') as f:
#     2 　　'代码块'
# 上述叫做上下文管理协议，即with语句，为了让一个对象兼容with语句，必须在这个对象的类中声明__enter__和__exit__方法
#
# 复制代码
#
# class Open:
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
#         # return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('with中代码块执行完毕时执行我啊')
# with Open('a.txt') as f:
#     print('=====>执行代码块')
#     # print(f,f.name)
# 复制代码
#
# __exit__()
# 中的三个参数分别代表异常类型，异常值和追溯信息, with语句中代码块出现异常，则with后的代码都无法执行
#
# 复制代码
#
#
# class Open:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('with中代码块执行完毕时执行我啊')
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#
#
# with Open('a.txt') as f:
#     print('=====>执行代码块')
#     raise AttributeError('***着火啦,救火啊***')
# print('0' * 100)  # ------------------------------->不会执行
# 复制代码
# 如果__exit()
# 返回值为True, 那么异常会被清空，就好像啥都没发生一样，with后的语句正常执行
#
# 复制代码
#
#
# class Open:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('with中代码块执行完毕时执行我啊')
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         return True
#
#
# with Open('a.txt') as f:
#     print('=====>执行代码块')
#     raise AttributeError('***着火啦,救火啊***')
# print('0' * 100)  # ------------------------------->会执行
# 复制代码
#
# 复制代码
#
#
class Open:
    def __init__(self, filepath, mode='r', encoding='utf-8'):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        # print('enter')
        self.f = open(self.filepath, mode=self.mode, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('exit')
        self.f.close()
        return True # return true 时就会把异常吃掉 意味着with 语句结束了
    def __getattr__(self, item):
        return getattr(self.f, item)
with Open('a.txt', 'w') as f:
    print(f)
    f.write('aaaaaa')
    f.wasdf  # 抛出异常，交给__exit__处理

 #执行代码块
    #在没有异常的情况下，整个代码块运行完毕后去触发__exit__,他的三个参数都为none
# 有异常的情况下，从异常出现的位置直接触发__exit__
# 如果 __exit__为true 代表吞掉了异常
# 如果 __exit__不为true 代表吐出了异常
# exit 的运行完毕就代表了整个with 语句的执行完毕
# 用途或者说好处：
#
# 使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
#
# 在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处