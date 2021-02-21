# coding:utf-8

from db.role_dao import RoleDao


class RoleService:
    __role_dao = RoleDao()

    def search_role_list(self):
        result = self.__role_dao.search_role_list()
        return result
