# coding:utf-8

import time

print(time.time())
print(time.localtime())
time.sleep(2)
print(time.localtime())

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strptime('2020-12-28', '%Y-%m-%d'))
