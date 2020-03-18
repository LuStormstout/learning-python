# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
#
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# 8.5打开文件mbox-short.txt并逐行阅读。 当您找到以'From'开头的行时，如下所示：
# 来自stephen.marquard@uct.ac.za 2008年1月5日星期六09:14:16
# 您将使用split（）解析“发件人”行，并打印出该行中的第二个单词（即发送消息的人的完整地址）。 然后在末尾打印计数。
# 提示：请确保不要包含以“发件人：”开头的行。
#
# 您可以从http://www.py4e.com/code3/mbox-short.txt下载示例数据

res = open('mbox-short.txt')
count = 0
for line in res:
    if 'From:' in line:
        print(line.split()[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
