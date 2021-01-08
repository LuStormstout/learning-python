# coding: utf-8

import base64

# 参数比特（Byte）类型，返回比特（Byte）类型
# base64.encodestring(b'hello') base64 加密
# base64.decodestring(b'xxxx') base64 解密

# 参数比特（Byte）类型，返回比特（Byte）类型，Python3 更推荐使用以下两种
# base64.encodebytes(b'hello') base64 加密
# base64.decodebytes(b'xxxx') base64 解密

replace_one = '%'
replace_two = '$'


def encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError('data need bytes or str.')

    _data = base64.encodebytes(data).decode('utf-8')
    _data = _data.replace('a', replace_one).replace('2', replace_two)
    return _data


def decode(data):
    if not isinstance(data, bytes):
        raise TypeError('data need bytes.')

    replace_one_b = replace_one.encode('utf-8')
    replace_two_b = replace_two.encode('utf-8')
    data = data.replace(replace_one_b, b'a').replace(replace_two_b, b'2')
    return base64.decodebytes(data).decode('utf-8')


if __name__ == '__main__':
    result = encode('你好 python')
    print(result)
    new_result = decode(result.encode('utf-8'))
    print(new_result)
