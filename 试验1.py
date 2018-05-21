import time
person_list=['alex','wupengqi','yuanhao',]
def ask_way(person_list):
    # print('-'*60)
    if len(person_list)==0:
        return "没人知道"
    person=person_list.pop(0)
    if person =='linhaifeng':
        return '%s说：我知道'%person
    print("hi[%s],敢问路在何方"%person)
    print("%s回答道:我不知道，但是念与你有缘我帮你问问%s"%(person,person_list))
    time.sleep(1)
    res=ask_way(person_list)
    # print('--')
    return res
res=ask_way(person_list)
# print(">>>>>"*20)
print(res)