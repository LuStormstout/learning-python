# coding:utf-8

import sys

# sys.modules python 启动时加载的模块，返回列表
# sys.path 返回当前 python 的环境路径，返回列表
# sys.exit() 退出程序，无返回值
# sys.getdefaultencoding() 获取系统编码，返回字符串
# sys.platform 获取当前系统平台，返回字符串
# sys.version 获取 python 版本，返回字符串
# sys.argv 程序外部获取参数，返回列表

# print(sys.modules)
# print(sys.path)
# sys.exit()
code = sys.getdefaultencoding()
print(code)

print(sys.platform)
print(sys.version)
print(sys.argv)
