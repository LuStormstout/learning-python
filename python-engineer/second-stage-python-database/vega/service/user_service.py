# coding:utf-8

from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    def login(self, username, password):
        result = self.__user_dao.login(username=username, password=password)
        return result

    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username=username)
        return role

    def insert(self, username, password, email, role_id):
        self.__user_dao.insert(username=username, password=password, email=email, role_id=role_id)
