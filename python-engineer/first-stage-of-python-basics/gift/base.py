# coding:utf-8

import os

from common.utils import check_file

"""
    1、确定用户表中每个用户的信息字段
    2、读取 user.json 文件
    3、写入 user.json （检测该用户是否存在），存在则不写入
"""


class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()

    def __check_user_json(self):
        check_file(self.user_json)

    def __check_gift_json(self):
        check_file(self.gift_json)


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')

    base = Base(user_json=user_path, gift_json=gift_path)
