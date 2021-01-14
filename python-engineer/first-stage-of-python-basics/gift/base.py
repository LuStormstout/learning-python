# coding:utf-8

import os
import json
import time

from common.error import UserExistsError
from common.utils import check_file, timestamp_to_string

"""
    1、确定用户表中每个用户的信息字段
    2、读取 user.json 文件
    3、写入 user.json （检测该用户是否存在），存在则不写入

    username
    role normal or admin
    active True or False
    create_time timestamp
    update_time timestamp
    gifts []
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

    def __read_users(self, time_to_str=False):
        with open(self.user_json, 'r') as f:
            data = json.loads(f.read())

        if time_to_str:
            for username, v in data.items():
                v['create_time'] = timestamp_to_string(v['create_time'])
                v['update_time'] = timestamp_to_string(v['update_time'])
                data[username] = v
        return data

    def __write_user(self, **user):
        if 'username' not in user:
            raise ValueError('missing username')
        if 'role' not in user:
            raise ValueError('missing role')

        user['active'] = True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []

        users = self.__read_users()

        if user['username'] in users:
            raise UserExistsError('username %s had exists' % user['username'])

        users.update(
            {user['username']: user}
        )

        json_users = json.dumps(users)
        with open(self.user_json, 'w') as f:
            f.write(json_users)


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')

    base = Base(user_json=user_path, gift_json=gift_path)

    # base.write_user(username='JackLu', role='admin')
