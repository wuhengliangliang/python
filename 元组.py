tu=(11,22,33,44)#元组中的元素不可被修改 也不能增加和删除
v=tu[0:2]
print(v)
for item in tu:#可携带对象
    print(item)
li=["adas","dasdasd"]
li.extend((11,22,33,))
print(li)
tuu=(111,"alex",(11,22),[(33,44)],True,33,44)
v=tuu[3][0][0]
print(v)#元组的一级元素不可修改 列表中可以
tuu[3][0]=267
print(tuu)
