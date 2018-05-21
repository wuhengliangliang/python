import re  #模糊匹配， 元字符  ..就是中间有几个未知的
t=re.findall("a..x","adsfafafexskl9")
print(t)
o=re.findall("^a..x","adaxafdx")# ^  且只能匹配一个  代表 必须从开头就匹配 匹配不了就失败
print(o)
p=re.findall("a..x$","asdxasdxdasdx")# 最后结尾处有相同 匹配
print(p)
# *（0，+00）
# +（1，,+00）
# ? (0,1)
# {0,}==*,{1,}== + {0,1}== ?  {1,6}
i=re.findall("alx{0,6}","alxxxxxxxdadssa")
print(i)
print(re.findall("q[^a-z]*","q88sa89s"))#尖角号在字符集中加上后
#  只能匹配除了字符集以外的东西
print(re.findall("\([^()]*\)","12+(34*6+2-5*(2-1)"))
print(re.findall("\d+","12-457-84+78*65"))
print(re.findall("\D","12-457-84+78*65"))#D为任何非数字字符
print(re.findall("\w","12-daa457-84+78*65"))
print(re.findall("\W","12-457-84+7fsdf8*65"))
print(re.findall("I\\b","hello I an list"))
print(re.findall("I\\\l","hello I\lan list"))
print(re.findall("(abc)","abcabcabc"))
print(re.match("\w+","445abcabca45645bc"))
print(re.split(" ","44abc abca 4564 5bc"))
print(re.split("[ab]","dsabdasfsakb"))
print(re.sub("\d+","a","asdasdasf487541113asd",3))
print(re.subn("\d","a","asdasdasf487541113asd"))#会加上匹配次数
print(re.compile("\d+"))
