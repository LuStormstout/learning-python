# import xml.etree.ElementTree as ET
#
# data = '''
# <person>
#     <name>JackLu</name>
#     <phone type="intl">
#         +86 136 **** 0105
#     </phone>
#     <email hide="yes"/>
# </person>
# '''
#
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))


# import xml.etree.ElementTree as ET
#
# data = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>JackLu</name>
#         </user>
#         <user x="7">
#             <id>004</id>
#             <name>Chuck</name>
#         </user>
#     </users>
# </stuff>
# '''
#
# stuff = ET.fromstring(data)
# lst = stuff.findall('users/user')
# print('User count:', len(lst), '\n')
# for item in lst:
#     print('Name:', item.find('name').text)
#     print('Id:', item.find('id').text)
#     print('Attr:', item.get('x'), '\n')


# 从XML提取数据
# http://py4e-data.dr-chuck.net/comments_331560.xml
# 该程序将提示输入URL，使用urllib从该URL读取XML数据 ，然后解析并从XML数据中提取注释计数，计算文件中数字的总和。

# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
#
# counts = tree.findall('.//count')
# Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

# 您将浏览所有<comment>标记，并找到<count>值对数字求和。
# 为了使代码简单一些，您可以使用XPath选择器字符串通过以下代码行遍历XML的整个树，以查找名为“ count”的任何标签：
# 查看Python ElementTree文档，并查找受支持的XPath语法以了解详细信息。您也可以从XML的顶部一直到注释节点，然后遍历注释节点的子节点。

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

cxt = ssl.create_default_context()
cxt.check_hostname = False
cxt.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_331560.xml'
data = urllib.request.urlopen(url, context=cxt).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
num_sum = 0
for item in counts:
    num = int(item.text)
    if num:
        num_sum += num
print(num_sum)
