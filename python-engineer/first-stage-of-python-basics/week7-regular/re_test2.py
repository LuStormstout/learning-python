# coding:utf-8


import re


# re.findall(pattern, str, [, flags])
#   查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表
#
# re.search(pattern, str, flags=0)
#   使用可选的标记搜索字符串中第一次出现的正则表达式模式，如果匹配成功，则返回匹配对象；如果失败，则返回 None
#
# re_search_obj.group(num)
#   返回整个匹配对象，或者编号为 num 的特定子组
#
# re_search_obj.groups()
#   返回一个包含所有匹配子组的元组（如果没有成功匹配，则返回一个空元组）
#
# re.split(pattern, str, max=0)
#   根据正则表达式的模式分隔符，split 函数将字符串分隔为列表，然后返回成功匹配的列表，分隔最多操作 max 次（默认分隔所有匹配成功的位置）
#
# re.compile(pattern, flags=0)
#   定义一个匹配规则的对象
#
# re.match(pattern, str, flags=0)
#   尝试使用带有可选的标记的正则表达式的模式来匹配字符串。如果匹配成功，就返回匹配对象；如果失败就返回 None，返回的对象可以通过 group 来调用


def check_url(url):
    re_g = re.compile(r'[a-zA-Z]{4,5}://\w*\.*\w+\.\w+')
    result = re_g.findall(url)
    if len(result) != 0:
        return True
    else:
        return False


def get_email(data):
    re_g = re.compile(r'.+@.+\.[a-zA-Z]+')
    result = re_g.findall(data)
    return result


html = ('<div class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')


def get_html_data(data):
    re_g = re.compile(r'style="(.*?)"')
    result = re_g.findall(data)
    return result


def get_all_html_data(data):
    re_g = re.compile(r'="(.+?)"')
    result = re_g.findall(data)
    return result


if __name__ == '__main__':
    check_result = check_url('https://jacklucn.com')
    print(check_result)

    email = get_email('jacklu.net@gmail.com')
    print(email)

    html_data = get_html_data(html)
    print(html_data)

    all_html_data = get_all_html_data(html)
    print(all_html_data)

    re_obj = re.compile(('<div class="(.*?)" style="(.*?)">'
        '</div><div class="(.*?)"></div>'))
    res = re_obj.search(html)
    print(res.groups())

    re_obj = re.compile(r'\s')
    res = re_obj.split(html)
    print(res)

    re_obj = re.compile(r'<div class="(.*?)"')
    res = re_obj.match(html)
    print(res.span())
    print(html[:22])
