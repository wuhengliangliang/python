import time
num_list=['1','3','5','7','9','10']
def find_num(num_list):
    print('-'*60)
    if len(num_list)==0:
        return "没找到"
    new_num=num_list.pop(0)
    if new_num=='10':
        return '%s已找到'%new_num
    print('[%s]你知道在哪吗？'%new_num)
    print("%s,不知道，我找找%s"%(new_num,num_list))
    time.sleep(3)
    res=find_num(num_list)#出现的错误是字符串的%s一一对应的关系
    print('---')
    return res
res=find_num(num_list)
print(res)





