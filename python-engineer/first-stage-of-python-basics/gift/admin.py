# coding:utf-8


import os

from base import Base
from common.error import NotUserError, UserActiveError, RoleError


class Admin(Base):

    def __init__(self, username, user_json, gift_json):
        self.username = username

        self.user = None
        self.role = None
        self.name = None
        self.active = None

        super().__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user is None:
            raise NotUserError(f"user '{self.username}' does not exist")

        if current_user.get('active') is False:
            raise UserActiveError(f"user '{self.username}' is not available")

        if current_user.get('role') != 'admin':
            raise RoleError('permission denied')

        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.active = current_user.get('active')

    def __check(self):
        self.get_user()
        if self.role != 'admin':
            raise Exception('permission denied')

    def add_user(self, username, role):
        self.__check()
        self._Base__write_user(username=username, role=role)

    def update_user_active(self, username):
        self.__check()
        self._Base__change_active(username=username)

    def update_user_role(self, username, role):
        self.__check()
        self._Base__change_role(username=username, role=role)

    def add_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check()
        self._Base__write_gift(first_level=first_level, second_level=second_level, gift_name=gift_name,
                               gift_count=gift_count)

    def delete_gift(self, first_level, second_level, gift_name):
        self.__check()
        self._Base__gift_delete(first_level=first_level, second_level=second_level, gift_name=gift_name)

    def update_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check()
        self._Base__gift_update(first_level=first_level, second_level=second_level, gift_name=gift_name,
                                gift_count=gift_count, is_admin=True)


if __name__ == '__main__':
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    admin = Admin('jacklu', user_path, gift_path)

    # print(admin.username)

    # admin.add_user(username='张飞', role='normal')
    # admin.update_user_role(username='张飞', role='normal')

    # admin.add_gift(first_level='level1', second_level='level1', gift_name='糖豆', gift_count=100)
    # admin.delete_gift(first_level='level1', second_level='level1', gift_name='糖豆')
    admin.update_gift(first_level='level1', second_level='level2', gift_name='iPhone11', gift_count=1000)
