import random
# ret=random.random()
# ret=random.randint(1,3)
# ret=random.randrange(1,3)
# ret=random.choice([11,22,33,44])
ret=random.sample([11,22,33,44],3)#后面的那个位数控制选择几个数
print(ret)
ret=[1,2,3,4,5,56,78,69]
random.shuffle(ret)  #顺序打乱
print(ret)
def v_code():
    ret=''
    for i in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,122))
        random.choice([num,alf])
        s=str(random.choice([num,alf]))
        ret+=s
    return ret
print(v_code())
#寻找路径
#os 模块 是与操作系统交互的一个接口
#os.removedirs() 删除文件 直到找到不为空的文件 停止
#os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
# os.curdir  返回当前目录: ('.')
# os.pardir  获取当前目录的父目录字符串名：('..')
# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()  删除一个文件
# os.rename("oldname","newname")  重命名文件/目录
# os.stat('path/filename')  获取文件/目录信息/创建时间修改时间 ，
# 模式 节点数 链接，最多的是上一次的访问时间修改时间
# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")  运行shell命令，直接显示
# os.environ  获取系统环境变量
# os.path.abspath(path)  返回path规范化的绝对路径
# os.path.split(path)  将path分割成目录和文件名二元组返回
# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间

# (* * *)
#
# 1
# 2
# 3
# 4
# 5
# 6
# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0)
# sys.version        获取Python解释程序的版本信息
# sys.maxint         最大的Int值
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称
# 进度条：
#
#
# import sys,time
# for i in range(10):
#     sys.stdout.write('#')
#     time.sleep(1)
#     sys.stdout.flush()
# json
#
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# ----------------------------序列化
# import json
#
# dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
# print(type(dic))  # <class 'dict'>
#
# j = json.dumps(dic)
# print(type(j))  # <class 'str'>

# f = open('序列化对象', 'w')
# f.write(j)  # -------------------等价于json.dump(dic,f)
# f.close()
# -----------------------------反序列化<br data-filtered="filtered">
# import json
#
# f = open('序列化对象')
# data = json.loads(f.read())  # 等价于data=json.load(f)

# 复制代码
#import json

# dct="{'1':111}"#json 不认单引号
# dct=str({"1":111})#报错,因为生成的数据还是单引号:{'one': 1}

# dct = '{"1":"111"}'
# print(json.loads(dct))

# conclusion:
#        无论数据是怎样创建的，只要满足json格式，
# 就可以json.loads出来,不一定非要dumps的数据才能loads
                          # 就其本质而言，正则表达式（或
# RE）是一种小型的、高度专业化的编程语言，（在Python中）它内嵌在Python中，并通过
# re
# 模块实现。正则表达式模式被编译成一系列的字节码，然后由用
# C
# 编写的匹配引擎执行。
#
# 字符匹配（普通字符，元字符）：
#
# 1
# 普通字符：大多数字符和字母都会和自身匹配
# >> > re.findall('alvin', 'yuanaleSxalexwupeiqi')
# ['alvin']
#
# 2
# 元字符：.^ $ *+ ? {}[] | ( ) \
#  \
#     元字符之. ^ $ *+ ? {}

# import re
#
# ret = re.findall('a..in', 'helloalvin')
# print(ret)  # ['alvin']
#
# ret = re.findall('^a...n', 'alvinhelloawwwn')
# print(ret)  # ['alvin']
#
# ret = re.findall('a...n$', 'alvinhelloawwwn')
# print(ret)  # ['awwwn']
#
# ret = re.findall('a...n$', 'alvinhelloawwwn')
# print(ret)  # ['awwwn']
#
# ret = re.findall('abc*', 'abcccc')  # 贪婪匹配[0,+oo]
# print(ret)  # ['abcccc']
#
# ret = re.findall('abc+', 'abccc')  # [1,+oo]
# print(ret)  # ['abccc']
#
# ret = re.findall('abc?', 'abccc')  # [0,1]
# print(ret)  # ['abc']
#
# ret = re.findall('abc{1,4}', 'abccc')
# print(ret)  # ['abccc'] 贪婪匹配
# 注意：前面的 *, +,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
#

# ret = re.findall('abc*?', 'abcccccc')
# print(ret)  # ['ab']
# 元字符之字符集［］：

# # --------------------------------------------字符集[]
# ret = re.findall('a[bc]d', 'acd')
# print(ret)  # ['acd']
#
# ret = re.findall('[a-z]', 'acd')
# print(ret)  # ['a', 'c', 'd']
#
# ret = re.findall('[.*+]', 'a.cd+')
# print(ret)  # ['.', '+']
#
# # 在字符集里有功能的符号: - ^ \
#
# ret = re.findall('[1-9]', '45dha3')
# print(ret)  # ['4', '5', '3']
#
# ret = re.findall('[^ab]', '45bdha3')
# print(ret)  # ['4', '5', 'd', 'h', '3']
#
# ret = re.findall('[\d]', '45bdha3')
# print(ret)  # ['4', '5', '3']
# 元字符之转义符 \
#  \
#     反斜杠后边跟元字符去除特殊功能, 比如\.
# 反斜杠后边跟普通字符实现特殊功能, 比如\d
#
# \d
# 匹配任何十进制数；它相当于类[0 - 9]。
# \D
# 匹配任何非数字字符；它相当于类[ ^ 0 - 9]。
# \s
# 匹配任何空白字符；它相当于类[ \t\n\r\f\v]。
# \S
# 匹配任何非空白字符；它相当于类[ ^ \t\n\r\f\v]。
# \w
# 匹配任何字母数字字符；它相当于类[a - zA - Z0 - 9
# _]。
# \W
# 匹配任何非字母数字字符；它相当于类[ ^ a - zA - Z0 - 9
# _]
# \b
# 匹配一个特殊字符边界，比如空格 ， & ，＃等
#
# 1
# 2
# 3
# 4
# ret = re.findall('I\b', 'I am LIST')
# print(ret)  # []
# ret = re.findall(r'I\b', 'I am LIST')
# print(ret)  # ['I']
# 现在我们聊一聊\, 先看下面两个匹配：

# import re
#
# ret = re.findall('c\l', 'abc\le')
# print(ret)  # []
# ret = re.findall('c\\l', 'abc\le')
# print(ret)  # []
# ret = re.findall('c\\\\l', 'abc\le')
# print(ret)  # ['c\\l']
# ret = re.findall(r'c\\l', 'abc\le')
# print(ret)  # ['c\\l']
#
# # -----------------------------eg2:
# # 之所以选择\b是因为\b在ASCII表中是有意义的
# m = re.findall('\bblow', 'blow')
# print(m)
# m = re.findall(r'\bblow', 'blow')
# print(m)
# 　　
#
# 元字符之分组()
#

# m = re.findall(r'(ad)+', 'add')
# print(m)
#
# ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '23/com')
# print(ret.group())  # 23/com
# print(ret.group('id'))  # 23
# 元字符之｜
#

# ret = re.search('(ab)|\d', 'rabhdg8sd')
# print(ret.group())  # ab
# re模块下的常用方法

# import re
#

# re.findall('a', 'alvin yuan')  # 返回所有满足匹配条件的结果,放在列表里
# # 2
# re.search('a', 'alvin yuan').group()  # 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# # 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
#
# # 3
# re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配
#
# # 4
# ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
# print(ret)  # ['', '', 'cd']
#
# # 5
# ret = re.sub('\d', 'abc', 'alvin5yuan6', 1)
# print(ret)  # alvinabcyuan6
# ret = re.subn('\d', 'abc', 'alvin5yuan6')
# print(ret)  # ('alvinabcyuanabc', 2)
#
# # 6
# obj = re.compile('\d{3}')
# ret = obj.search('abc123eeee')
# print(ret.group())  # 123

# import re
#
# ret = re.finditer('\d', 'ds3sy4784a')
# print(ret)  # <callable_iterator object at 0x10195f940>
#
# print(next(ret).group())
# print(next(ret).group())
# 注意：
#
# import re
#
# ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
# print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可
#
# ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
# print(ret)  # ['www.oldboy.com']
        ## http://www.cnblogs.com/yuanchenqi/articles/5732581.html   #模块的博客