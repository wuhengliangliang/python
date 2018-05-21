# AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError 输入/输出异常；基本上是无法打开文件
# ImportError 无法引入模块或包；基本上是路径问题或名称错误
# IndentationError 语法错误（的子类） ；代码没有正确对齐
# IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError 试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C 被按下
# NameError 使用一个还未被赋予对象的变量
# SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError 传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
# 导致你以为正在访问它
# ValueError 传入一个调用者不期望的值，即使值的类型是正确的
# 为什么需要异常处理  ：
# 为了保证程序的健壮性与容错性，即在遇到错误时程序不会崩溃，我们需要对异常进行处理
  #  错误  ： 语法错误  和逻辑错误

#使用if 判断式
age=input(">>>:")
if age.isdigit():
    int(age)
elif age.isspace():
    print("---> 用户输入的空格")
elif len(age)==0:
    print('--->用户输入的为空')
else :
    print('其他非法输入')
# if 判断虽然可以做异常处理 但是必须为相同代码 写重复的操作  可读性变得极其的底
  #python 为每一种异常定制一个类型，然后提供了一种特定的语法结构用来进行异常处理

# 如果错误发生的条件是不可预知的，则需要用到try...except：在错误发生之后进行处理
# #基本语法为
# try:
#     被检测的代码块
# except 异常类型：
#     try中一旦检测到异常，就执行这个位置的逻辑
                                  #  举例 如下  ：
try :
    age = input(">>>")
    int(age) # 主逻辑
    num2 = input(">>:")
    int(num2) # 主逻辑
except ValueError as e :
    print(e)