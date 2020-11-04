# coding:utf-8

# 首字母转换成大写
name = 'zhangSan'
new_name = name.capitalize()
print(new_name)

# 所有字母转换成小写
new_name = name.casefold()
print(new_name)

# 所有字母转换成小写
new_name = name.lower()
print(new_name)

# 所有字母转换成大写
new_name = name.upper()
print(new_name)

# 所有字母大小写转换
new_name = name.swapcase()
print(new_name)

# 字符串长度补齐 不足用 0 填充 足不做改变
new_name = name.zfill(10)
print(new_name)

# 查询字符串中某个字符出现的次数 没有返回 0
new_name = name.count('a')
print(new_name)

# startswith(): 匹配以某字符开始的 区分大小写
# endswith(): 匹配以某字符结束的 区分大小写
info = "We believe in the transformative power of engaging different perspectives."
result = info.startswith('We')
print(result)
result = info.endswith('perspectives.')
print(result)

# 从左往右 以 0 开始
# find(): 查询字符串中的元素 返回一个整型 找不到返回 -1
# index(): 查询字符串中的元素 返回一个整型 找不到报错
result = info.find('in')
print(result)
result = info.index('in')
print(result)

# strip(): 将去掉字符串两边的字符，默认是去掉左右两边的空格
# lstrip(): 去掉左边的
# rstrip(): 去掉右边的
info = ' engaging different perspectives.'
print(info.strip())
print(info.lstrip(' e'))
print(info.rstrip('.'))

# replace(old, new, max): 替换字符串中的指定字符, max 替换次数
info = ('iPhone 供应情况每天可能有所不同，你可稍后实时查看今天的供应情况，也可以立即在线选购并选择其他购买方式。预约系统的开放时间为每天上午 6:00。 '
        '如果你参加了 iPhone 年年焕新计划，请查询升级换购资格，然后预约到 Apple Store 零售店购买新 iPhone。')
print(info.replace('iPhone', '****', 2))

# isspace() 返回 bool 仅仅是空格的话返回 True 否则返回 False
# istitle() 判断字符串是否是一个标题类型 返回 bool 每个字母的首字母都大写的话就认为是 title 返回 True
# isupper() 返回 bool 是否都是大写
# islower() 返回 bool 是否都是小写

# 格式化字符串 发短信、邮件、通知时
print('my name is %s, my age is %s' % ('Jacklu', 29))
message = '您好，今天是%s，您的手机号码：%s 已经欠费了，请尽快重置。'
print(message % ('星期四', '13659338888'))

# format()
message = '您好，今天是 {}，您的手机号码：{} 已经欠费了，请尽快重置。'
date = '2020-01-01'
phone_number = '13659330808'
print(message.format(date, phone_number))
print(f'您好，今天是 {date}，您的手机号码：{phone_number} 已经欠费了，请尽快重置。')
