import json
dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))  # <class 'dict'>
j = json.dumps(dic)
print(type(j))  # <class 'str'>