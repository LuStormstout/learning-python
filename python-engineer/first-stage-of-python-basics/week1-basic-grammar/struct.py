# coding:utf-8

import os

print(os.getcwd())
print('今天开始重新系统的学习一下 python')
print('这是一个 python 程序')

name = 'Jacklu'
age = 29
weight = 62.1

print(name)
print(age)
print(weight)
print(type(name))
print(type(age))
print(type(weight))

print('今天的天气很糟糕啊', end='')
print('希望明天的天气能够好一些')

print(id(name))  # 这是一个简单注释练习

'''
    这是一个注释块这就是联系注释用的
    这样的注释我们将来会对函数进行注释
'''

if __name__ == '__main__':
    print(os.getcwd())

print('又回到了一级代码块')

# result = input('请出入你的名字：')
# print(result)

color = '红色'
price = 1998.00

if __name__ == '__main__':
    print(color)
    print(price)

info = 'iphone 12 pro 可以预约了'
result = '12' in info
result2 = 'pro' not in info
print(result, result2)

users = ['zhangsan', 'lisi', 'wangmazi']  # 列表 值可以修改

'''
    元组 占用空间比列表小 值不可修改 如果一个元组中只有一个值的话那么类型是他本来的类型
    例如：tuple_test = (1) 那么 tuple_test 是 int 类型
'''
users_tuple = ('zhangsan', 'lisi')
users_dict = {'name': 'zhangsan', 'age': 18}  # 可以修改的 不支持 *

a = 1
b = 2
c = 3
d = a + b + c
d += c
print(d)  # 9
d -= a
print(d)  # 8

e = b * c
print(e)  # 6
f = c / b
print(f)

print(a == b)
