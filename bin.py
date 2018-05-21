#同级文件去寻找路径
# import os
# print(os.getcwd())
# os.chdir("test11")
# print(os.getcwd())
# print(os.listdir())
# print(os.stat('我.py'))
import time,sys
for i in range(10):
    sys.stdout.write('#')
    print(i)
    time.sleep(0.2)
    sys.stdout.flush()
