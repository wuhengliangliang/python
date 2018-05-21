#www.cnblogs.com/jasonenbo/p/6091120.html
info = {
    "k1": 13,
    "k2": True,  # 注意字典中的逗号和列表中的逗号，列表不能作为字典的k,
    # 元组可以作为字典的k
    "k3": [
        11,
        [11, 22],
        (11, 22),
        22,
        33,
    ]
}
print(info)
i = {
    "1": "pengliang",  # 如果1的值用引号这样冒号后面的东西会出现，不用则不出现
    True: "123",
    # [11, 22]:123#注意列表不可用于元组的k值
    (11, 22, 33): 123  # 字典中需要有逗号记住出现过这关问题
}
print(i)
# 字典是无序的
v = info["k1"]  # 根据索引来取字典中对应的值  数字也可以作为k
print(v)
v1 = info["k3"][1][1]  # 记住k有引号的
print(v1)

del info["k3"][2]  # 记住在字典中自能删除一个整体的元组 删除不了元组中的元素

# 因为元组不可修改 不能增加或者删除 而列表可以  可变
print(info)
for pl in info.keys():  # 可以用for来表示，默认输出输出的k
    print(pl)
for pl in info.values():  # 输出其中的值
    print(pl)
for pl in info.keys():  # 一一对应的输出其中的元素，记住在循环后面必须加上冒号
    print(pl, info[pl])
print("-"*20)
for i in info.items():#以括号的形式来一一对应输出key和value的值
    print(i)
dic = {
    "kk1": 'v2',
    "kk2": 'v4'
}
m = dict.fromkeys(["kk1", 123, "999"], 123)  # 注意加入中括号里面传入想要的值
# 后面是中括号里面对应的逗号后面的值，根据序列来创建字典
print(m)
vv1 = dic.get("kk1")  # 得到对应的值在字典中，k不存在时可以默认为none
print(vv1)
dic.pop("kk1")  # 删除字典中的元素
print(dic)
v5 = dic.setdefault('kk1', 123)
print(v5)
dic.update(kk1=123, kk2=456, k5="567")
print(dic)
mm={'k1':123,'k2':456,'k3':789}
for i,v in enumerate(mm.items(),1):#对应序号来输出
    print(i,v)
for i,v in enumerate(mm,1):#对应序号来输出且 不用元组的方式输出
    print(i,v,mm[v])