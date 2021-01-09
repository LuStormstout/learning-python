# coding：utf-8

from functools import reduce

# filter
# 对循环根据过滤条件进行过滤
# filter(func, list)
#   func：对 list 每个 item 进行条件过滤的定义
#   list：需要过滤的列表
#   例：res = filter(lambda x: x > 1, [0, 1, 2]) 返回一个迭代器
#
# map
# 对列表中每个成员是否满足条件返回对应的 True 与 False/None
# map(func, list)
#   func：对 list 每个 item 进行条件是否满足判断
#   list：需要过滤的列表
#   例：res = filter(lambda x: x > 1, [0, 1, 2]) 返回一个迭代器
#
# reduce
# 对循环前后两个数据进行累加
# from functools import reduce
# reduce(func, list)
#   func：对数据累加的函数
#   list：需要处理的列表
#   例：res = filter(lambda x, y: x + y, [0, 1, 2]) 返回数字 3

fruits = ['apple', 'banana', 'orange']

result = filter(lambda x: 'e' in x, fruits)
print(list(result))
print(fruits)


def filter_func(item):
    if 'e' in item:
        return True


filter_result = filter(filter_func, fruits)
print(list(filter_result))

map_result = map(filter_func, fruits)
print(list(map_result))

reduce_result = reduce(lambda x, y: x + y, [0, 1, 2])
print(reduce_result)

reduce_result = reduce(lambda x, y: x + y, [0, 1, 2])
print(reduce_result)

reduce_str = reduce(lambda x, y: x + y, fruits)  # reduce 对字符串累加
print(reduce_str)
