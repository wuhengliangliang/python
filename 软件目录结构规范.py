#为了增强可读性  可维护性高 必须保持一个层次清晰的目录结构
# 假设你的项目名为foo, 我比较建议的最方便快捷目录结构这样就足够了:
#
# Foo/ 可执行文件
# |-- bin/
# |   |-- foo
# |
# |-- foo/
# |   |-- tests/
# |   |   |-- __init__.py
# |   |   |-- test_main.py
# |   |
# |   |-- __init__.py
# |   |-- main.py
# |
# |-- docs/
# |   |-- conf.py
# |   |-- abc.rst
# |
# |-- setup.py
# |-- requirements.txt
# |-- README
# 简要解释一下:
#
# bin/: 存放项目的一些可执行文件，当然你可以起名script/之类的也行。
# foo/: 存放项目的所有源代码。(1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。(2) 其子目录tests/存放单元测试代码； (3) 程序的入口最好命名为main.py。
# docs/: 存放一些文档。
# setup.py: 安装、部署、打包的脚本。
# requirements.txt: 存放软件依赖的外部Python包列表。
# README: 项目说明文件。
           #第二种 代码风格  必有一种核心目录
           

