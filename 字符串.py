test = "xAles"
v1 = test.rstrip("eslxa")
v2 = test.strip()
print(v1)  # 最多匹配
l = "aeiou"
m = "12345"
v = "adadas;dasdasda;fsfff"
m = str.maketrans("adiou", "12345")  # 一一应的关系
new_v = v.translate(m)
print(new_v)
t = "teasdasd"
b = t.partition("s")  # 以什么为分割
print(b)
b1 = t.split("s", 3)  # 找多个分割
print(b1)
# 换行
test2 = "dasdhsakdj\ndsadasda\nsadasdas\n"
v2 = test2.splitlines(False)  # 以换行符来划分换行
print(v2)
test3 = "pengliang"
bb = test3.startswith('l')  # 以什么首字母开头，同理endswith以什么味为结尾
print(bb)
test4 = "aLex"
v3 = test4.swapcase()  # 大小写转换
print(v3)
g = "dasda"
v4 = g[0:-1]  # 获取索引的字符
print(v4)
li = [11, 22, "sd"]  # 注意字母必须用引号括起来
mm = len(li)
print(mm)
gh = "我想上天"  # 把列表当中的元素一个一个输出
index = 0
while index < len(gh):
    f = gh[index]
    print(f)
    index = index + 1
for pl in gh:
    print(pl)
name = "zhengjianwen"
age = "18"
al = name + age  # 字符串修改时候是因为重新生成了字符串（一旦创建 就不可修改）
print(al)
e = "els"
v5 = e.replace("el", "bb")  # 替换
print(v5)
k = range(0, 100, 5)  # 创建连续和不连续的数
print(k)
for pl in k:
    print(pl)
test5 = ("qwe")
print(test5)
ll = len(test5)
print(ll)
m1 = "你是风儿"
l1 = "_".join(m1)
print(l1)
value = "5+9"
n1, n2 = value.split("+")
print(n1, n2)
