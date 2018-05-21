# try :
#     age = input(">>>")
#     int(age) # 主逻辑
#     num2 = input(">>:")
#     int(num2) # 主逻辑
# except ValueError as e :
#     print(e)
# except KeyError as e:
#     print(e)
 #  多种错误捕捉
 # 这样会使代码重复  有一种 万能异常 Exception 处理
# try :
#     age = input(">>>")
#     int(age) # 主逻辑
#     num2 = input(">>:")
#     int(num2) # 主逻辑
# except Exception as e :
#     print(e)
# while True:
#     try:
#         age = input(">>>")
#         int(age)  # 主逻辑
#         num2 = input(">>:")
#         int(num2)  # 主逻辑
#         break
#     except Exception as e:
#         print("请重新输入",e)
# #1 异常类只能用来处理指定的异常情况，如果非指定异常则无法处理。
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e: # 未捕获到异常，程序直接报错
#     print e
#
# #2 多分支
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
#
# #3 万能异常Exception
# s1 = 'hello'
# try:
#     int(s1)
# except Exception as e:
#     print(e)
#
# #4 多分支异常与万能异常
# #4.1 如果你想要的效果是，无论出现什么异常，我们统一丢弃，或者使用同一段代码逻辑去处理他们，那么骚年，大胆的去做吧，只有一个Exception就足够了。
# #4.2 如果你想要的效果是，对于不同的异常我们需要定制不同的处理逻辑，那就需要用到多分支了。
#
# #5 也可以在多分支后来一个Exception
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
#
# #6 异常的其他机构
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# #except Exception as e:
# #    print(e)
# else:
#     print('try内代码块没有异常则执行我')
# finally:
#     print('无论异常与否,都会执行该模块,通常是进行清理工作')
#
# #7 主动触发异常
# try:
#     raise TypeError('类型错误')
# except Exception as e:
#     print(e)
#
# #8 自定义异常
# class EgonException(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
#
# try:
#     raise EgonException('类型错误')
# except EgonException as e:
#     print(e)
#
# #9 断言:assert 条件
# assert 1 == 1
# assert 1 == 2
#
# #10 总结try..except
#
# 1：把错误处理和真正的工作分开来
# 2：代码更易组织，更清晰，复杂的工作任务更容易实现；
# 3：毫无疑问，更安全了，不至于由于一些小的疏忽而使程序意外崩溃了；
  # 异常的其他机构
s1='11'
try:
    int(s1)
except IndexError as e :
    print(e)
except KeyError as e :
    print(e)
else:
    print("try 内代码块没有异常则执行")
finally:
    print("无论异常与否，都会执行该操作，通常是进行清理工作")

   #  主动触发异常 的例子
# try :
#     raise TypeError('类型错误')
# except Exception as e :
#     print(e)
#
#    #  自定义异常
# class EgonException(BaseException):
#     def __init__(self,a):
#         self.a=a
# raise EgonException('自定制的异常')


      #  断言
print("dadadfafffg")
assert 1==2  # 当断言错误时候 程序 不会执行断言的下一句 直接抛出异常 断言可与if 用法类似 更简洁
print("dadasd")
  ###  只有在 有些 异常无法预知的情况下 才会用 try .... except  ,其他的逻辑错误英尽量修正