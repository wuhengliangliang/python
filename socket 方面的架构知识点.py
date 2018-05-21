# 客户端/ /服务器架构
# 即c/s架构 包括
# 1.硬件c/s架构（打印机）
# 2.软件c/s架构(客户端/服务器架构)（web服务 ftp）
# Client/Server架构，即客户端/服务器架构。是大家熟知的软件系统体系结构，
# 通过将任务合理分配到Client端和Server端，降低了系统的通讯开销，需要安装客户端才可进行管理操作。
# B/S架构:客户端基本上没有专门的应用程序，应用程序基本上都在服务器端。
# 由于 客户端没有程序，应用程序的升级和维护都可以在服务器端完成，升级维护方便。
  # 利用socket 完成 客户端和服务器端
  #  osi 七层
 # C/S 架构的软件（软件属于应用层）是基于网络通信的
 # 网络的核即一堆协议，协议即标准，你想开发一款基于网络通信的软件，就必须遵循这些标准





    #   SOCKET  是应用层与tcp/ip 协议通信的中间软件抽象层，他是一组接口
    # 在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，
    # 对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。
    # 所以，我们无需深入理解tcp/udp协议，socket已经为我们封装好了，
    # 我们只需要遵循socket的规定去编程，写出的程序自然就是遵循tcp/udp标准的。
