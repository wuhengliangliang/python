import os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
from score import main  # 这样是找不到 路径的 需要取绝对路径
   #对于 文件包的形式 直接用文件的模块导入 这样不在一个文件包 会找不到 需要进行 PAth 操作
   # PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   #sys.path.append(PATH)
#  以上两步骤 是 基于 不在一个文件包中 调用 另一个文件导入的 方法


if __name__=='__main__':
     main.ArgvHandler()