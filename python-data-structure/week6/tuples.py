# x = ('zhangsan', 'lisi', 'wangmazi')
# print(x[2])
#
# y = (1, 9, 2)
# print(y)
# print(max(y))
# for item in y:
#     print(item)

# (x, y) = (4, 'fred')
# print(y)
# (a, b) = (99, 98)
# print(a)

# d = dict()
# d['v1'] = 99
# d['v2'] = 100
# for (k, v) in d.items():
#     print(k, v)
# tups = d.items()
# print(tups)

# tuples are comparable
# print((5, 1, 2) < (5, 0, 2))

# d = {'a': 10, 'b': 1, 'c': 22}
# t = sorted(d.items())
# print(t)
# for k, v in sorted(d.items()):
#     print(k, v)

# c = {'a': 10, 'b': 1, 'c': 22}
# tmp = list()
# for k, v in c.items():
#     tmp.append((v, k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)

# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print(y)

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# 10.2编写程序以通读mbox-short.txt并找出每个消息在一天中的小时分布。 您可以通过找到时间，然后使用冒号将字符串第二次拆分，从“发件人”行中拉出小时。
# 来自stephen.marquard@uct.ac.za 2008年1月5日星期六09:14:16
# 累积每小时的计数后，请打印出计数，按小时排序，如下所示。

name = "mbox-short.txt"
handle = open(name)
tmp = dict()
for line in handle:
    if line.startswith('From') and len(line.split()) > 2:
        hour = line.split()[5][:2]
        tmp[hour] = tmp.get(hour, 0) + 1

tmp = sorted(tmp.items())
for k, v in tmp:
    print(k, v)

# 列出文件中出现次数前五的单词
name = "clown.txt"
handle = open(name)
words = handle.read().split()
dic = dict()
for word in words:
    dic[word] = dic.get(word, 0) + 1

tmp = list()
for k, v in dic.items():
    tmp.append((v, k))

tmp = sorted(tmp, reverse=True)
for v, k in tmp[:5]:
    print(v, k)

