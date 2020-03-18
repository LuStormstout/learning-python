# import demjson
#
# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
#
# json = demjson.encode(data)
# print(json)


# import json
#
# data = '''{
#     "name": "Jacklu",
#     "phone": {
#         "type": "int",
#         "number": "+86 13659330808"
#     },
#     "email": {
#         "hide": "yes"
#     }
# }'''
#
# info = json.loads(data)
# print(info)
# print("Name:", info["name"])
# print(info["email"]["hide"])


# import json
#
# input_data = '''[
#     {
#         "id": "001",
#         "x": "2",
#         "name": "Jacklu"
#     },
#     {
#         "id": "009",
#         "x": "3",
#         "name": "Chuck"
#     }
# ]'''
#
# info = json.loads(input_data)
# print(info)
# print('User count:', len(info))
# for item in info:
#     print('Name:', item['name'])
#     print('Id:', item['id'])
#     print('Attribute', item['x'])

# input address:Jacklucn
# import urllib.request, urllib.parse, urllib.error
# import json
#
# service_url = 'https://jacklucn.com/index/get-json?'
#
# while True:
#     # address = input('Enter location:')
#     address = 'Jacklucn'
#     if len(address) < 1:
#         break
#     url = service_url + urllib.parse.urlencode({'address': address})
#
#     print('Retrieving', url)
#     res = urllib.request.urlopen(url)
#     data = res.read().decode()
#     print('Retrieving', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('============= Failure To Retrieve =============')
#         print(data)
#         continue
#
#     lat = js['results'][0]['geometry']['location']['lat']
#     lng = js['results'][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)
#     quit()

# 从JSON提取数据
#
# 在此作业中，您将编写一个类似于http://www.py4e.com/code3/json2.py的Python程序 。程序将提示您输入URL，使用urllib从该URL读取JSON数据 ，然后解析并从JSON数据中提取注释计数，计算文件中数字的总和，并在下面输入总和：
# 我们为此任务提供了两个文件。一个是示例文件，我们在其中为您提供测试的总和，另一个是您需要进行分配以处理的实际数据。
#
# 样本数据：http : //py4e-data.dr-chuck.net/comments_42.json （Sum = 2553）
# 实际数据：http：//py4e-data.dr-chuck.net/comments_331561.json （总和以51结尾）
# 您不需要将这些文件保存到文件夹中，因为您的程序将直接从URL读取数据。 注意：每个学生的作业都会有不同的数据网址-因此只能使用自己的数据网址进行分析。
# Extracting Data from JSON
#
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_331561.json (Sum ends with 51)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# import urllib.request
# import json
#
# url = 'http://py4e-data.dr-chuck.net/comments_331561.json'
# res = urllib.request.urlopen(url)
# data = res.read().decode()
# json_data = json.loads(data)
# sum_num = 0
# for item in json_data['comments']:
#     sum_num += item['count']
# print(sum_num)


# Calling a JSON API
#
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# API End Points
#
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#
# http://py4e-data.dr-chuck.net/json?
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py
#
# Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.
#
# Test Data / Sample Execution
#
# You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJ1Z9sheJZkFQRDePQqQebCdg".
#
# $ python3 solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 2279 characters
# Place id ChIJ1Z9sheJZkFQRDePQqQebCdg
# Turn In
#
# Please run your program to find the place_id for this location:
#
# Instituto Tecnologico de Santo Domingo
# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJ44v ..."
# Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.

import urllib.request, urllib.parse, urllib.error
import json

base_url = 'http://py4e-data.dr-chuck.net/json?'
params = dict()
params['address'] = 'Instituto Tecnologico de Santo Domingo'
params['key'] = 42
url = base_url + urllib.parse.urlencode(params)
res = None

while True:
    try:
        res = urllib.request.urlopen(url)
    except:
        print("request fail.")
        quit()

    data = res.read().decode()
    json_data = json.loads(data)

    if json_data and 'status' in json_data and json_data['status'] == 'OK':
        print(json_data['results'][0]['place_id'])
        quit()
    else:
        print('request success, check data fail.')
        continue
