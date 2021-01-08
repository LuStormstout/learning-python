# coding: utf-8

import hashlib
import time

# hashlib.md5(b'hello')
# hashlib.sha1(b'hello')
# hashlib.sha256(b'hello')
# hashlib.sha512(b'hello')
# 参数都是比特（byte）类型，返回加密后的结果

md5_hash = hashlib.md5(b'123456')
md5_hash_str = md5_hash.hexdigest()
print(md5_hash_str)

base_sign = 'jacklucn'


def custom():
    a_timestamp = str(time.time())
    _token = '%s%s' % (base_sign, a_timestamp)
    hash_obj = hashlib.sha1(_token.encode('utf-8'))
    a_token = hash_obj.hexdigest()
    return a_token, a_timestamp


def b_service_check(token, timestamp):
    _token = '%s%s' % (base_sign, timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        return True
    else:
        return False


if __name__ == '__main__':
    need_help_token, custom_timestamp = custom()
    result = b_service_check(need_help_token, custom_timestamp)
    if result:
        print('验证通过')
    else:
        print('验证失败')
