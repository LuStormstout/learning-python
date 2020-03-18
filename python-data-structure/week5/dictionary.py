# array = dict()
# array['name'] = 'Jacklu'
# array['birth'] = '1991-08-09'
# array['money'] = 10
# array['money'] += 1
# print(array)

# string = 'chengdu beijing shanghai lanzhou xian xian xian'
# cities = string.split()
# counts = dict()
# for city in cities:
#     counts[city] = counts.get(city, 0) + 1
#
# print(counts)
# print(list(counts))
# print(counts.keys())
# print(counts.values())
# print(counts.items())
#
# for aaa, bbb in counts.items():
#     print(aaa, bbb)

# name = input('Enter file:')
# handle = open(name)
#
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# big_count = None
# big_word = None
# for word, count in counts.items():
#     if big_count is None or count > big_count:
#         big_word = word
#         big_count = count
#
# print(counts)
# print(big_count, big_word)


# x = dict()
# x['name'] = 'zhangsan'
# x['age'] = 19
# for y in x:
#     print(y)

# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# 9.4编写程序以通读mbox-short.txt并找出谁发送了最多的邮件。 该程序将查找“发件人”行，并将这些行的第二个单词作为发送邮件的人。 该程序创建一个Python字典，该字典将发件人的邮件地址映射到它们出现在文件中的次数计数。 生成字典后，程序将使用最大循环遍历字典以查找最多产的提交者。

name = 'mbox-short.txt'
handle = open(name)
counts = dict()
words = list()
for line in handle:
    if line.startswith('From') and len(line.split()) > 2:
        word = line.split()[1]
        counts[word] = counts.get(word, 0) + 1

big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_count = count
        big_word = word

print(big_word, big_count)

