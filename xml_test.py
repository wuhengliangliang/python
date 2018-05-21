# import xml.etree.ElementTree as a  #追踪根节点
#
# tree=a.parse("xml_lesson")
# root=tree.getroot()
#print(root.tag)
#  遍历 根节点   只要有地址 就是对象
# for i in root:
#     #print(i.text)
#     #print(i.tag)#tag 打印对象的名字
#     #print(i.attrib)#属性  一个键值对 代表一个属性  一个标签的 属性
#     for j in i :
        #print(j.tag)
        #print(j.attrib)
#text 是标签所包裹的内容
#         print(j.text)
# for node in root.iter("year"):
    #print(node.tag,node.text)
    #如果没有值 则输出none

#     new_year=int(node.text)+1
#     node.text=str(new_year)
#     node.set("updated","yes")# set 增加属性
#     print(node.tag,node.text)
# tree.write("abc.xml")
                                 #删除
# for country in root.findall("country"):#findall可以找多个标签
#     rank=int(country.find("rank").text)
#     if rank>50:
#         root.remove(country)
# tree.write("abd.xml")
import xml.etree.ElementTree as ET
new_xml=ET.Element("namelist")

# <namelist>
#     <name enrolled="yes"></name>
#
# </namelist>
name=ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
pl=ET.SubElement(new_xml,"pl",attrib={"enrolled":"no"})
pl.text="19"
et=ET.ElementTree(new_xml)
et.write("test.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)
