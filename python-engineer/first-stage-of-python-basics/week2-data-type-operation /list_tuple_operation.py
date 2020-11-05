# coding:utf-8

names = ['zhangsan', 'lisi', 'wangmazi']

# list.append(new_item) 列表中追加元素
# list.insert(index, new_item) 将一个元素添加到 list 的指定位置，当 index 不存在时会直接追加到 list 末尾
append_name = 'zhangsanfeng'
names.append(append_name)
print(names)
insert_name = 'qiaobusi'
names.insert(1, insert_name)
print(names)

# list.count(item) 返回当前列表中某个元素的个数 返回数字 不存在则返回 0
names_count = names.count('lisi')
print(names_count)

# list.remove(item) 删除列表中的某个元素 如果有多个的话 只会删除掉最左边的一个
names.remove('wangmazi')
print(names)

# del 删除变量
# del names

# list.reverse() 当前列表内容顺序颠倒
names.reverse()
print(names)

# list.sort(key=None, reverse=False) 对当前列表内容进行排序 key 参数比较 reverse 按照什么顺序进行排序
# 要保证列表中的元素类型必须相同
names.sort()
print(names)

# list.clear() 清空当前列表内容
names.clear()
print(names)

# list.copy() 将当前列表复制出一个新的列表 返回一个一摸一样的列表
# 浅拷贝 如果是嵌套的多维列表深层的元素还是会和之前的指向同一地址会受到被拷贝列表的影响
# list.deepcopy() 深拷贝 原始变量和新变量完全不共享数据
# 二次复制新变量会和原变量共享内存空间 修改的话会互相影响 数据共享
old_list = ['python', 'django', 'flask']
new_list = old_list
new_list.append('tornado')
print(new_list, old_list)

del new_list
print(old_list)  # del 并不会直接删除内存空间

old_list_copy = ['python', 'django', 'flask']
new_list_copy = old_list_copy.copy()
print(new_list_copy, old_list_copy)
new_list_copy.append('tornado')
print(new_list_copy, old_list_copy)

# list.extend(iterable) 将其他列表或元祖中的元素导入到当前列表中 继承， iterable 列表、元组、字符串（会被打乱成每个字符的列表）、字典（只会拿到 key）
comics = []  # 漫画
history = []
code = []

new_comics = ('七龙珠', '海贼王', '猫和老鼠')
new_history = ('中国历史', '日本历史', '韩国历史')
new_code = ('python', 'django', 'flask')

comics.extend(new_comics)
history.extend(new_history)
code.extend(new_code)

print(comics, history, code)
history.extend(comics)
del comics
print(history)

test = []
test.extend('asdf')
print(test)

# 索引与切片在列表中的使用
# 索引：字符串、列表、元组 从最左边记录的位置就是索引 用数字表示 从 0 开始 字符串列表元组的最大长度减 1 就是索引的长度 对单个元素进行访问
# 切片：访问一定范围内的元素 [0:10] 切片的规则「左含右不含」
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(numbers) - 1)  # 9
print(numbers[9])  # 10
print(numbers[:])  # 返回完整的数据 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:])  # 返回完整的数据 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[:-1])  # 返回少了最后一个元素的所有元素 「左含右不含」[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[3:8])  # [4, 5, 6, 7, 8]
print(numbers[::-1])  # 等同于 list.reverse() 函数 反转内容 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers[-3:-1])  # [8, 9]
print(numbers[0:8:2])  # [1, 3, 5, 7] 步长为 2 每个两个获取一个 从索引 0 开始 到索引 8 结束
print(numbers[0:0])  # 切片生成空列表 []
# 获取和修改列表内容通过索引 list[index] = new_item
# list.index(item) 获取查询内容的索引位置
numbers[3] = 'code'
print(numbers)
numbers[0:2] = ['a', 'b']
print(numbers)
print(numbers.index('code'))
# list.pop(index) 通过索引获取并删除对应的元素 返回对应的元素并删除
pop_item = numbers.pop(9)
print(pop_item)
print(numbers)
del numbers[0]
print(numbers)
