# import re

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     y = re.findall("^From (\S+@\S+)", line)
#     if len(y) != 0:
#         print(y)

# 在 + 或者 * 后面加 ？可以控制贪婪（不加 ？ ）/非贪婪（加 ？ ）匹配
# string = 'jacklu.net@gmail.com'
# print(re.findall('^j.+?\.', string))

# string = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# print(re.findall('\S+?@\S+', string))

# 在此作业中，您将通读并解析带有文本和数字的文件。您将提取文件中的所有数字并计算这些数字的总和。
import re

handle = open('regex_sum_331556.txt')
num_sum = 0
for line in handle:
    numbers = re.findall('[0-9]+', line)
    if numbers:
        for number in numbers:
            num_sum += int(number)
print(num_sum)


