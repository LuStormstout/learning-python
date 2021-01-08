# coding:utf-8

import os
import os.path

# os.getcwd() 返回当前的路径，返回值是字符串
# os.listdir() 返回指定路径下所有的文件或文件夹，返回值是一个列表
# os.makedirs() 创建多级文件夹，没有返回值
# os.removedirs() 删除多级文件夹，没有返回值
# os.rename() 修改文件夹名字，没有返回值
# os.rmdir() 只能删除空文件夹，没有返回值

# os.path.exists() 文件或文件夹是否存在，返回 bool 类型
# os.path.isdir() 是否是文件夹，返回 bool 类型
# os.path.isabs() 是否是绝对路径，返回 bool 类型
# os.path.isfile() 是否是文件，返回 bool 类型
# os.path.join() 路径字符串合并，返回字符串
# os.path.split() 以最后以层路径为基准切割，返回列表

current_path = os.getcwd()
print(current_path)

new_path = '%s/test_path' % current_path
if not os.path.exists(new_path):
    os.makedirs(new_path)

data = os.listdir(current_path)
print(data)

if os.path.exists('./test_path'):
    os.removedirs('./test_path')
# os.rename('test_path', 'test_path_rename')
# os.rmdir('%s/test_path_rename' % current_path)
