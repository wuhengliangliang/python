import hashlib           #加密方式
obj=hashlib.md5()
obj.update("hello".encode("utf8"))

print(obj.hexdigest())
obj.update("pl".encode("utf8"))
print(obj.hexdigest())
