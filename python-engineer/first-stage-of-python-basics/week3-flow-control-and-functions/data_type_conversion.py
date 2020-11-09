# coding:utf-8

# 数据类型转换
# str() int() float()

# 字符串列表转换
# string.split(sep=None, maxsplit=-1) 以一定的规则将字符串切割成列表
#   sep 默认是以空格切割，如果没有空格则不分割 直接生成列表 不能传空字符串
#   maxsplit 根据切割符号切割的次数 默认 -1 无限制
#   返回值：返回一个列表

message = "Reserve and Pick Up We're sorry, but this service is currently unavailable."
message_split = message.split()
print(message_split)
a = 'abc'
print(a.split())  # 没有空格不做切割 ['abc'] 直接生成
b = 'a,b,c'
print(b.split(','))  # ['a', 'b', 'c'] 以逗号「,」 切割
print(b.split(',', 1))  # 只切割一次 ['a', 'b,c']

# 'sep'.join(iterable) 将列表、元组、集合以一定的规则转换成字符串
#   sep 生成字符串用来分割列表每个元素的符号
#   iterable 非数字类型的列表、元组或集合，有数字元素会直接报错 字典也是不行的
#   返回值：返回一个列表
test_list = ['a', 'b', 'c']
test_tuple = ('x', 'y', 'z')
print('/'.join(test_tuple))
test_str = '|'.join(test_list)
print(test_str)
sort_str = 'a b c x f d'
sort_list = sort_str.split()
print(sort_list)
sort_list.sort()
print(sort_list)
sort_str = ' '.join(sort_list)
print(sort_str)

# sorted() 对任何类型进行排序
test_str_new = 'abcxfd'
print(''.join(sorted(test_str_new)))

# string 和 bytes 之间的转换
# bytes 二进制数据流 字符串前面加一个 b 就是 bytes 类型 bytes_str = b'this is bytes' 只支持 ASCII 类型的内容
# string.encode(encoding='utf-8', errors='strict') 将字符串转换成 bytes 返回一个比特类型
#   encoding 将要转换成的编码格式 默认 utf-8
#   errors 出错时的处理方法，默认 strict 直接抛出错误，也可以选择 ignore 忽略错误
# string.decode() 将比特类型转换成字符串类型 参数和 encode 一致 返回一个字符串类型
bytes_str = b'this is bytes'
print(bytes_str, type(bytes_str))
print(bytes_str.capitalize())
print(bytes_str.replace(b'is', b'IS'))
print(bytes_str[0])  # 输出 116 被转换后的二进制值
print(bytes_str.find(b'is'))

str_data = 'my name is 张飞'
encode_str_data = str_data.encode()
print(encode_str_data)
decode_str_data = encode_str_data.decode()
print(decode_str_data)

# dir() 输出对应对象可以使用的的函数
print(dir(list()))
print(dir(test_str_new))

# 列表 元组 集合之间的转换
# set()
# tuple()
# list()
