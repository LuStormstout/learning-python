# coding:utf-8

import re


def had_number(data):
    result = re.findall(r'\d', data)
    print(result)
    for i in result:
        return True
    return False


def remove_number(data):
    result = re.findall(r'\D', data)
    print(result)
    return ''.join(result)


def startswith(sub, data):
    _sub = r'\A%s' % sub
    result = re.findall(_sub, data)
    for i in result:
        return True
    return False


def endswith(sub, data):
    _sub = r'%s\Z' % sub
    result = re.findall(_sub, data)
    if len(result) != 0:
        return True
    else:
        return False


def real_len(data):
    result = re.findall(r'\S', data)
    print(result)
    return len(result)


if __name__ == '__main__':
    data = 'I am JackLu, I am 20'
    result = had_number(data)
    print(result)

    result = remove_number(data)
    print(result)

    data = 'Hello Python, I am JackLu. I am 20 year\'s old'
    print(re.findall(r'\W', data))

    result = startswith('sHell', data)
    print(result)

    result = endswith('old', data)
    print(result)

    print(len(data))
    result = real_len(data)
    print(result)
