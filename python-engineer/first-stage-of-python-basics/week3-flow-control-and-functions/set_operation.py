# coding:utf-8

# 集合是不重复元素的序列 无序 无索引概念 帮助 list 去重 处理列表和元组的一种临时类型
# set() 函数创建集合
# set.add(item) 在集合中添加一个元素 无返回值 重复的值只会添加一次 其他的会被忽略
# set.update(iterable) 将新的元素加入到当前的集合中 无返回值
# set.remove(item) 删除集合中的某个元素 元素不存在直接报错 无返回值
# set.clear() 清空当前集合中的所有元素 无返回值
# del 删除集合

a_list = ['python', 'django', 'flask', 'python']
a_set = set()
a_set.add(a_list[0])
a_set.add(a_list[1])
a_set.add(a_list[2])
a_set.add(a_list[-1])
print(a_set)
a_set.add(True)
a_set.add(None)
print(a_set)
a_set.update([1, 2, 3])
print(a_set)
a_set.remove(2)
print(a_set)
a_set.clear()
print(a_set)

# 获取两个集合的差集
# 差集：a，b 两个集合 由所有属于 a 切不属于 b 的元素组成的集合叫做 a 与 b 的差集
# a_set.difference(b_set) 返回集合的差集
a_set = {'zhangsan', 'lisi', 'wangmazi', 'jacklucn'}
b_set = {'xiaozhang', 'xiaoli', 'xiaowang', 'jacklucn'}
new_set = a_set.difference(b_set)
print(new_set)

# a_set.intersection(b_set...) 可以传入多个集合
# 交集：两个集合或者多个集合分别拥有相同的元素集
c_set = {'关羽', '张飞', '赵云', 'wangmazi', 'jacklucn'}
new_set = a_set.intersection(b_set, c_set)
print(new_set)

# a_set.union(b_set...)
# 并集：两个以上集合所有的不重复元素的集合（去重）
new_set = a_set.union(b_set, c_set)
print(new_set)

# a_set.isdisjoint(b_set) 判断两个集合是否包含相同的元素 没有返回 True 有相同的元素返回 False
d_set = {'曹操', '司马懿'}
print(a_set.isdisjoint(d_set))  # 没有相同的返回 True
print(a_set.isdisjoint(b_set))  # 有相同的返回 False
