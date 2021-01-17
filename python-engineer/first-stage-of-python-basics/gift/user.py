# coding:utf-8

import os
from base import Base
from common.error import NotUserError, RoleError, UserActiveError
from common.utils import timestamp_to_string


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username

        self.name = None
        self.role = None
        self.gifts = None
        self.create_time = None

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


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user = User(username='张飞', user_json=user_path, gift_json=gift_path)

    # print(user.name)
    # print(user.create_time)
    # print(user.gifts)
    # print(user.role)

    result = user.get_gifts()
    print(result)
