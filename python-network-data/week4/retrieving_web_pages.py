# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())


# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# # url = 'http://www.dr-chuck.com/page1.htm'
# url = 'https://jacklucn.com'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))


# Scraping Numbers from HTML using BeautifulSoup
# extracting numbers and compute the sum of the numbers in the file
# 用 BeautifulSoup 在网页上爬取数字 并且求和
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = 'http://py4e-data.dr-chuck.net/comments_331558.html'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('span')
# num_sum = 0
# for tag in tags:
#     num = int(tag.string)
#     if num:
#         num_sum += num
# print(num_sum)


# Following Links in Python
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
# 在此作业中，您将编写一个在http://www.py4e.com/code3/urllinks.py上扩展的Python程序 。该程序将使用urllib从下面的数据文件中读取HTML，从定位标记中提取href = vaues，扫描相对于列表中第一个名称处于特定位置的标记，然后点击该链接并重复处理多次并报告您找到的姓氏。

# Start at: http://py4e-data.dr-chuck.net/known_by_Savin.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: K
# 从以下 位置开始：http://py4e-data.dr-chuck.net/known_by_Savin.html
# 在位置18（名字为1）找到链接。点击该链接。重复此过程7次。答案是您检索的姓氏。
# 提示：您要加载的最后一页名称的第一个字符是：K

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Savin.html'
loop_count = 1
while loop_count < 8:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    if loop_count == 7:
        print(tags[17].string)
    url = tags[17].get('href')
    loop_count += 1
