# dic='{"name":"alex"}'
# f=open('hello','w')
# f.write(dic)   #先把字典写入一个文件
# f_read=open('hello','r')
# data=f_read.read()
# data=eval(data)
# print(data["name"])  #json 把单引号 变成双引号
# import json
# dic={"name":"alex"}
# data=json.dumps(dic)
# f=open("new_hello","w")
# f.write(data)


# import json
# print(data)
# print(type(data))
# i=888
# s='hhellp'
# l=[11,22,33]
# p=json.dumps(i)    #所有的json  都可以把数据类型转换为字符串
# print(p)
# f_read=open("new_hello","r")
# data=json.loads(f_read.read())#可以变换成原来的数据
# print(data)
# import json
# with open("hello","r")as f:   #注意双引号  在文件调用当中
#     data=f.read()
#     data=json.loads(data)
#     print(data["name"])#rb 读的是字节
###----------------------------序列化
import pickle

dic={'name':'alvin','age':23,'sex':'male'}

print(type(dic))#<class 'dict'>

j=pickle.dumps(dic)
print(type(j))#<class 'bytes'>


f=open('序列化对象_pickle','wb')#注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  #-------------------等价于pickle.dump(dic,f)

f.close()
#-------------------------反序列化
import pickle
f=open('序列化对象_pickle','rb')

data=pickle.loads(f.read())  #  等价于data=pickle.load(f)


print(data['age'])#pickle 不可以查看 并且是以字节的方式存储
#需求少 基本用json
#   shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;key必须为字符串，而值可以是python所支持的数据类型

#import shelve
#f = shelve.open(r'shelve.txt')
# f['stu1_info']#空字典= #键值对：{'name':'alex','age':'18'}
# f['stu2_info']={'name':'alvin','age':'20'}
# f['school_info']={'website':'oldboyedu.com','city':'beijing'}
# f.close()
#print(f.get('stu_info')['age'])#去取
                             # xml模块(**)
#
# xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，至今很多传统公司如金融行业的很多系统的接口还主要是xml。
#
# xml的格式如下，就是通过 <> 节点来区别数据结构的:
#
# 复制代码
# < ?xml
# version = "1.0"? >
# < data >
# < country
# name = "Liechtenstein" >
# < rank
# updated = "yes" > 2 < / rank >
# < year > 2008 < / year >
# < gdppc > 141100 < / gdppc >
# < neighbor
# name = "Austria"
# direction = "E" / >
# < neighbor
# name = "Switzerland"
# direction = "W" / >
# < / country >
# < country
# name = "Singapore" >
# < rank
# updated = "yes" > 5 < / rank >
# < year > 2011 < / year >
# < gdppc > 59900 < / gdppc >
# < neighbor
# name = "Malaysia"
# direction = "N" / >
# < / country >
# < country
# name = "Panama" >
# < rank
# updated = "yes" > 69 < / rank >
# < year > 2011 < / year >
# < gdppc > 13600 < / gdppc >
# < neighbor
# name = "Costa Rica"
# direction = "W" / >
# < neighbor
# name = "Colombia"
# direction = "E" / >
# < / country >
# < / data >
# 复制代码
# xml协议在各个语言里的都
# 是支持的，在python中可以用以下模块操作xml：
#
#
# 复制代码
# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
# print(root.tag)
#
# # 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text)
#
# # 只遍历year 节点
# for node in root.iter('year'):
#     print(node.tag, node.text)
# # ---------------------------------------
#
# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
#
# # 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated", "yes")
#
# tree.write("xmltest.xml")
#
# # 删除node
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')
# 复制代码
# 自己创建xml文档：
#
#
# 复制代码
# import xml.etree.ElementTree as ET
#
# new_xml = ET.Element("namelist")
# name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
# age = ET.SubElement(name, "age", attrib={"checked": "no"})
# sex = ET.SubElement(name, "sex")
# sex.text = '33'
# name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
# age = ET.SubElement(name2, "age")
# age.text = '19'
#
# et = ET.ElementTree(new_xml)  # 生成文档对象
# et.write("test.xml", encoding="utf-8", xml_declaration=True)
#
# ET.dump(new_xml)  # 打印生成的格式
# xml协议在各个语言里的都
# 是支持的，在python中可以用以下模块操作xml：
#
#
# 复制代码
# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
# print(root.tag)
#
# # 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text)
#
# # 只遍历year 节点
# for node in root.iter('year'):
#     print(node.tag, node.text)
# # ---------------------------------------
#
# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
#
# # 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated", "yes")
#
# tree.write("xmltest.xml")
#
# # 删除node
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')
# 复制代码
# 自己创建xml文档：
#
#
# 复制代码
# import xml.etree.ElementTree as ET
#
# new_xml = ET.Element("namelist")
# name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
# age = ET.SubElement(name, "age", attrib={"checked": "no"})
# sex = ET.SubElement(name, "sex")
# sex.text = '33'
# name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
# age = ET.SubElement(name2, "age")
# age.text = '19'
#
# et = ET.ElementTree(new_xml)  # 生成文档对象
# et.write("test.xml", encoding="utf-8", xml_declaration=True)
#
# ET.dump(new_xml)  # 打印生成的格式