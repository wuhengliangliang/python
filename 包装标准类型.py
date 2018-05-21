class List(list):
    def append(self, object_l):
        if type(object_l) is str:
            super().append(object_l)#不用加自己
        else:
            print("只能添加字符串类型")
    def show_midle(self):
        mid_index=int(len(self)/2)
        return self[mid_index]
l1=List('你好啊我是彭亮')
print(l1)
l2=list('helloworld')
print(l2)
l1.append(111111111)
l1.append('sb')
print(l1)
print(l1.show_midle())