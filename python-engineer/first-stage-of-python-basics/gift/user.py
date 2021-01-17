# coding:utf-8

"""
    1、抽奖函数 随机判断第一层（level1） 1：50%  2：30%  3：15%  4：5%
    2、抽奖函数 随机判断第二层（level2） 1：80%  2：15%  3：5%
    3、抽奖函数 获取到对应层级的真是奖品，并随机一个奖品，查看奖品 count 是否为 0，不为零则中奖同时提醒用户且奖品数量减 1，更新奖品到 user 表
              中的 gifts 中
              数量为 0，则未中奖
"""

import os
import random
from base import Base
from common.error import NotUserError, RoleError, UserActiveError, CountError
from common.utils import timestamp_to_string


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username

        self.user = None
        self.name = None
        self.role = None
        self.gifts = None
        self.create_time = None

        self.gift_random = list(range(1, 101))

        super(User, self).__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()

        if self.username not in users:
            raise NotUserError(f"user '{self.username}' does not exist")

        current_user = users.get(self.username)

        if current_user.get('active') is False:
            raise UserActiveError(f"user '{self.username}' is not available")

        if current_user.get('role') != 'normal':
            raise RoleError('permission denied by normal')

        self.user = current_user
        self.name = current_user.get('username')
        self.role = current_user.get('role')
        self.gifts = current_user.get('gifts')
        self.create_time = timestamp_to_string(current_user.get('create_time'))

    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gift_list = []

        for level_one, level_one_pool in gifts.items():
            for level_two, level_two_pool in level_one_pool.items():
                for gift_name, gift_info in level_two_pool.items():
                    gift_list.append(gift_info.get('name'))
        return gift_list

    def choice_gist(self):
        self.get_user()
        first_level, second_level = None, None
        level_one_count = random.choice(self.gift_random)

        if 1 <= level_one_count <= 50:
            first_level = 'level1'
        elif 51 <= level_one_count <= 80:
            first_level = 'level2'
        elif 81 <= level_one_count < 95:
            first_level = 'level3'
        elif level_one_count >= 95:
            first_level = 'level4'
        else:
            raise CountError('level_one_count should be 0-100')
        gifts = self._Base__read_gifts()
        level_one = gifts.get(first_level)

        level_two_count = random.choice(self.gift_random)
        if 1 <= level_two_count <= 80:
            second_level = 'level1'
        elif 81 <= level_two_count < 95:
            second_level = 'level2'
        elif 95 <= level_two_count < 100:
            second_level = 'level3'
        else:
            raise CountError('level_two_count should be 0-100')
        level_two = level_one.get(second_level)

        if len(level_two) == 0:
            print('可惜 你没有中奖')
            return False
        gift_names = []
        for k, _ in level_two.items():
            gift_names.append(k)

        gift_name = random.choice(gift_names)
        gift_info = level_two.get(gift_name)
        if gift_info.get('count') <= 0:
            print('可惜 你没有中奖')
            return False

        gift_info['count'] -= 1
        level_two[gift_name] = gift_info
        level_one[second_level] = level_two
        gifts[first_level] = level_one
        self._Base__save(gifts, self.gift_json)

        self.user['gifts'].append(gift_name)
        self.update()
        print(f'恭喜你获得 {gift_name}')

    def update(self):
        users = self._Base__read_users()
        users[self.username] = self.user
        self._Base__save(users, self.user_json)


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user = User(username='张飞', user_json=user_path, gift_json=gift_path)

    # print(user.name)
    # print(user.create_time)
    # print(user.gifts)
    # print(user.role)

    # result = user.get_gifts()
    # print(result)

    user.choice_gist()
