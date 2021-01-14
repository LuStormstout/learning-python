# coding:utf-8

import os
import json
import time

from common.utils import check_file, timestamp_to_string
from common.error import UserExistsError, RoleError, LevelError
from common.consts import ROLES, FIRST_LEVELS, SECOND_LEVELS

"""
    1、gifts 奖品结构的确定
    2、gifts 奖品的读取
    3、gifts 添加
    4、gifts 初始化
    
    {
      "level1": {
        "level1": {
          "gift_name1": {
            "name": "xx",
            "count": "xxx"
          },
          "gift_name2": {
            "name": "xx",
            "count": "xxx"
          }
        },
        "level2": {},
        "level3": {}
      },
      "level2": {
        "level1": {},
        "level2": {},
        "level3": {}
      },
      "level3": {
        "level1": {},
        "level2": {},
        "level3": {}
      },
      "level4": {
        "level1": {},
        "level2": {},
        "level3": {}
      }
    }

    username
    role normal or admin
    active True or False
    create_time timestamp
    update_time timestamp
    gifts []
    
    username:{username, role, active, ...}
    
"""


class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()
        self.__init_gifts()

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
            raise UserExistsError("user '%s' already exists" % user['username'])

        users.update(
            {user['username']: user}
        )
        self.__save(users, self.user_json)

    def __change_role(self, username, role):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        if role not in ROLES:
            raise RoleError("role is not allowed to be '%s'" % role)

        user['role'] = role
        user['update_time'] = time.time()
        users[username] = user

        self.__save(users, self.user_json)
        return True

    def __change_active(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user

        self.__save(users, self.user_json)
        return True

    def __delete_user(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        delete_user = users.pop(username)
        self.__save(users, self.user_json)
        return delete_user

    def __read_gifts(self):
        with open(self.gift_json, 'r') as f:
            data = json.loads(f.read())
        return data

    def __init_gifts(self):
        data = {
            "level1": {
                "level1": {},
                "level2": {},
                "level3": {}
            },
            "level2": {
                "level1": {},
                "level2": {},
                "level3": {}
            },
            "level3": {
                "level1": {},
                "level2": {},
                "level3": {}
            },
            "level4": {
                "level1": {},
                "level2": {},
                "level3": {}
            }
        }

        gifts = self.__read_gifts()
        if len(gifts) != 0:
            return
        self.__save(data, self.gift_json)

    def __write_gift(self, first_level, second_level, gift_name, gift_count):
        if first_level not in FIRST_LEVELS:
            raise LevelError("'first level' does not exist")
        if second_level not in SECOND_LEVELS:
            raise LevelError("'second level' does not exist")

        gifts = self.__read_gifts()

        current_gift_pool = gifts[first_level]
        current_second_gift_pool = current_gift_pool[second_level]

        if gift_count <= 0:
            gift_count = 1

        if gift_name in current_second_gift_pool:
            current_second_gift_pool[gift_name]['count'] = current_second_gift_pool[gift_name]['count'] + gift_count
        else:
            current_second_gift_pool[gift_name] = {
                "name": gift_name,
                "count": gift_count
            }

        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool
        self.__save(gifts, self.gift_json)

    def __save(self, data, path):
        self.is_not_used()
        json_data = json.dumps(data)
        with open(path, 'w') as f:
            f.write(json_data)

    def is_not_used(self):
        pass


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')

    base = Base(user_json=user_path, gift_json=gift_path)

    # base.write_user(username='jacklu', role='admin')

    # result = base.change_role(username='jacklu', role='admin')
    # print(result)

    # result = base.change_active(username='jacklu')
    # print(result)

    # result = base.delete_user(username='jacklu')
    # print(result)

    # result = base.read_gifts()
    # print(result)

    # result = base.init_gifts()
    # print(result)

    # result = base.write_gift(first_level='level4', second_level='level3', gift_name='楷书字典', gift_count=10)
    # print(result)
