# coding:utf-8

"""
Python 异常处理

try:
    <代码块1>
except <异常的类型>:
    <代码块2>

通用异常类型 Exception
try:
    <代码块1>
except Exception as e:
    <代码块2>

具体异常捕获

多重异常捕获：
    写多个 except:
    except(异常类型1, 异常类型2, ...) as e:

"""


def upper(str_data):
    try:
        new_str = str_data.upper()
        return new_str
    except Exception as e:
        print('程序出错了:{}'.format(e))
