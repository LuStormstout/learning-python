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

    def search_count_page(self):
        count_page = self.__user_dao.search_count_page()
        return count_page

    def search_user_list(self, page):
        result = self.__user_dao.search_user_list(page=page)
        return result

    def update_user(self, user_id, username, password, email, role_id):
        self.__user_dao.update_user(user_id=user_id, username=username, password=password, email=email, role_id=role_id)

    def delete_user(self, user_id):
        self.__user_dao.delete_user(user_id=user_id)
