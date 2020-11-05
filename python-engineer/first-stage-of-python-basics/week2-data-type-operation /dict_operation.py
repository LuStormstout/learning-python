# coding:utf-8

# 字典中的 key 是唯一的，数据量没有限制
user = {'username': 'jacklucn', 'age': '29'}

# dict.update(new_dict) 更新 dict
user.update({'age': '30', 'top': 174})
print(user)

# dict.setdefault(key, value) 获取 key 对应的值 对应的 key 不存在的话就会新增，返回 value （已存在或新增的）
value = user.setdefault('birthday', '2020-01-01')
print(user, value)

# dict.keys() 获取当前字典中所有的 key 返回一个 key 集合的伪列表
# 伪列表：不具备列表的所有功能，通过 list() 函数可以转换成真正的列表
user_keys = user.keys()
print(user_keys)  # 伪列表
print(list(user_keys))  # 通过 list() 函数转换成真正的列表

# dict.values() 获取当前字典中的所有 value 返回一个 value 集合的伪列表
user_values = user.values()
print(user_values)
print(list(user_values))

# dict.get(key, default=None) 获取指定 key 的值，default：如果不存在返回 default 的值，默认是 None 获取不到也不会报错
# [] 直接获取如果获取不到会报错 但是效率大于 dict.get()
username = user.get('username')
print(username)

# dict.clear() 清空当前字典中的所有内容
my_dict = {'name': 'zhangsan', 'age': '1400'}
print(my_dict)
my_dict.clear()
print(my_dict)

# dict.pop(key) 删除指定 key 对应的内容，key 不存在会报错，成功返回对应的值
pop_value = user.pop('age')
print(pop_value)
print(user)

# dict.copy() 将当前字典复制出一个新的字典 新的字典和原来的字典内存地址不同
user_copy = user.copy()
print(user_copy, id(user), id(user_copy))

# 字典中 in ，not in 以及 dict.get()
print('username' in user)
print('username' not in user)

# dict.popitem() 删除当前字典中末尾的元素并将其返回 返回值用元组包裹 ('key', '对应的 value')
user_popitem = user.popitem()
print(user_popitem)
