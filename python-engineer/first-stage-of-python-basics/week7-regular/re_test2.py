# coding:utf-8


import re


def check_url(url):
    result = re.findall(r'[a-zA-Z]{4,5}://\w*\.*\w+\.\w+', url)
    if len(result) != 0:
        return True
    else:
        return False


def get_email(data):
    result = re.findall(r'.+@.+\.[a-zA-Z]+', data)
    return result


html = ('<div class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')


def get_html_data(data):
    result = re.findall(r'style="(.*?)"', data)
    return result


def get_all_html_data(data):
    result = re.findall(r'="(.+?)"', data)
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
