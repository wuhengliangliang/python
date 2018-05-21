import random
# ret=random.sample([11,22,33,44],3)#后面的那个位数控制选择几个数
# print(ret)
# ret=[1,2,3,4,5,56,78,69]
# random.shuffle(ret)  #顺序打乱
# print(ret)
def v_code():
    ret=''
    for i in range(6):
        num=random.randint(0,9)
        alf=chr(random.randint(65,122))
        random.choice([num,alf])
        s=str(random.choice([num,alf]))
        ret+=s
    return ret
print(v_code())